/*
 * Arduino Programming Assignment #4
 * Adaptive Lighting
 * By the use of a photoresistor I plan to cause a LED to shine more brightly the darker and environment is and vice versa
 * Written by KHAIRALLAH
 * use an Atmega328P
 * use digital pin 9 and analog pin 1 
 * 5/6/2022
 * Version 1.0
 */


 int x;//throw away variable
 byte y=A1;//declaring my analog pin
 int light;//throw away variable made to represent the value of the brightness
 byte led=9;//declaring my digital pin


 void setup()
 {
  pinMode(y,INPUT);//setting up my analog pin as an input
  pinMode(led,OUTPUT);//setting up my digital pin as an output
  Serial.begin (9600);//setting up baud rate for my serial monitor
 }


 void loop()
 {
 x=analogRead(y);// "x" is equal to the resistance read from the photoresistor
   light= map(x,0,1023,255,0);//"light" is equal to the value of "x" taken from a range of 0-1023 to 255-0 (0 being 255 and 1023 being 0)
   Serial.println(light);//print the value of "light"
   analogWrite (led,light);//set the brightness of the LED to the value of "light"
 }