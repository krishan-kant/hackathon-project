#include<Servo.h>

Servo myservo1;
Servo myservo2;
int change1=0;
int change2=0;
int final_angle=90;
int final_angle_y=90;
int bit1=1;
int bit2=1;
void setup() 
{
      myservo1.attach(6);
      myservo2.attach(9);
      Serial.begin(9600);
      Serial.println("Connection established...");
      myservo1.write(final_angle);
      myservo2.write(final_angle_y);
}

void loop() 
{ 
  while (Serial.available())
    {
           change1=0;change2=0;
           bit1=Serial.read();
           delay(5);
           bit2=Serial.read();
           delay(5);
           change1= Serial.read();//change can be both +ve or -ve
           delay(5);
           change2 = Serial.read();//change can be both +ve or -ve
          
           if(bit1==0)
            change1*=-1;
           if((final_angle+change1)>=0 && (final_angle+change1)<=180)
              final_angle+=change1;
           if(bit2==0)
            change2*=-1;
           if((final_angle_y+change2)>=0 && (final_angle_y+change2)<=180)
              final_angle_y+=change2;
           
           //Serial.println(final_angle);
           myservo1.write(final_angle);
           //Serial.println(final_angle_y);
           myservo2.write(final_angle_y);
           
           
    }
}

