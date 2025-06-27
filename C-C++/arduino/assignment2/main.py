/*
 * Light button
 * Imitate the effect of a light switch with a button.
 * will be done by changing the state each time the button is pressed
 * Written by KHAIRALLAH
 * 4/28/20022
 * Version 1.0
 * use an Atmega328P
 * debounce your button
 */


 byte led=11; //declaring led pin
 byte button=9; // declaring button pin
 int x; //throw away variable
 byte y=0; //indicates the state of the light (on/1 or off/0)[a]
 
 void setup ()
 {
  pinMode(led,OUTPUT); //The LED will be receiving information from the chip
  pinMode(button,INPUT); // the Chip will be receiving info from the button
  Serial.begin(9600); // troubleshooting purposes (sets baud rate)
 }
 void loop()
 {
 x= digitalRead (button); // the variable x represents 
 Serial.println(y); //prints the value of y in a linear format
 if(x==1)//in other words: if the button is pressed.
 {
  y++; //"y" is now increased by 1
  delay (250); //delay in order to give time for user to release finger from button
 }
 if (y==1) //if this is the first time the button is pressed ("y" is originally equal to 0 so: 0+1=1) turn the LED on
 {
  digitalWrite (led,HIGH);
 }
 if (y!=1) //If this is the second time the button is pressed (meaning it was originally on since "y" is now equal to 1 so 1+1=2 and 2≠1) turn the LED off
 {
  digitalWrite (led,LOW);
  y=0; //reset the value of "y"
 }
 }
[a]Boolean