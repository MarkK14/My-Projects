﻿/*
 *Project Moting Motor
 *Goal is to make 2 motors sound forward, and backward.
*Written by KHAIRALLAH
 *5/19/2022
 * use a L293D Motor controller
 */


byte WL1=7;//Wheel Left input 1
byte WL2=8;//Wheel Left input 2
byte WR1=9;//Wheel Rightinput 1
byte WR2=10;//Wheel Left input 1
int ftime=5000;//delay time for forward movement
int rtime=5000;//delay time for reverse movement


void setup()
{
  pinMode (WL1,OUTPUT);//setting the digital pin connected to the first input on the left wheel as an output
  pinMode (WL2,OUTPUT);//setting the digital pin connected to the second input on the left wheel as an output
  pinMode (WR1,OUTPUT);//setting the digital pin connected to the first input on the right wheel as an output
  pinMode (WR2,OUTPUT);//setting the digital pin connected to the second input on the right wheel as an output
}


void loop()
{
forward();//move forwards for 5 seconds
halt();//Complete stop and wait 5 seconds
reverse();//move backwards for 5 seconds
halt();//Complete stop and wait 5 seconds
}


void forward ()//causes both motors to work together to move forward
 {
  digitalWrite(WL2,HIGH);//send 5V to input 2 of the left wheel (turns anti-clockwise)
  digitalWrite(WR1,HIGH);//send 5V to input 1 of the left wheel (turns clockwise)
  delay(ftime);//keep doing this for 5 seconds
 }
void reverse ()//causes both motors to work together to move backwards
 {
  digitalWrite(WL1,HIGH);//send 5V to input 1 of the left wheel (turns clockwise)
  digitalWrite(WR2,HIGH);//send 5V to input 2 of the left wheel (turns anti-clockwise)
  delay(rtime);//keep doing this for 5 seconds
 }


void halt()//turns all the wheels off
{
  digitalWrite(WL1,LOW);//turn first input on the left wheel off
  digitalWrite(WL2,LOW);//turn second input on the left wheel off
  digitalWrite(WR1,LOW);//turn first input on the right wheel off
  digitalWrite(WR2,LOW);//turn second input on the right wheel off
  delay(5000);//stay off for 5 seconds
}