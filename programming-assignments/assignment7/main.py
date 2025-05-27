/*
 * Advanced NightRider
 * Goal is to create a LED chaser with a tail of 2 LEDs
 * written by KHAIRALLAH
 * 5/24/2022
 */
 int x;//throwaway variable
 int y;//throwaway variable
 int Tail []
={0,0,0,3,5,6,9,10,11,0,0,0};//LED array


 void setup()
 {
  pinMode(3,OUTPUT);//setting my 6 LEDs as outputs
  pinMode(5,OUTPUT);
  pinMode(6,OUTPUT);
  pinMode(9,OUTPUT);
  pinMode(10,OUTPUT);
  pinMode(11,OUTPUT);
 }
 void loop()
{
  for(x=3;x<=11;x++)// Start at index number 3 and finishes at 11
  {
  analogWrite(Tail[x],255);//turns on 3,4,5,6,7,8,9,10 then 11 (9,10 and 11 are all 0’s)
  analogWrite(Tail[x-1],125);// turns 2,3,4,5,6,7,8,9 then 10 half on (2,9 and 10 are all 0’s)
  analogWrite(Tail[x-2],50);// turns 1,2,3,4,5,6,7,8 then 9 quarter on (1,2 and 9 are all 0’s)
  analogWrite(Tail[x-3],0);//follows 3 LEDs behind the lead chaser and turns the LEDs off
  delay(90);
  }
   for(y=8;y>=0;y--)//Start at index number 8 and finishes at 0
  {
  analogWrite(Tail[y],255);//turns on 8,7,6,5,4,3,2,1 then 0 (2,1 and 0 are all 0’s)
  analogWrite(Tail[y+1],170);//turns on 9,8,7,6,5,4,3,2 then 1 half on (9,2 and 1 are all 0’s)
  analogWrite(Tail[y+2],100);//turns on 10,9,8,7,6,5,4,3 then 2 (10,9 and 2 are all 0’s)
  analogWrite(Tail[y+3],0);//follows 3 LEDs behind the lead chaser and turns the LEDs off
  delay(90);
  }
}