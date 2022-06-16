#include <Servo.h>

Servo servoMotor;

int motor1pin1 = 2;
int motor1pin2 = 3;
int ENA_pin = 4;
bool val = true;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(motor1pin1, OUTPUT);
  pinMode(motor1pin2, OUTPUT);
  pinMode(ENA_pin, OUTPUT); 

  servoMotor.attach(5);

}

void loop() {
  // hacer rodar la plataforma
      
  
  //Serial.println("hola");
  if(Serial.available()>0){
      char option = Serial.read();
      if (option == '1'){
          analogWrite(ENA_pin, 100); // de 100 a 250
          digitalWrite(motor1pin1, HIGH);
          digitalWrite(motor1pin2, LOW);
        }else if(option == '0'){
            //analogWrite(ENA_pin, 100); // de 100 a 250
            digitalWrite(motor1pin1, LOW);
            digitalWrite(motor1pin2, LOW);
          }else if(option == '2'){
            servoMotor.write(0);
            }else if(option == '3'){
               servoMotor.write(180);
              }
  }
  
}
