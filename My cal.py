from tkinter import *

def clickbut(number):
    global operator
    operator = operator + str(number)
    textin.set(operator)

def clear_entry():
    textin.set('')

def calculate_result():
    try:
        result = str(eval(operator))
        textin.set(result)
    except Exception as e:
        textin.set("Error")

def add_functionality(symbol):
    global operator
    operator = operator + str(symbol)
    textin.set(operator)

def square_root():
    try:
        result = str(eval(operator) ** 0.5)
        textin.set(result)
    except Exception as e:
        textin.set("Error")

def percentage():
    try:
        result = str(eval(operator) / 100)
        textin.set(result)
    except Exception as e:
        textin.set("Error")

def exponentiation():
    global operator
    operator = operator + "**"
    textin.set(operator)

me = Tk()
me.geometry("354x460")
me.title("CALCULATOR")
melabel = Label(me, text="CALCULATOR", bg='White', font=("Times", 30, 'bold'))
melabel.pack(side=TOP)
me.config(background='Dark gray')

textin = StringVar()
operator = ""

metext = Entry(me, font=("Courier New", 12, 'bold'), textvar=textin, width=25, bd=5, bg='powder blue')
metext.pack()

buttons = [
    ["7", 140, 100], ["8", 140, 170], ["9", 140, 240],
    ["4", 75, 100], ["5", 75, 170], ["6", 75, 240],
    ["1", 10, 100], ["2", 10, 170], ["3", 10, 240],
    ["0", 10, 310], [".", 75, 310], ["+", 205, 100],
    ["-", 205, 170], ["*", 205, 240], ["/", 205, 310],
    ["CE", 270, 100], ["=", 10, 380], ["√", 270, 240],
    ["%", 270, 310], ["^", 270, 170]
]

for button in buttons:
    btn_text, x_pos, y_pos = button
    Button(me, padx=14, pady=14, bd=4, bg='white', text=btn_text,
           command=lambda btn=btn_text: clickbut(btn) if btn != "=" else calculate_result(),
           font=("Courier New", 16, 'bold')).place(x=x_pos, y=y_pos)

me.mainloop()

