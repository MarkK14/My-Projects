/*
 * Knight Rider
 * Flash a series of 6 LEDs in a back and forth formation
 * Written by KHAIRALLAH
 * 4/26/2022
 * Version 1.0
 * use an Atmega 328P chip
 * use Digital pins 8, 9, 10, 11, 12 and 13
 */


int x; // Throw away variable
int hold=75;// delay time


void setup()
{
 pinMode (13,OUTPUT); //making digital pins 8 through 13 output pins
 pinMode (12,OUTPUT);
 pinMode (11,OUTPUT);
 pinMode (10,OUTPUT);
 pinMode (9,OUTPUT);
 pinMode (8,OUTPUT);[a]
}


void loop()
{
 back();
 forth();[b]
}




void back()
{
  for(x=8;x<13;x++)//make x equal to 8 then add 1 each time till 12.
  {
    digitalWrite (x,HIGH);// whatever the value of x is, is the pin that will be On (8, 9, 10, 11, 12)
    delay (hold); //keep it on for 75ms
    digitalWrite (x,LOW); // turn it off
  }
}


void forth()
{
   for(x=13;x>8;x--)//make x equal to 13 then subtract 1 each time till 9.
  {
    digitalWrite (x,HIGH);//whatever the value of x is, is the pin that will be On (13, 12 11, 10, 9)
    delay (hold);//keep it on for 75ms
    digitalWrite (x,LOW);// turn it off
  }
}
[a]looping this would be more efficient
[b]why are you creating unnecessary functions ?