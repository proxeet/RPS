from tkinter import *
import PIL
from PIL import Image
from PIL import ImageTk
from random import randint

root = Tk()
root.title("Rock&Scissors%Paper")
root.configure(background="White")

rock_img = ImageTk.PhotoImage(Image.open("user.rock.png"))
paper_img = ImageTk.PhotoImage(Image.open("user.paper.png"))
scissors_img = ImageTk.PhotoImage(Image.open("user.scissors.png"))
rock_img_cpu = ImageTk.PhotoImage(Image.open("rock.png"))
paper_img_cpu = ImageTk.PhotoImage(Image.open("paper.png"))
scissors_img_cpu = ImageTk.PhotoImage(Image.open("scissors.png"))

userLabel = Label(root, image = rock_img)
cpuLabel = Label(root, image = rock_img_cpu)
userLabel.grid(row = 1, column = 4)
cpuLabel.grid(row = 1, column = 0)

playerScore = Label(root, text=0,font=100,bg="red")
cpuScore = Label(root, text=0,font=100,bg="red")
playerScore.grid(row=1, column=3)
cpuScore.grid(row=1, column=1)

userIndicator = Label(root, font=48,text="ME", bg="white", fg="black")
cpuIndicator = Label(root, font=48,text="CPU", bg="white", fg="black")
userIndicator.grid(row=0,column=3)
cpuIndicator.grid(row=0,column=1)

msg = Label(root, font = 50, bg="white", fg="black")
msg.grid(row=3, column=2)

def updateMsg(x):
      msg["text"]= x 

def updateuserScore():
      score = int(playerScore["text"])
      score += 1
      playerScore["text"] = str(score)
def updatescoreCpu():
      score = int(cpuScore["text"])
      score += 1
      cpuScore["text"] = str(score)

def checkWin(player, cpu):
      print(f"player:{player},cpu:{cpu}")
      if player == cpu:
            updateMsg("Draw!")
      elif player == "rock":
            if cpu == "paper":
                  updateMsg("Lose!")
                  updatescoreCpu()
            else:
                  updateMsg("Won!")
                  updateuserScore()
      elif player == "paper":
            if cpu    == "scissors":
                  updateMsg("Lose!")
                  updatescoreCpu()
            else:
                  updateMsg("Won!")
                  updateuserScore()
      elif player == "scissors":
            if cpu == "rock":
                  updateMsg("Lose!")
                  updatescoreCpu()
            else:
                  updateMsg("Won!")
                  updateuserScore()
      else:
            pass
      



options = ["rock" , "paper", "scissors"]
options[0]

def updateOptions(x):
       
      cpuOptions = options[randint(0, 2)]
      if cpuOptions == "rock":
        cpuLabel.configure(image=rock_img_cpu)
      elif cpuOptions == "paper":
        cpuLabel.configure(image=paper_img_cpu)  
      else:
        cpuLabel.configure(image=scissors_img_cpu)  
       
       
       
       
      if x == "rock":
                userLabel.configure(image=rock_img) 
      elif x == "paper":
                userLabel.configure(image=paper_img)
      else:
                userLabel.configure(image=scissors_img)
      checkWin(x,cpuOptions)


rock = Button(root,width=18,height=2,text="ROCK!",bg="#45458B", fg="black",command = lambda:updateOptions("rock")).grid(row=2,column=1)
paper = Button(root,width=18,height=2,text="PAPER!",bg="#EEEE3B", fg="black",command = lambda:updateOptions("paper")).grid(row=2,column=2)
scissors = Button(root,width=18,height=2,text="SCISSORS!",bg="red",fg="black",command = lambda:updateOptions("scissors")).grid(row=2,column=3)




root.mainloop()