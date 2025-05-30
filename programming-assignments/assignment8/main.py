﻿byte WL1 = 7; //Wheel Left input 1
byte WL2 = 8; //Wheel Left input 2
byte WR1 = 9; //Wheel Rightinput 1
byte WR2 = 10; //Wheel Left input 1
int ftime = 10000; //delay time for forward movement
int rtime = 5000; //delay time for reverse movement
int Dturntime = 5000; //delay time to designate the angle of the turn
int Tturntime = 5000; //delay time to designate the angle of the turn


void setup()
{
  pinMode (WL1, OUTPUT); //setting the digital pin connected to the first input on the left wheel as an output
  pinMode (WL2, OUTPUT); //setting the digital pin connected to the second input on the left wheel as an output
  pinMode (WR1, OUTPUT); //setting the digital pin connected to the first input on the right wheel as an output
  pinMode (WR2, OUTPUT); //setting the digital pin connected to the second input on the right wheel as an output
}


void loop()
{
  delay(3000);
  digitalWrite(WL1, HIGH);
  digitalWrite(WL2, LOW);
  digitalWrite(WR1, LOW);
  digitalWrite(WR2, HIGH);
  delay(11500);
  digitalWrite(WL1, LOW);
  digitalWrite(WL2, LOW);
  digitalWrite(WR1, LOW);
  digitalWrite(WR2, HIGH);
  delay(1900);
  digitalWrite(WL1, HIGH);
  digitalWrite(WL2, LOW);
  digitalWrite(WR1, LOW);
  digitalWrite(WR2, HIGH);
  delay(11000);
  digitalWrite(WR1, HIGH);
  digitalWrite(WL2, LOW);
  digitalWrite(WL1, HIGH);
  digitalWrite(WR2, LOW);
  delay(1050);
  digitalWrite(WL1, HIGH);
  digitalWrite(WL2, LOW);
  digitalWrite(WR1, LOW);
  digitalWrite(WR2, HIGH);
  delay(17000);
  digitalWrite(WR1, HIGH);
    digitalWrite(WR2, LOW);
  digitalWrite(WL1, HIGH);
    digitalWrite(WL2, LOW);
  delay(1200);
    digitalWrite(WL1, HIGH);
  digitalWrite(WL2, LOW);
  digitalWrite(WR1, LOW);
  digitalWrite(WR2, HIGH);
  delay(11500);
}


void forward ()
{
  digitalWrite(WL2, HIGH); //send 5V to input 2 of the left wheel (turns anti-clockwise)
  digitalWrite(WR1, HIGH); //send 5V to input 1 of the left wheel (turns clockwise)
  delay(ftime);//keep doing this for 5 seconds
}
void reverse ()
{
  digitalWrite(WL1, HIGH); //send 5V to input 1 of the left wheel (turns clockwise)
  digitalWrite(WR2, HIGH); //send 5V to input 2 of the left wheel (turns anti-clockwise)
  delay(rtime);//keep doing this for 5 seconds
}
void TturnR()
{
  digitalWrite(WR1, HIGH);
  digitalWrite(WL1, HIGH);
  delay(Tturntime);


}
void TturnL()
{
  digitalWrite(WL2, HIGH);
  digitalWrite(WR2, HIGH);
  delay(Tturntime);
}
void DturnR()
{
  digitalWrite(WR1, HIGH);
  delay(Dturntime);
}
void DturnL ()
{
  digitalWrite(WR2, HIGH);
  delay(Dturntime);
}
void halt()
{
  digitalWrite(WL1, LOW);
  digitalWrite(WL2, LOW);
  digitalWrite(WR1, LOW);
  digitalWrite(WR2, LOW);
  delay(2000);
}