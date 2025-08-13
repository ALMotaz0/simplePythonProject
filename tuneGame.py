import tkinter as tk
import random
    
class TuneGame :
    def __init__(self, root):
        self.root = root
        self.root.geometry('300x400')
        self.root.title('GuessTheTuneGame')
        self.buttonColor = ['red','yellow','green','blue']
        self.counter =  0
        self.botChoice = []
        self.userChoice = []

        self.label = tk.Label(text="Click start to begin")
        self.label.pack(pady=10)

        for i in self.buttonColor :
            self.btn = tk.Button(self.root, text=i, bg=i, width=25, height=2, command=lambda c = i : self.colorPressed(c))
            self.btn.pack(pady=3)

        self.startBtn = tk.Button(self.root, text='start game', width=10, height=2, command = self.startGame)
        self.startBtn.pack()

    def colorPressed(self, c) :
        self.userChoice.append(c)

        self.counter = self.counter + 1

        if self.counter == 3 :
            if self.botChoice == self.userChoice :
                print('You entered the correct sequence.')
            else :
                print('Wrong input!')

            self.botChoice = []
            self.userChoice = []
            self.counter = 0
            
            self.startGame()
    
    def startGame(self) :
        for j in range(3) :
            self.botChoice.append(random.choice(self.buttonColor))

        print('>>> Sequence to remember: ',self.botChoice)
        

root = tk.Tk()
game = TuneGame(root)
root.mainloop()