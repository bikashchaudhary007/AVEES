#include <SPI.h>
#include <MFRC522.h>
#include <Servo.h>

#define SS_PIN 10
#define RST_PIN 9
#define BUZZER_PIN 7 // Define the pin where the buzzer is connected
#define SERVO_PIN 6 // Define the pin where the servo signal wire is connected

Servo servo;
int initialPos = 0; //inital position of servo
int targetPos = 90; //target position of servo

MFRC522 rfid(SS_PIN, RST_PIN);

void setup() {
  pinMode(BUZZER_PIN, OUTPUT);
  servo.attach(SERVO_PIN); // Attaching the servo to the specified pin
  servo.write(initialPos);
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

      else if (receivedChar=='E'){
        moveServo();
      }

    }


   
  }
}

// Function to trigger the buzzer
void triggerBuzzer() {
  // Code to turn on the buzzer for a specific duration (e.g., 2 seconds)
  digitalWrite(BUZZER_PIN, HIGH);
  delay(2000); // Buzzer on for 2 seconds
  digitalWrite(BUZZER_PIN, LOW);
}


//Function to move the servo to 90 degree
// void moveServo(){
//   // Move the servo to 90 degrees
//       servo.write(90); // Angle adjustment as needed
//       delay(4000); // Delay for servo movement (adjust as needed)
//       servo.write(0); // Move back to initial position (adjust as needed)
// }

void moveServo(){
  // Moving gradually the servo to 90 degrees
  for (int pos=0;pos<=90;pos += 1){
    servo.write(pos);
    delay(15);
  }

  delay(4000);
  servo.write(0);

}

// void moveServo(){
//   // Moving gradually the servo to 90 degrees
//   int currentPos = servo.read();
//   if(targetPos > currentPos){
//     for (int pos = currentPos; pos <= targetPos; pos +=1){
//       servo.write(pos);
//       delay(15);
//     }

//   }
//   else {
//     for(int pos = targetPos; pos >= 0; pos -=1){
//       servo.write(pos);
//       delay(15);
//     }
//   }
  

// }



