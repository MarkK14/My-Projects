﻿/*
 * Arduino Programming Assignment#1
 * Objective is to Blink 1 LED in a specific flashing routine.
 * Written by KHAIRALLAH
 * Created 4/19/2022
 * Version 1.0
 * use an ATMEGA 328P
 * use digital pin 11
 */
 byte Led=11; //declaring pin
 int x;       //Throw away variable
byte between=250;//delay between flashes
byte letter=1500;//delay between letters


 void setup()
 {
  pinMode(Led,OUTPUT); //Sets pin 11 to output
 }
 
void loop()
{
  for(x=1;x<=5;x++)//flashes the LED 5 times
  {
    dot();
  }
  delay (3000); //3.00 second delay
  dot();//Letter "A"
  dash();
  delay(letter);//delay between each letter of 1.5 seconds
  dot();//Letter"S"
  dot();
  dot();
  delay(letter);
  dash();//Letter"T"
  delay(letter);
  dot();//Letter"R"
  dash();
  dot();
  delay(letter);
  dash();//Letter"O"
  dash();
  dash();
  delay(letter);
  dash();//Letter"N"
  dot();
  delay(letter);
  dash();//Letter"O"
  dash();
  dash();
  delay(letter);
  dash();//Letter"M"
  dash();
  delay(letter);
  dash();//Letter"Y"
  dot();
  dash();
  dash();
  delay(5000);
   for(x=1;x<=5;x++)//flashes the LED 5 times
  {
    dot();
  }
  delay(10000);//final 10.0 second delay
}


void dot()
{
 digitalWrite (Led,HIGH);//LED On
 delay(between);//Hold for 1/4 of a second
 digitalWrite (Led,LOW);//LED Off
 delay(between); //Delay between dots or dashes of 1/4 seconds
}
void dash()
{
 digitalWrite (Led,HIGH); //LED On
 delay(750);//Hold for 3/4 of a second
 digitalWrite (Led,LOW);//LED Off
 delay(between);//Delay between dots or dashes of 1/4 seconds
}