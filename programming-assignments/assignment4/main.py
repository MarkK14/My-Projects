﻿/*
 * Turn signal
 * goal is to make a set of 6 LEDs shine in patterns of 3 to indicate a left or light turn by shining outwards\
 * Written by KHAIRALLAH
 * 5/11/2022
 * use an Atmega328P
 */


 byte left1=8;//declaring LED pin
 byte left2=7;//declaring LED pin
 byte left3=6;//declaring LED pin
 byte right1=9;//declaring LED pin
 byte right2=10;//declaring LED pin
 byte right3=11;//declaring LED pin[a]
 byte buttonL=4;//declaring button pin
 byte buttonR=A0;//declaring button pin
 byte x;//throw-away variable for right button
 byte y;//throw-away variable for right button
 byte a;//throw-away variable for left button
 byte b;//throw-away variable for left button


 void setup()
 {
 pinMode (left1,OUTPUT);//setting digital pin 8 as an output pin (LED)
 pinMode (left2,OUTPUT);//setting digital pin 7 as an output pin (LED)
 pinMode (left3,OUTPUT);//setting digital pin 6 as an output pin (LED)
 pinMode (right1,OUTPUT);//setting digital pin 9 as an output pin (LED)
 pinMode (right2,OUTPUT);//setting digital pin 10 as an output pin (LED)
 pinMode (right3,OUTPUT);//setting digital pin 11 as an output pin (LED)[b]
 pinMode (buttonL,INPUT);//setting digital pin 4 as an input pin (button)
 pinMode (buttonR,INPUT);//setting analog pin 0 as an input pin (button)
 }


void loop()
{
 x=digitalRead(buttonR);//"x" is equal to the right button's state
 delay(50);//giving time for user to remove finger
if (x==1)//if right button is pressed
{
  for(y=9;y<=11;y++)//"y" will be equal to 9, 10 then 11
  {
digitalWrite(y,HIGH);//cause the pin number that "y" is one to turn on
delay(80); //keep the LED on
digitalWrite(y,LOW);//turn it off
  }
}


 a=digitalRead(buttonL);//"a"[c] is equal to the right button's state
 delay(50);//giving time for user to remove finger
if (a==1)//if left button is pressed
{
  for(b=8;b>=6;b--)//"b" will be equal to 8, 7 then 6
  {
digitalWrite(b,HIGH);//cause the pin number that "b" is one to turn on
delay(80);//keep the LED on
digitalWrite(b,LOW);//turn it off
  }
}
}




[a]since you don't use these in your program, they are a memory waste
[b]could be done with a loop
[c]Just a FYI, it has been found to be more efficient to do all the reading of the pins first and then do the logic.  Something to consider in future and simple information for you, no affect on your mark.  :)