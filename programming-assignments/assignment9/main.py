﻿void forward ()
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