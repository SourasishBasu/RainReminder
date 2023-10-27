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

# ---------------------------- TIMER MECHANISM ------------------------------- #

def timer_start():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text = "Break", fg = RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text = "Break", fg = PINK)
    else:
        count_down(work_sec)
        timer_label.config(text = "Work", fg = RED)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    min = math.floor(count/60)
    sec = count % 60
    if sec < 10:
        sec = f"0{sec}"

    canvas.itemconfig(timer_text, text=f"{min}:{sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        timer_start()
        mark=""
        work_sessions = math.floor(reps/2)
        for i in range(work_sessions):
            mark += "✓"
        check.config(text = mark)


# ---------------------------- TIMER RESET ------------------------------- #
def timer_reset():
    window.after_cancel(timer_text)
    canvas.itemconfig(timer_text, text = "00:00")
    timer_label.config(text = "Timer")
    check.config(text = "")
    global reps
    reps = 0

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="assets/tomato.png")
canvas.create_image(100,112, image=tomato_img)
timer_text = canvas.create_text(100,130,text="00:00", fill="white",font=("Arial",30,"bold"))
canvas.grid(column=1, row=1)

timer_label = Label(text="TIMER", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
timer_label.grid(column=1, row=0)

start = Button(text="Start", highlightthickness=0, command = timer_start)
start.grid(column=0, row=2)

reset = Button(text="Reset", highlightthickness=0, command=timer_reset)
reset.grid(column=2, row=2)

check=Label(fg=GREEN, bg =YELLOW, font=("Arial", 20, "bold"))
check.grid(column=1, row=3)


window.mainloop()