from tkinter import *


class FlashCardUI(Tk):
    def __init__(self):
        super().__init__()
        self.title("Flash Card")
        self.config(bg="#B1DDc6", padx=20, pady=20)

        self.canvas = Canvas(self, width=600, height=400, bg="white")
        self.canvas.grid(row=0, column=0, columnspan=3)

        


        
        self.btn_known = Button(self, text="Correct", width=12, height=2, bg="green", fg="white", font=("Courier", 15 ,"bold"))
        self.btn_unknown = Button(self, text="Incorrect", width=12, height=2, bg="red", fg="white", font=("Courier", 15 ,"bold"))

        self.btn_known.grid(column=0, row=1, pady=10)
        self.btn_unknown.grid(column=2, row=1, pady=10)

        # self.btn_known.pack(side="left", padx=50, pady=20)
        # self.btn_unknown.pack(side="right", padx=50, pady=20)

