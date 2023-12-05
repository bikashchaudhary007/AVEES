import serial
import mysql.connector

serial_port = 'COM5'
db_conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",  # Replace with your MySQL password
    database="aveesdb"
)

try:
    arduino = serial.Serial(serial_port, 9600)
except Exception as e:
    print(f"Failed to connect on {serial_port}: {str(e)}")

while True:
    try:
        data = arduino.readline().decode().strip()
        if data.startswith("Card detected:"):
            card_id = data[len("Card detected:"):].strip().replace(" ", "")

            # Check if the card ID is registered in the database
            with db_conn.cursor() as cursor:
                cursor.execute("SELECT * FROM regvehicle WHERE Tag_id = %s", (card_id,))
                result = cursor.fetchone()

            if result:
                # Card ID is registered, record attendance
                with db_conn.cursor() as cursor:
                    cursor.execute(
                        "INSERT INTO vehicledetails (Tag_id, Entry_Time) VALUES (%s, NOW())",
                        (card_id,)
                    )
                    db_conn.commit()
                    print(f"Entry recorded for card ID: {card_id}")
            else:
                # Card ID not found, register it
                print(f"Card ID {card_id} is not registered.")
                # employee_name = input("Enter employee name: ")
                vehicleName = input("Enter vehicle name: ")
                vehicleNo = input("Enter vehicle number: ")
                vehicleOwner = input("Enter vehicle owner: ")
                ownerContact = input("Enter vehicle owner contact: ")
                if vehicleNo.strip():  # Check if the input is not empty
                    with db_conn.cursor() as cursor:
                        cursor.execute(
                            "INSERT INTO regvehicle (VehicleName, VehicleNo,VehicleOwner,OwnerContact,Tag_id) VALUES (%s, %s,%s, %s,%s)",
                            (vehicleName, vehicleNo,vehicleOwner,ownerContact,card_id)
                        )
                        db_conn.commit()
                        print(f"Registered RFID tag for vehicle: {vehicleOwner}")
    except Exception as e:
        print(f"Error processing data: {str(e)}")
