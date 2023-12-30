#include <SPI.h>
#include <MFRC522.h>
#include <Servo.h>

#define SS_PIN 10
#define RST_PIN 9
#define BUZZER_PIN 7 // Define the pin where the buzzer is connected
#define SERVO_PIN 6 // Define the pin where the servo signal wire is connected
#define BUTTON_PIN 2 // Define the pin where the push button is connected
int buttonState = 0;
int lastButtonState = 0;


Servo servo;

MFRC522 rfid(SS_PIN, RST_PIN);

void setup() {
  pinMode(BUZZER_PIN, OUTPUT);
  servo.attach(SERVO_PIN); // Attaching the servo to the specified pin
  pinMode(BUTTON_PIN, INPUT);
  servo.write(0);
  Serial.begin(9600);
  SPI.begin();
  rfid.PCD_Init();
}
  
void loop() {
  if (rfid.PICC_IsNewCardPresent() && rfid.PICC_ReadCardSerial()) {
    Serial.print("Card detected: ");

    for (byte i = 0; i < rfid.uid.size; i++) {
      Serial.print(rfid.uid.uidByte[i], HEX);
    }
    Serial.println();

    // Send the card data to the computer over the USB serial connection
    for (byte i = 0; i < rfid.uid.size; i++) {
      Serial.print(rfid.uid.uidByte[i], HEX);
    }
    Serial.println();
    
    // Add a delay to prevent reading the same card multiple times
    delay(2000);


    // Check for incoming data from Python
    if(Serial.available()>0){
      char receivedChar = Serial.read();
      if(receivedChar == 'B') {
        triggerBuzzer();
      }
      else if (receivedChar=='S'){
        moveServo();
      }
    }

  }

  // Read the state of the push button
  buttonState = digitalRead(BUTTON_PIN);
  if (buttonState == LOW && lastButtonState == HIGH){
    moveServo();
    // Print(buttonState);
  }

  lastButtonState = buttonState;

}

// Function to trigger the buzzer
void triggerBuzzer() {
  // Code to turn on the buzzer for a specific duration (e.g., 2 seconds)
  digitalWrite(BUZZER_PIN, HIGH);
  delay(2000); // Buzzer on for 2 seconds
  digitalWrite(BUZZER_PIN, LOW);
}


//Function to move the servo to 90 degree
void moveServo(){
  // Move the servo to 90 degrees

      servo.write(90); // Angle adjustment as needed
      delay(4000); // Delay for servo movement (adjust as needed)
      servo.write(0); // Move back to initial position (adjust as needed)
}
