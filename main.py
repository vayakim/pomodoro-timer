from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 


def reset_timer():
    global reps
    if reps != 0:
        reps = 0
        window.after_cancel(timer)
        check_mark.config(text="")
        title.config(text="Timer", fg=GREEN)
        canvas.itemconfig(timer_text, text="00:00")

# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():
    global reps
    if reps == 0:
        reps += 1
        work_sec = WORK_MIN * 60
        short_break_sec = SHORT_BREAK_MIN * 60
        long_break_sec = LONG_BREAK_MIN * 60
        if reps % 8 == 0:
            title.config(text="Break", fg=RED)
            count_down(long_break_sec)
        elif reps % 2 == 0:
            title.config(text="Break", fg=PINK)
            count_down(short_break_sec)
        else:
            title.config(text="Work", fg=GREEN)
            count_down(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count % 60

    if count_min < 10:
        count_min = f"0{count_min}"
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    elif reps < 8:
        start_timer()
        if reps % 2 == 0:
            work_sessions = math.floor(reps/2)
            check_mark.config(text="✔" * work_sessions)
    elif reps == 8:
        title.config(text="End")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro App")
window.config(padx=100, pady=50, bg=YELLOW)


canvas = Canvas(width=220, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(110, 112, image=tomato_img)
timer_text = canvas.create_text(110, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

title = Label(text="Timer")
title.config(font=(FONT_NAME, 50), fg=GREEN, bg=YELLOW)
title.grid(column=1, row=0)

start_button = Button(text="Start", command=start_timer)
start_button.grid(row=2, column=0)
start_button.config(highlightthickness=0)

reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(row=2, column=2)
reset_button.config(highlightthickness=0)

check_mark = Label(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 20))
check_mark.grid(column=1, row=3)

window.mainloop()