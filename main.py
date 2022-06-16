

from tkinter import *
from time import sleep

def create():
  root = Tk()
  root.geometry('1000x1000')  

class Question:
    def __init__(self, question, answers, correctLetter):
        self.question = question
        self.answers = answers
        self.correctLetter = correctLetter

    def check(self, letter, view):
        global right
        if(letter == self.correctLetter):
            label = Label(view, text="Good job nane!")
            right += 1
        else:
            label = Label(view, text="WRONG WRONG WRONG... IS CUNNANE REALLY BEHIND THE SCREEN?")
        label.pack()
        view.after(1000, lambda *args: self.unpackView(view))


    def getView(self, window):
        view = Frame(window)
        Label(view, text=self.question).pack()
        Button(view, text=self.answers[0], command=lambda *args: self.check("A", view)).pack()
        Button(view, text=self.answers[1], command=lambda *args: self.check("B", view)).pack()
        Button(view, text=self.answers[2], command=lambda *args: self.check("C", view)).pack()
        Button(view, text=self.answers[3], command=lambda *args: self.check("D", view)).pack()
        return view

    def unpackView(self, view):
        view.pack_forget()
        askQuestion()

def askQuestion():
    global questions, window, index, button, right, number_of_questions 
    if(len(questions) == index + 1):
        Label(window, text="YOU DID TERRIBLE NANE IS THAT REALLY YOU BEHIND THE SCREEN (you got " + str(right) + " of " + str(number_of_questions) + " questions answered right)").pack()
        windowSpam()
        return
    button.pack_forget()
    index += 1
    questions[index].getView(window).pack()

def windowSpam():
  for x in range(100):
      win = Tk()

      label = Label(win, text='YOU LOSE CUNNANE!', font=('Helvetica', 18, 'bold')) 
      label.pack()

questions = []
file = open("questions.txt", "r")
line = file.readline()
while(line != " "):
    questionString = line
    answers = []
    for i in range (4):
        answers.append(file.readline())

    correctLetter = file.readline()
    correctLetter = correctLetter[:-1]
    questions.append(Question(questionString, answers, correctLetter))
    line = file.readline()
file.close()
index = -1
right = 0
number_of_questions = len(questions)

window = Tk()
window.title("Cunnane Test")
button = Button(window, text="By pressing this button you consent to pass down all your belonginings to Mr Sarri Munem & Mr Ben Martin", command=askQuestion)
button.pack()
window.mainloop()
root.mainloop()
