from tkinter import *
import math
import winsound
from plyer import notification
import sys # Import the 'sys' module
import os  # Import the 'os' module

# --- FILE PATHS FIX ---
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# --- CONSTANTS ---
BROWN = "#674800"
GREEN = "#7ab000"
RED = "#8b0202"
PINK = "#ffe67d"
WHITE = "#ffffff"
FONT_NAME = "Courier"
WORK_MIN = 25
BREAK_MIN = 5
LONG_BREAK_MIN = 15

# --- GLOBAL VARIABLES ---
reps = 0
timer = None

# --- FUNCTIONS ---
def play_sound():
    winsound.Beep(1000, 500)

def reset_time():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")
    check_marks.config(text="")
    global reps
    reps = 0
    start_btn.config(state="normal")

def start_timer():
    global reps
    start_btn.config(state="disabled")
    reps += 1
    work_sec = WORK_MIN * 60
    break_sec = BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Long Break", fg=RED)
        notification.notify(title="Pomodoro", message="Work session over! Take a long break.")
    elif reps % 2 == 0:
        count_down(break_sec)
        title_label.config(text="Break", fg=BROWN)
        notification.notify(title="Pomodoro", message="Work session over! Take a break.")
    else:
        notification.notify(title="Pomodoro", message="Work session start!")
        count_down(work_sec)
        title_label.config(text="Work", fg=GREEN)

def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    canvas.itemconfig(timer_text, text=f"{count_min:02d}:{count_sec:02d}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        play_sound()
        start_timer()
        marks = ""
        work_sesions = math.floor(reps / 2)
        for _ in range(work_sesions):
            marks += "✅"
        check_marks.config(text=marks)

# --- UI SETUP ---
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=PINK)
window.resizable(False, False)

canvas = Canvas(width=256, height=256, bg=PINK, highlightthickness=0)
image_path = resource_path("pomodoro.png")
tomate_img = PhotoImage(file=image_path)
canvas.create_image(128, 128, image=tomate_img)
timer_text = canvas.create_text(128, 128, text="00:00", fill=WHITE, font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

title_label = Label(text="Timer", fg=GREEN, bg=PINK, font=(FONT_NAME, 35))
title_label.grid(column=1, row=0)

start_btn = Button(text="Start", highlightthickness=0, command=start_timer)
start_btn.grid(column=0, row=2)

reset_btn = Button(text="Reset", highlightthickness=0, command=reset_time)
reset_btn.grid(column=2, row=2)

check_marks = Label(text="", bg=PINK, fg=GREEN)
check_marks.grid(column=1, row=3)

window.mainloop()
