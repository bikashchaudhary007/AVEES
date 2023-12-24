#include <SPI.h>
#include <MFRC522.h>

#define SS_PIN 10
#define RST_PIN 9
#define BUZZER_PIN 7 // Define the pin where the buzzer is connected

MFRC522 rfid(SS_PIN, RST_PIN);

void setup() {
  pinMode(BUZZER_PIN, OUTPUT);
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
