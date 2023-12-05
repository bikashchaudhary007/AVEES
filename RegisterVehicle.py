import tkinter as tk
from tkinter import messagebox
import mysql.connector
import serial

class VehicleRegistrationGUI:
    def __init__(self, root, arduino):
        self.root = root
        self.root.title("Vehicle Registration")
        self.root.geometry("400x350")

        # Connect to MySQL database
        self.db_conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",  # Replace with your MySQL password
            database="aveesdb"
        )

        self.arduino = arduino  # Serial object for RFID communication

        self.create_widgets()

    def create_widgets(self):
        # Labels
        lbl_vehicle_name = tk.Label(self.root, text="Vehicle Name:")
        lbl_vehicle_no = tk.Label(self.root, text="Vehicle Number:")
        lbl_vehicle_owner = tk.Label(self.root, text="Vehicle Owner:")
        lbl_owner_contact = tk.Label(self.root, text="Owner Contact:")
        lbl_rfid_tag = tk.Label(self.root, text="RFID Tag:")

        # Entry widgets
        self.entry_vehicle_name = tk.Entry(self.root)
        self.entry_vehicle_no = tk.Entry(self.root)
        self.entry_vehicle_owner = tk.Entry(self.root)
        self.entry_owner_contact = tk.Entry(self.root)
        self.entry_rfid_tag = tk.Entry(self.root, state='readonly')  # readonly for displaying RFID tag ID

        # Scanned RFID Tag ID Label
        lbl_scanned_rfid_tag = tk.Label(self.root, text="Scanned RFID Tag:")
        self.lbl_scanned_rfid_tag_id = tk.Label(self.root, text="", font=("Arial", 12, "bold"))

        # Simulated RFID Scanning Button
        btn_scan_rfid = tk.Button(self.root, text="Scan RFID", command=self.scan_rfid)

        # Register Button
        btn_register = tk.Button(self.root, text="Register", command=self.register_vehicle)

        # Layout using grid
        lbl_vehicle_name.grid(row=0, column=0, pady=5, padx=10, sticky="w")
        lbl_vehicle_no.grid(row=1, column=0, pady=5, padx=10, sticky="w")
        lbl_vehicle_owner.grid(row=2, column=0, pady=5, padx=10, sticky="w")
        lbl_owner_contact.grid(row=3, column=0, pady=5, padx=10, sticky="w")
        lbl_rfid_tag.grid(row=4, column=0, pady=5, padx=10, sticky="w")

        self.entry_vehicle_name.grid(row=0, column=1, pady=5, padx=10)
        self.entry_vehicle_no.grid(row=1, column=1, pady=5, padx=10)
        self.entry_vehicle_owner.grid(row=2, column=1, pady=5, padx=10)
        self.entry_owner_contact.grid(row=3, column=1, pady=5, padx=10)
        self.entry_rfid_tag.grid(row=4, column=1, pady=5, padx=10)

        lbl_scanned_rfid_tag.grid(row=5, column=0, pady=5, padx=10, sticky="w")
        self.lbl_scanned_rfid_tag_id.grid(row=5, column=1, pady=5, padx=10, sticky="w")

        btn_scan_rfid.grid(row=6, column=0, columnspan=2, pady=5)
        btn_register.grid(row=7, column=0, columnspan=2, pady=10)

    def scan_rfid(self):
        try:
            data = self.arduino.readline().decode().strip()
            if data.startswith("Card detected:"):
                card_id = data[len("Card detected:"):].strip().replace(" ", "")
                self.entry_rfid_tag.config(state='normal')
                self.entry_rfid_tag.delete(0, tk.END)
                self.entry_rfid_tag.insert(0, card_id)
                self.entry_rfid_tag.config(state='readonly')
                self.lbl_scanned_rfid_tag_id.config(text=f"ID: {card_id}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to scan RFID: {str(e)}")

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

if __name__ == "__main__":
    serial_port = 'COM5'
    try:
        arduino = serial.Serial(serial_port, 9600)
    except Exception as e:
        print(f"Failed to connect on {serial_port}: {str(e)}")
        exit()

    root = tk.Tk()
    app = VehicleRegistrationGUI(root, arduino)
    root.mainloop()
