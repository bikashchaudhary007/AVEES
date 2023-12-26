import os
import customtkinter as cttk
import tkinter as tk
from tkinter import messagebox
import mysql.connector
import serial
import tkinter.ttk as ttk
import threading
import time
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from tkcalendar import DateEntry
from datetime import datetime, date



class Dashboard:
    def __init__(self, root, user):
        # serial_port = 'COM5'
        self.root = root
        self.root.title("Dashboard")
        self.root.geometry("1280x1080+50+0")
        # self.root.resizable(False, False)
        self.user = user
        self.arduino = None  # Initialize self.arduino to None
        self.db_conn = None  # Initialize db_conn to None
        self.lbl_noOfVehicleEntered =None
        self.lbl_noOfVehicleExit = None
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
        self.dashboard_frame = cttk.CTkScrollableFrame(root, width=850, height=650, fg_color=("white", "#4B49AC"))
        self.settings_frame = cttk.CTkFrame(root, width=850, height=450, fg_color=("white", "#4B49AC"))
        self.components_frame = cttk.CTkFrame(root, width=850, height=450, fg_color=("white", "#4B49AC"))

        # Initial frame to show is the dashboard frame
        self.current_frame = self.dashboard_frame
        self.show_frame()

        #-------------------Top Main Frame----------------------------------------------------
        self.top_main_frame = cttk.CTkFrame(self.dashboard_frame,height=60,fg_color=("#4B49AC", "white"))
        self.top_main_frame.pack(fill="x",padx=10,pady=10)

        # Displaying the username on the dashboard
        username_label = cttk.CTkLabel(self.top_main_frame, text=f"Welcome, {self.user}!", font=("Arial", 16, "bold"))
        username_label.pack(side='left',padx=10,pady=10)

        btn_profile = cttk.CTkButton(self.top_main_frame,text="Profile",font=("Arial", 16, "bold"))
        btn_profile.pack(side='right',padx=10,pady=10)

        #--------------x-----Top Main Frame-------x---------------------------------------------

        #--------------------------------Vechile Details Frame-----------------------------------------------------------
        self.vechile_count_detail_frame= cttk.CTkFrame(self.dashboard_frame,height=300,fg_color=("white", "#4B49AC"))
        self.vechile_count_detail_frame.pack(fill="x",padx=10,pady=10)
       

        # ----------------Dashboard Inside Widgets-----------------------------------
        #No of Vehicles Entered
        self.vehicle_entered_frame = cttk.CTkFrame(self.vechile_count_detail_frame, width=350, height=350,fg_color=("#4B49AC", "white"))
        # self.vehicle_entered_frame.place(x=30,y=50)
        self.vehicle_entered_frame.pack(side='left',padx=30,pady=30)

        # Corrected initialization of lbl_noOfVehicleEntered
        self.lbl_noOfVehicleEntered = cttk.CTkLabel(
            self.vehicle_entered_frame,
            text="Total Vehicles: 0",
            font=("Arial", 18, "bold"),
            fg_color=("#4B49AC", "white")
        )
        self.lbl_noOfVehicleEntered.pack(padx=40,pady=30,ipadx=20,ipady=14)

        # Initialize the total number of vehicles label
        self.update_total_vehicles_label()


        #No of Vehicles Exit
        self.vehicle_exit_frame = cttk.CTkFrame(self.vechile_count_detail_frame, width=350, height=350,fg_color=("#98BDFF", "white"))
        self.vehicle_exit_frame.pack(side='left',padx=100,pady=30)

        self.lbl_noOfVehicleExit = cttk.CTkLabel(
            self.vehicle_exit_frame,
            text="Total Vehicles Exit: 0",
            font=("Arial", 18, "bold"),
            fg_color=("#98BDFF", "white")
        )
        self.lbl_noOfVehicleExit.pack(padx=30,pady=30,ipadx=18,ipady=14)


        self.update_total_vehicles_exit_label()

        #----------------------x----------Vechile Details Frame----------x-------------------------------------------------


        # Vehicle List Frame
        self.vehicle_list_frame = cttk.CTkFrame(self.components_frame, width=600, height=250, fg_color=("red", "#4B49AC"))
        self.vehicle_list_frame.place(x=70, y=170)

        # Treeview to display vehicle list
        columns = ("Vehicle No", "Entry Time")
        self.treeview = ttk.Treeview(self.vehicle_list_frame, columns=columns, show="headings", selectmode="browse", height=15)
        self.treeview.place(x=10, y=10)


        
        # Configure column headings
        for col in columns:
            self.treeview.heading(col, text=col, anchor="center", command=lambda c=col: self.sort_treeview(c))
            self.treeview.column(col, width=150, anchor="center")
            # self.treeview.heading(col, text=col)
            # self.treeview.column(col, width=150, anchor="center")
               
        # Function to update vehicle list information
        self.update_vehicle_list()


        # # Initial frame to show is the dashboard frame
        # self.current_frame = self.dashboard_frame
        # self.show_frame()


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

        # # Register Vehicle
        # btn_components = cttk.CTkButton(SideMenuFrame, text="Register", font=("Arial", 14, "bold"), height=35, width=180, command=self.registerVehicle)
        # btn_components.place(x=10, y=180)

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
        

    #-------------Graphs-------------------------------------------
        
        style = ttk.Style()
        style.configure('TButton', font=('Arial', 12))


        # self.filter_frame = ttk.Frame(self.dashboard_frame,width=650, height=50)
        # self.filter_frame.pack(padx=10,pady=10)

        self.filter_frame = cttk.CTkFrame(self.dashboard_frame,width=650, height=50)
        self.filter_frame.pack(padx=10,pady=10)


        self.current_month_start, self.current_month_end = self.get_current_month_dates()

        self.entry_from_date = DateEntry(self.filter_frame, width=12, background='darkblue', foreground='white', borderwidth=2)
        self.entry_from_date.grid(row=0, column=1, padx=5, pady=5)
        self.entry_from_date.set_date(self.current_month_start.strftime('%m/%d/%y'))

        self.entry_to_date = DateEntry(self.filter_frame, width=12, background='darkblue', foreground='white', borderwidth=2)
        self.entry_to_date.grid(row=0, column=3, padx=5, pady=5)
        self.entry_to_date.set_date(self.current_month_end.strftime('%m/%d/%y'))

        self.label_from_date = ttk.Label(self.filter_frame, text='From Date:')
        self.label_from_date.grid(row=0, column=0, padx=5, pady=5)

        self.label_to_date = ttk.Label(self.filter_frame, text='To Date:')
        self.label_to_date.grid(row=0, column=2, padx=5, pady=5)

        self.graph_frame = ttk.Frame(self.dashboard_frame, width=650, height=450)
        # self.graph_frame.place(x=40,y=210)
        self.graph_frame.pack()
        

        self.plot_vehicle_count(self.current_month_start, self.current_month_end)

        self.entry_from_date.bind("<<DateEntrySelected>>", self.update_graph)
        self.entry_to_date.bind("<<DateEntrySelected>>", self.update_graph)


        #------------xx-Graphs---------------xx----------------------------

        #-------------------------PIE CHART--------------------------------------------------------------
        self.pie_filter_frame = ttk.Frame(self.dashboard_frame,width=650, height=50)
        self.pie_filter_frame.pack(padx=10, pady=10)

        self.pie_entry_from_date = DateEntry(self.pie_filter_frame, width=12, background='darkblue', foreground='white', borderwidth=2)
        self.pie_entry_from_date.grid(row=0, column=1, padx=5, pady=5)
        self.pie_entry_from_date.set_date(datetime.now().replace(day=1))  # Default start date (1st day of current month)

        self.pie_entry_to_date = DateEntry(self.pie_filter_frame, width=12, background='darkblue', foreground='white', borderwidth=2)
        self.pie_entry_to_date.grid(row=0, column=3, padx=5, pady=5)
        self.pie_entry_to_date.set_date(datetime.now())  # Default end date (current date)

        self.pie_label_from_date = ttk.Label(self.pie_filter_frame, text='From Date:')
        self.pie_label_from_date.grid(row=0, column=0, padx=5, pady=5)

        self.pie_label_to_date = ttk.Label(self.pie_filter_frame, text='To Date:')
        self.pie_label_to_date.grid(row=0, column=2, padx=5, pady=5)

        self.pie_chart_frame = ttk.Frame(self.dashboard_frame, width=650, height=650)
        self.pie_chart_frame.pack()

        self.pie_entry_from_date.bind("<<DateEntrySelected>>", self.update_pie_chart)
        self.pie_entry_to_date.bind("<<DateEntrySelected>>", self.update_pie_chart)

        # Initially, show pie chart for the current month
        self.update_pie_chart(None)

        #----------------xx---------PIE CHART------------------xx--------------------------------------------
    
        #----Graphs--------
    def get_current_month_dates(self):
        today = date.today()
        first_day = today.replace(day=1)
        last_day = today.replace(day=28)
        last_day = last_day.replace(day=max(min(31, last_day.day), 29))
        return first_day, last_day

    def plot_vehicle_count(self, from_date, to_date):
        from_date_str = from_date.strftime('%m/%d/%y')
        to_date_str = to_date.strftime('%m/%d/%y')

        from_date_formatted = from_date.strftime('%Y-%m-%d')
        to_date_formatted = to_date.strftime('%Y-%m-%d')

        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='aveesdb'
        )

        cursor = connection.cursor()

        query = "SELECT DATE_FORMAT(Entry_Time, '%Y-%m-%d') AS Entry_Date, COUNT(*) AS Vehicle_Count FROM vehicledetails WHERE Entry_Time BETWEEN %s AND %s GROUP BY Entry_Date"
        cursor.execute(query, (from_date_formatted, to_date_formatted))

        rows = cursor.fetchall()

        cursor.close()
        connection.close()

        x_data = [row[0] for row in rows]
        y_data = [row[1] for row in rows]

        # Clear previous plot data
        for widget in self.graph_frame.winfo_children():
            widget.destroy()
        
        # List of colors for bars
        bar_colors = ['#FF5733', '#C70039', '#900C3F', '#581845', '#FFC300', '#DAF7A6', '#FF5733', '#C70039', '#900C3F', '#581845']  # Example colors list

        # fig, ax = plt.subplots(figsize=(7, 4))
        # bars = ax.bar(x_data, y_data, color='skyblue')

        #Plotting the bar graph with custom colors
        fig, ax = plt.subplots(figsize=(7, 4))
        bars = ax.bar(x_data, y_data, color=bar_colors[:len(x_data)])  # Use colors list for bars

        ax.set_xlabel('Date', fontsize=12)
        ax.set_ylabel('Number of Vehicles', fontsize=12)
        ax.set_title('Number of Vehicles Entered on Different Days', fontsize=14)
        ax.set_xticklabels(x_data, rotation=0)

        ax.set_facecolor('white')

        # Change the color of the X and Y axis labels
        ax.xaxis.label.set_color('red')  # Change X axis label color
        ax.yaxis.label.set_color('blue')  # Change Y axis label color

        # Change the color of the X and Y axis ticks and tick labels
        ax.tick_params(axis='x', colors='green')  # Change X axis tick color
        ax.tick_params(axis='y', colors='orange')  # Change Y axis tick color

        # Change the color of the spines (borders)
        for spine in ax.spines.values():
            spine.set_edgecolor('green')  # Set the border color here

        for bar, count in zip(bars, y_data):
            ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), count,
                    ha='center', va='bottom', color='green', fontsize=10)

        canvas = FigureCanvasTkAgg(fig, master=self.graph_frame)
        canvas.draw()
        canvas.get_tk_widget().place(x=0,y=0)

        print("From Date:", from_date_formatted)
        print("To Date:", to_date_formatted)
        print("Query Executed Successfully")
        print("Rows Fetched:", rows)

    def update_graph(self, event):
        from_date = datetime.strptime(self.entry_from_date.get(), '%m/%d/%y')
        to_date = datetime.strptime(self.entry_to_date.get(), '%m/%d/%y')
        self.plot_vehicle_count(from_date, to_date)
        #-----------x--------Graphs--------------------------------------


    

        
    #-------------------------PIE CHART #--------------------------------------------------------------
    def fetch_data_from_db(self, from_date, to_date):
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',  # Enter your MySQL password here
            database='aveesdb'
        )

        cursor = connection.cursor()

        query = "SELECT DATE_FORMAT(Entry_Time, '%Y-%m-%d') AS Entry_Date, COUNT(*) AS Vehicle_Count FROM vehicledetails WHERE Entry_Time BETWEEN %s AND %s GROUP BY Entry_Date"
        cursor.execute(query, (from_date, to_date))

        rows = cursor.fetchall()

        cursor.close()
        connection.close()

        return rows

    def update_pie_chart(self, event):
        from_date = self.pie_entry_from_date.get_date().strftime('%Y-%m-%d')  # Selected 'from' date
        to_date = self.pie_entry_to_date.get_date().strftime('%Y-%m-%d')  # Selected 'to' date

        rows = self.fetch_data_from_db(from_date, to_date)

        x_data = [row[0] for row in rows]
        y_data = [row[1] for row in rows]

        labels = x_data
        sizes = y_data

        # Clear previous plot
        for widget in self.pie_chart_frame.winfo_children():
            widget.destroy()

        fig, ax = plt.subplots(figsize=(6, 6))
        ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
        ax.axis('equal')

        ax.set_title('Vehicle Distribution Based on Dates')

        canvas = FigureCanvasTkAgg(fig, master=self.pie_chart_frame)
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        
        #-------------------x------PIE CHART-----------------------x---------------------------------------


    def show_frame(self, frame=None):
        if frame:
            # Stop RFID scanning when switching to the settings frame
            if frame == self.settings_frame:
                self.stop_rfid_scan_thread()

            # if frame == self.dashboard_frame:
            #     self.rfid_scan_background() 

            # Hide the current frame
            # self.current_frame.place_forget()
            self.current_frame.pack_forget()

            # Update the current frame to the selected frame
            self.current_frame = frame

            

        # Show the selected frame
        # self.current_frame.place(x=280, y=50)
        self.current_frame.pack(padx=230,pady=50)
        # Update the total number of vehicles when switching to the dashboard frame
        if frame == self.dashboard_frame:
            self.update_total_vehicles_label()
            self.update_total_vehicles_exit_label()

            # Refresh the treeview to apply the font changes
            self.treeview.update_idletasks()




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
        
        # Function to trigger the buzzer
        def trigger_buzzer():
            self.arduino.write(b'B')  # Sending 'B' to trigger the buzzer signal in Arduino

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
                        status = result[6] #Set Card Status

                        if status == "stolen":
                            #Trigger the buzzer
                            trigger_buzzer()
                            messagebox.showwarning(f"WARNING!!!",f"This RFID tag {card_id} \n is marked as stolen!")
                            print("WARNING: This RFID tag is marked as stolen!")
                        else: 
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
                # cursor.execute("SELECT COUNT(*) FROM vehicledetails")
                cursor.execute('''SELECT COUNT(*) AS OddRowCount FROM (
                                SELECT (@row_number:=@row_number + 1) AS row_num
                                FROM vehicledetails, (SELECT @row_number:=0) AS t
                            ) AS numbered_rows
                            WHERE row_num % 2 != 0''')
                result = cursor.fetchone()
                total_vehicles = result[0] if result else 0
                print(total_vehicles)

                # Update the label
                self.lbl_noOfVehicleEntered.configure(text=f"Total Vehicles: \n {total_vehicles}")

                # Update the vehicle list information
                self.update_vehicle_list()

        except Exception as e:
            print(f"Error updating total vehicles label: {str(e)}")
    
    #Exit Vehicles
    def update_total_vehicles_exit_label(self):
        try:
            with self.db_conn.cursor() as cursor:
                # Perform a query to get the total number of vehicles
                # cursor.execute("SELECT COUNT(*) FROM vehicledetails")
                cursor.execute('''SELECT COUNT(*) AS OddRowCount FROM (
                                SELECT (@row_number:=@row_number + 1) AS row_num
                                FROM vehicledetails, (SELECT @row_number:=0) AS t
                            ) AS numbered_rows
                            WHERE row_num % 2 = 0''')
                result = cursor.fetchone()
                total_vehicles = result[0] if result else 0
                print(total_vehicles)

                # Update the label
                self.lbl_noOfVehicleExit.configure(text=f"Total Vehicles Exit:\n {total_vehicles}")

                # Update the vehicle list information
                self.update_vehicle_list()

        except Exception as e:
            print(f"Error updating total vehicles label: {str(e)}")

        

    # Function to update vehicle list information
    def update_vehicle_list(self):
        try:
            with self.db_conn.cursor() as cursor:
                # Perform a query to get vehicle information
                cursor.execute("SELECT Tag_id, Entry_Time FROM vehicledetails order by Id DESC LIMIT 10")
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

