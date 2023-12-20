import os
import customtkinter as cttk
import tkinter as tk
from tkinter import messagebox
import mysql.connector
import serial
import tkinter.ttk as ttk
import threading
import time



class Dashboard:
    def __init__(self, root, user):
        # serial_port = 'COM5'
        self.root = root
        self.root.title("Dashboard")
        self.root.geometry("1280x1080+50+0")
        self.root.resizable(False, False)
        self.user = user
        self.arduino = None  # Initialize self.arduino to None
        self.db_conn = None  # Initialize db_conn to None
        self.lbl_noOfVehicleEntered =None
        # self.treeview = None



        # Connect to MySQL database
        self.db_conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",  # Replace with your MySQL password
            database="aveesdb"
        )

        # Create a flag to control the RFID scanning thread
        self.rfid_scan_flag = True


        # Start RFID scanning in a separate thread
        self.rfid_thread = threading.Thread(target=self.rfid_scan_background)
        self.rfid_thread.start()
    

        # Create frames for dashboard, settings, and components
        self.dashboard_frame = cttk.CTkFrame(root, width=850, height=450, fg_color=("white", "#4B49AC"))
        self.settings_frame = cttk.CTkFrame(root, width=850, height=450, fg_color=("white", "#4B49AC"))
        self.components_frame = cttk.CTkFrame(root, width=850, height=450, fg_color=("white", "#4B49AC"))

         # Dashboard Inside Widgets
        #No of Vehicles Entered
        self.vehicle_entered_frame = cttk.CTkFrame(self.dashboard_frame, width=250, height=100,fg_color=("#4B49AC", "white"))
        self.vehicle_entered_frame.place(x=30,y=50)

        # Corrected initialization of lbl_noOfVehicleEntered
        self.lbl_noOfVehicleEntered = cttk.CTkLabel(
            self.vehicle_entered_frame,
            text="Total Vehicles: 0",
            font=("Arial", 18, "bold"),
            fg_color=("#4B49AC", "white")
        )
        self.lbl_noOfVehicleEntered.place(x=70,y=20)

        # Initialize the total number of vehicles label
        self.update_total_vehicles_label()

        # Vehicle List Frame
        self.vehicle_list_frame = cttk.CTkFrame(self.dashboard_frame, width=600, height=250, fg_color=("red", "#4B49AC"))
        self.vehicle_list_frame.place(x=70, y=170)

        # Treeview to display vehicle list
        columns = ("Vehicle No", "Entry Time")
        self.treeview = ttk.Treeview(self.vehicle_list_frame, columns=columns, show="headings", selectmode="browse", height=15)
        self.treeview.place(x=10, y=10)

        # Configure column headings
        for col in columns:
            self.treeview.heading(col, text=col)
            self.treeview.column(col, width=150, anchor="center")

        
        # Function to update vehicle list information
        self.update_vehicle_list()




        # Initial frame to show is the dashboard frame
        self.current_frame = self.dashboard_frame
        self.show_frame()

        # Displaying the username on the dashboard
        username_label = cttk.CTkLabel(self.dashboard_frame, text=f"Welcome, {self.user}!", font=("Arial", 16, "bold"))
        username_label.place(x=10, y=20)

        #-----------------------------------SideMenu Frame---------------------------------------
        SideMenuFrame = cttk.CTkFrame(root, width=200, height=450, fg_color=("white", "#4B49AC"))
        SideMenuFrame.place(x=10, y=50)

        sideMenuTitle = cttk.CTkLabel(SideMenuFrame, text=f"AVEES", font=("Arial", 24, "bold"))
        sideMenuTitle.place(x=50, y=10)

        # Dashboard
        btn_dashboard = cttk.CTkButton(SideMenuFrame, text="Dashboard", font=("Arial", 14, "bold"), height=35, width=180,
                                       command=lambda: self.show_frame(self.dashboard_frame))
        btn_dashboard.place(x=10, y=60)

        # Setting
        btn_setting = cttk.CTkButton(SideMenuFrame, text="Setting", font=("Arial", 14, "bold"), height=35, width=180,
                                     command=lambda: self.show_frame(self.settings_frame))
        btn_setting.place(x=10, y=100)

        # Components
        btn_components = cttk.CTkButton(SideMenuFrame, text="Components", font=("Arial", 14, "bold"), height=35, width=180,
                                        command=lambda: self.show_frame(self.components_frame))
        btn_components.place(x=10, y=140)

        # Register Vehicle
        btn_components = cttk.CTkButton(SideMenuFrame, text="Register", font=("Arial", 14, "bold"), height=35, width=180, command=self.registerVehicle)
        btn_components.place(x=10, y=180)

        # Logout
        btn_logout = cttk.CTkButton(SideMenuFrame, text="Logout", font=("Arial", 14, "bold"), command=self.logout,
                                    height=35, corner_radius=20)
        btn_logout.place(x=10, y=285)


        # -----------------------------Registration--------------------------------------------
        # Labels
        lbl_vehicle_name = cttk.CTkLabel(self.settings_frame, text="Vehicle Name:")
        lbl_vehicle_no = cttk.CTkLabel(self.settings_frame, text="Vehicle Number:")
        lbl_vehicle_owner = cttk.CTkLabel(self.settings_frame, text="Vehicle Owner:")
        lbl_owner_contact = cttk.CTkLabel(self.settings_frame, text="Owner Contact:")
        lbl_rfid_tag = cttk.CTkLabel(self.settings_frame, text="RFID Tag:")

        # Entry widgets
        self.entry_vehicle_name = cttk.CTkEntry(self.settings_frame)
        self.entry_vehicle_no = cttk.CTkEntry(self.settings_frame)
        self.entry_vehicle_owner = cttk.CTkEntry(self.settings_frame)
        self.entry_owner_contact = cttk.CTkEntry(self.settings_frame)
        self.entry_rfid_tag = cttk.CTkEntry(self.settings_frame, state='readonly')  # readonly for displaying RFID tag ID

        # Simulated RFID Scanning Button
        btn_scan_rfid = cttk.CTkButton(self.settings_frame, text="Scan RFID", command=self.scan_rfid)

        # Register Button
        btn_register = cttk.CTkButton(self.settings_frame, text="Register", command=self.register_vehicle)

        # Layout 
        lbl_vehicle_name.place(x=50,y=100)
        lbl_vehicle_no.place(x=50,y=140)
        lbl_vehicle_owner.place(x=50,y=180)
        lbl_owner_contact.place(x=50,y=220)
        lbl_rfid_tag.place(x=50,y=260)

        self.entry_vehicle_name.place(x=150,y=100)
        self.entry_vehicle_no.place(x=150,y=140)
        self.entry_vehicle_owner.place(x=150,y=180)
        self.entry_owner_contact.place(x=150,y=220)
        self.entry_rfid_tag.place(x=150,y=260)


        # Scanned RFID Tag ID Label
        lbl_scanned_rfid_tag = cttk.CTkLabel(self.settings_frame, text="Scanned RFID Tag:")
        self.lbl_scanned_rfid_tag_id = cttk.CTkLabel(self.settings_frame, text="", font=("Arial", 12, "bold"))

        lbl_scanned_rfid_tag.place(x=50,y=300)
        self.lbl_scanned_rfid_tag_id.place(x=150,y=300)


        btn_scan_rfid.place(x=50,y=360)
        btn_register.place(x=200,y=360)
    #---------------------------------------------------------------------------------------


    
    

    def show_frame(self, frame=None):
        if frame:
            # Stop RFID scanning when switching to the settings frame
            if frame == self.settings_frame:
                self.stop_rfid_scan_thread()

            # if frame == self.dashboard_frame:
            #     self.rfid_scan_background() 

            # Hide the current frame
            self.current_frame.place_forget()

            # Update the current frame to the selected frame
            self.current_frame = frame

            

        # Show the selected frame
        self.current_frame.place(x=280, y=50)
        # Update the total number of vehicles when switching to the dashboard frame
        if frame == self.dashboard_frame:
            self.update_total_vehicles_label()




    def scan_rfid(self):
        try:
                self.arduino = serial.Serial('COM5', 9600)
        except Exception as e:
                messagebox.showerror("Error", f"Failed to connect on COM5: {str(e)}")
                print(f"Failed to connect on COM5: {str(e)}")
                return

        try:
            print("Reading: ")
            data = self.arduino.readline().decode().strip()
            if data.startswith("Card detected:"):
                card_id = data[len("Card detected:"):].strip().replace(" ", "")
                self.entry_rfid_tag.configure(state='normal')
                self.entry_rfid_tag.delete(0, tk.END)
                self.entry_rfid_tag.insert(0, card_id)
                self.entry_rfid_tag.configure(state='readonly')
                self.lbl_scanned_rfid_tag_id.configure(text=f"ID: {card_id}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to scan RFID: {str(e)}")
            print(f"Error:  {str(e)}")

    def register_vehicle(self):
        vehicle_name = self.entry_vehicle_name.get()
        vehicle_no = self.entry_vehicle_no.get()
        vehicle_owner = self.entry_vehicle_owner.get()
        owner_contact = self.entry_owner_contact.get()
        rfid_tag = self.entry_rfid_tag.get()

        try:
            with self.db_conn.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO regvehicle (VehicleName, VehicleNo, VehicleOwner, OwnerContact, Tag_id) "
                    "VALUES (%s, %s, %s, %s, %s)",
                    (vehicle_name, vehicle_no, vehicle_owner, owner_contact, rfid_tag)
                )
                self.db_conn.commit()

                messagebox.showinfo("Success", "Vehicle registration successful.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to register vehicle: {str(e)}")

        finally:
            # Close the serial connection to release the port
            if self.arduino:
                self.arduino.close()

    


    def rfid_scan_background(self):
        try:
            self.arduino = serial.Serial('COM5', 9600)
        except Exception as e:
            print(f"Failed to connect on COM5: {str(e)}")

        while self.rfid_scan_flag:
            try:
                print("Reading: ")
                data = self.arduino.readline().decode().strip()
                if data.startswith("Card detected:"):
                    card_id = data[len("Card detected:"):].strip().replace(" ", "")

                    # Check if the card ID is registered in the database
                    with self.db_conn.cursor() as cursor:
                        cursor.execute("SELECT * FROM regvehicle WHERE Tag_id = %s", (card_id,))
                        result = cursor.fetchone()

                    if result:
                        # Card ID is registered, record attendance
                        with self.db_conn.cursor() as cursor:
                            cursor.execute(
                                "INSERT INTO vehicledetails (Tag_id, Entry_Time) VALUES (%s, NOW())",
                                (card_id,)
                            )
                            self.db_conn.commit()
                            print(f"Entry recorded for card ID: {card_id}")
                    else:
                        print("Need To Register card")

            except Exception as e:
                print(f"Error processing data: {str(e)}")

            # Add a small delay to avoid high CPU usage in the loop
            time.sleep(0.1)

    
    def stop_rfid_scan_thread(self):
        # Set the flag to stop the RFID scanning thread
        self.rfid_scan_flag = False

        # Wait for the thread to finish before continuing
        if self.rfid_thread.is_alive():
            self.rfid_thread.join()
        
        # Close the serial connection if it's open
        if self.arduino and self.arduino.is_open:
            self.arduino.close()
    
    def on_system_button_click(self):
        # Add logic for handling the system button click
        # For example, stop the RFID scanning thread
        self.stop_rfid_scan_thread()
    

    def update_total_vehicles_label(self):
        try:
            with self.db_conn.cursor() as cursor:
                # Perform a query to get the total number of vehicles
                cursor.execute("SELECT COUNT(*) FROM vehicledetails")
                result = cursor.fetchone()
                total_vehicles = result[0] if result else 0
                print(total_vehicles)

                # Update the label
                self.lbl_noOfVehicleEntered.configure(text=f"Total Vehicles: {total_vehicles}")

                # Update the vehicle list information
                self.update_vehicle_list()

        except Exception as e:
            print(f"Error updating total vehicles label: {str(e)}")

        

    # Function to update vehicle list information
    def update_vehicle_list(self):
        try:
            with self.db_conn.cursor() as cursor:
                # Perform a query to get vehicle information
                cursor.execute("SELECT Tag_id, Entry_Time FROM vehicledetails")
                results = cursor.fetchall()

                # Clear existing items in the treeview
                for item in self.treeview.get_children():
                    self.treeview.delete(item)

                # Insert new data into the treeview
                for row in results:
                    self.treeview.insert("", "end", values=row)

        except Exception as e:
            print(f"Error updating vehicle list: {str(e)}")


    
    

    def registerVehicle(self):
        self.root.destroy()
        #  import LoginPage
        os.system("python RegisterVehicle.py") #better to use this

    
    def stop_system(self):
        # Set the flag to stop the RFID scanning thread
        self.rfid_scan_flag = False

        # Wait for the thread to finish before continuing
        if self.rfid_thread.is_alive():
            self.rfid_thread.join()

        # Close the serial connection if it's open
        if self.arduino and self.arduino.is_open:
            self.arduino.close()
    


    def logout(self):
        # Stop the system and clean up resources
        self.stop_system()

        self.root.destroy()
        #  import LoginPage
        os.system("python LoginPage2.py") #better to use this
        print("logout")


