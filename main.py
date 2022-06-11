
import random

l = ["scissor","paper","rock"]

d = {1:"scissor",2:"paper",3:"rock"}

target = int(input("For how much games do you want to play game:"))

cha,rob =0,0
while target>0:
  print("charan : ",cha," robot : ",rob)
  robot = random.choice(l)
  charan = int(input("1.scissor 2.paper 3.rock:"))
  if(charan<=0 or charan>3):
    print("Incorrect input")
  else:
    if((d[charan]=="scissor" and robot=="paper") or (d[charan]=="rock" and robot=="scissor") or (d[charan]=="paper" and robot=="rock")):
      cha+=1
    elif((d[charan]=="paper" and robot=="scissor") or (d[charan]=="scissor" and robot=="rock") or (d[charan]=="rock" and robot=="paper")):
      rob+=1
    else:
      pass
    print("charan = ",d[charan]," robot = ",robot)
  target-=1
if cha==rob:
  print("charan = ",cha," robot = ",rob)
  print("Match tie..:)")
elif cha>rob:
  print("charan = ",cha," robot = ",rob)
  print("charan won")
else:
  print("charan = ",cha," robot = ",rob)
  print("robot win")
      

  
