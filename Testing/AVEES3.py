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

# Function to trigger the buzzer
def trigger_buzzer():
    arduino.write(b'B')  # Sending 'B' to trigger the buzzer signal in Arduino

#Function to move servo motor
def move_servo():
    arduino.write(b'S')  # Sending 'S' to trigger servo movement
    print("Registered vehicle found. Triggering servo motor.")


while True:
    try:
        print("Reading: ")
        data = arduino.readline().decode().strip()
        if data.startswith("Card detected:"):
            card_id = data[len("Card detected:"):].strip().replace(" ", "")

            # Check if the card ID is registered in the database
            with db_conn.cursor() as cursor:
                cursor.execute("SELECT * FROM regvehicle WHERE Tag_id = %s", (card_id,))
                result = cursor.fetchone()
                print(result)
                # print(result[6])


            if result:
                status = result[6]
                if status == "stolen":
                    #Trigger the buzzer
                    trigger_buzzer()
                    print("WARNING: This RFID tag is marked as stolen!")
                else: 
                    # Card ID is registered, record attendance
                    with db_conn.cursor() as cursor:
                        cursor.execute(
                            "INSERT INTO vehicledetails (Tag_id, Entry_Time) VALUES (%s, NOW())",
                            (card_id,)
                        )
                        db_conn.commit()
                        print(f"Entry recorded for card ID: {card_id}")
                    move_servo()
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
