byte WL1 = 7; //Wheel Left input 1
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
  delay(3000);//to give time for me to release robot
  digitalWrite(WL1, HIGH);//drive forward
  digitalWrite(WL2, LOW);
  digitalWrite(WR1, LOW);
  digitalWrite(WR2, HIGH);
  delay(10800);//for 10800 milliseconds
  digitalWrite(WL1, LOW);//drag turn left
  digitalWrite(WL2, LOW);
  digitalWrite(WR1, LOW);
  digitalWrite(WR2, HIGH);
  delay(2500);//for 2500 milliseconds
  digitalWrite(WL1, HIGH);//drive forwards
  digitalWrite(WL2, LOW);
  digitalWrite(WR1, LOW);
  digitalWrite(WR2, HIGH);
  delay(9200);//for 9200 milliseconds
  digitalWrite(WR1, LOW);//drag turn right
  digitalWrite(WL2, LOW);
  digitalWrite(WL1, HIGH);
  digitalWrite(WR2, LOW);
  delay(1300);//for 1300 milliseconds
  digitalWrite(WL1, HIGH);//drive forward
  digitalWrite(WL2, LOW);
  digitalWrite(WR1, LOW);
  digitalWrite(WR2, HIGH);
  delay(17500);//for 17500 milliseconds
  digitalWrite(WR1, LOW);//drag turn right
    digitalWrite(WR2, LOW);
  digitalWrite(WL1, HIGH);
    digitalWrite(WL2, LOW);
  delay(1100);//for 1100 milliseconds
    digitalWrite(WL1, HIGH);//drive forward
  digitalWrite(WL2, LOW);
  digitalWrite(WR1, LOW);
  digitalWrite(WR2, HIGH);
  delay(12000);//for 12000 milliseconds
  digitalWrite(WL1, LOW);//drag turn left
  digitalWrite(WL2, LOW);
  digitalWrite(WR1, LOW);
  digitalWrite(WR2, HIGH);
  delay(2300);//for 2300 milliseconds
    digitalWrite(WL1, HIGH);//drive forward
  digitalWrite(WL2, LOW);
  digitalWrite(WR1, LOW);
  digitalWrite(WR2, HIGH);
  delay(10500);//for 10500 milliseconds
}