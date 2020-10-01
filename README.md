# Calculator-in-python3-tkinter
from tkinter import *
from math import *

root = Tk()
root.title("Calculator")
root.resizable(width=False, height=False)

screen = StringVar()
screen.set("0")

current = ""
power = ""

firstnum = str()
secondnum = str()
mathsign = str()

defxworking = False
percentt = False

def math_button_pressed():
    if mathsign == '+':
        button_plus.config(relief=SUNKEN)
    if mathsign == '-':
        button_minus.config(relief=SUNKEN)
    if mathsign == '*':
        button_multiply.config(relief=SUNKEN)
    if mathsign == '/':
        button_division.config(relief=SUNKEN)

def math_button_raised():
    button_plus.config(relief=RAISED)
    button_minus.config(relief=RAISED)
    button_multiply.config(relief=RAISED)
    button_division.config(relief=RAISED)

def is_int(num):
    if int(num) == float(num):
        return int(num)
    else:
        return float(num)

def number_pressed(butt):
    global current, power, firstnum, secondnum

    if mathsign == str() and defxworking == False:
        current = current + str(butt)
        screen.set(current)
        firstnum = float(current)

    elif mathsign != str() and defxworking == False:
        math_button_raised()
        current = current + str(butt)
        screen.set(current)
        secondnum = float(current)

    elif mathsign == str() and defxworking == True:
        power = power + str(butt)
        current = current + str(butt)
        screen.set(current)

    elif mathsign != str and defxworking == True:
        power = power + str(butt)
        current = current + str(butt)
        screen.set(current)
        print(power)

def math_pressed(math):
    global current, power, mathsign, firstnum, secondnum, defxworking, percentt

    if mathsign == str() and defxworking == False and percentt == False and firstnum != str():
        mathsign = str(math)
        math_button_pressed()
        current = ""

    elif mathsign != str() and defxworking == False and percentt == False:
        print(2)
        if mathsign == '+':
            firstnum = round(float(firstnum + secondnum),6)
        if mathsign == '-':
            firstnum = round(float(firstnum - secondnum),6)
        if mathsign == '*':
            firstnum = round(float(firstnum * secondnum),6)
        if mathsign == '/':
            firstnum = round(float(firstnum / secondnum),6)
        screen.set(is_int(firstnum))

        mathsign = str(math)
        math_button_pressed()
        current = ""

    elif mathsign != str() and defxworking == True and percentt == False:
        if mathsign == '+':
            firstnum = round(firstnum + secondnum ** int(power),6)
        if mathsign == '-':
            firstnum = round(firstnum - secondnum ** int(power),6)
        if mathsign == '*':
            firstnum = round(firstnum * (secondnum ** int(power)),6)
        if mathsign == '/':
            firstnum = round(firstnum / (secondnum ** int(power)),6)
        defxworking = False
        screen.set(is_int(firstnum))
        defxworking = False
        mathsign = str(math)
        math_button_pressed()
        power = ""
        current = ""

    elif defxworking and percentt == False:
        firstnum = round(firstnum ** int(power), 6)
        defxworking = False
        screen.set(is_int(firstnum))
        mathsign = str(math)
        math_button_pressed()
        power = ""
        current = ""

    elif percentt:
        if mathsign == '+':
            firstnum = round(float(firstnum + firstnum/100*secondnum),6)
        if mathsign == '-':
            firstnum = round(float(firstnum - firstnum/100*secondnum),6)
        screen.set(is_int(firstnum))
        percentt = False
        mathsign = str(math)
        math_button_pressed()
        current = ""

def squareroot():
    global firstnum, secondnum, mathsign, current

    if mathsign == str():
        firstnum = round(sqrt(firstnum),6)
        screen.set(is_int(firstnum))

    if mathsign != str():
        if mathsign == '+':
            firstnum = round(sqrt(firstnum + float(secondnum)),6)
        if mathsign == '-':
            firstnum = round(sqrt(firstnum - float(secondnum)),6)
        if mathsign == '*':
            firstnum = round(sqrt(firstnum * float(secondnum)),6)
        if mathsign == '/':
            firstnum = round(sqrt(firstnum / float(secondnum)),6)

        screen.set(is_int(firstnum))
        secondnum = str()
        mathsign = str()
        current = ""

def x():
    global firstnum, secondnum, mathsign, current, defxworking

    if mathsign == str():
        current = str(is_int(firstnum)) + '^'
        screen.set(current)
        defxworking = True

    elif mathsign != str():

        current = str(is_int(secondnum)) + '^'
        screen.set(current)
        defxworking = True

def result():
    global firstnum, secondnum, mathsign, current, power, defxworking, percentt
    if defxworking == False and percentt == False:
        if mathsign == '+':
            firstnum = round(float(firstnum + secondnum),6)
        if mathsign == '-':
            firstnum = round(float(firstnum - secondnum),6)
        if mathsign == '*':
            firstnum = round(float(firstnum * secondnum),6)
        if mathsign == '/':
            firstnum = round(float(firstnum / secondnum),6)
        screen.set(is_int(firstnum))

    if mathsign == str() and defxworking == True and percentt == False:
        firstnum = round(firstnum ** int(power),6)
        defxworking = False
        screen.set(is_int(firstnum))

    if mathsign != str() and defxworking == True and percentt == False:
        if mathsign == '+':
            firstnum = round(firstnum + secondnum ** int(power),6)
            defxworking = False
        if mathsign == '-':
            firstnum = round(firstnum - secondnum ** int(power),6)
            defxworking = False
        if mathsign == '*':
            firstnum = round(firstnum * (secondnum ** int(power)),6)
            defxworking = False
        if mathsign == '/':
            firstnum = round(firstnum / (secondnum ** int(power)),6)
            defxworking = False
        screen.set(is_int(firstnum))


    if defxworking == False and percentt == True:
        if mathsign == '+':
            firstnum = round(float(firstnum + firstnum/100*secondnum),6)
            screen.set(is_int(firstnum))
            percentt = False
        if mathsign == '-':
            firstnum = round(float(firstnum - firstnum/100*secondnum),6)
            screen.set(is_int(firstnum))
            percentt = False

    mathsign = str()
    current = ""
    power = ""

    if defxworking == False and mathsign == '*' or '/' and percentt == True:
        clear()

def clear():
    global current, firstnum, secondnum, mathsign, power, defxworking, percentt

    screen.set(0)
    current = ""
    power = ""
    firstnum = str()
    secondnum = str()
    mathsign = str()
    defxworking = False
    math_button_raised()
    percentt = False

def percent():
    global firstnum, secondnum, current, percentt

    current = str(is_int(secondnum)) + '%'
    screen.set(current)
    percentt = True



# Widgets

calculation = Entry(root, textvariable = screen, font=("Verdana", 15, ), bd = 12,
                    insertwidth=4, width=14, justify=RIGHT)
calculation.grid(columnspan=4)
#   Numbers
button1 = Button(root, text='1', command=lambda: number_pressed(1), bg="gainsboro",
                 bd=3, padx=12, pady=5, font=("Helvetica", 14, "bold"))
button1.grid(row=2, column=0, sticky=W)
button2 = Button(root, text='2', command=lambda: number_pressed(2), bg="gainsboro",
                 bd=3, padx=12, pady=5, font=("Helvetica", 14, "bold"))
button2.grid(row=2, column=1, sticky=W)
button3 = Button(root, text='3', command=lambda: number_pressed(3), bg="gainsboro",
                 bd=3, padx=12, pady=5, font=("Helvetica", 14, "bold"))
button3.grid(row=2, column=2, sticky=W)
button4 = Button(root, text='4', command=lambda: number_pressed(4), bg="gainsboro",
                 bd=3, padx=12, pady=5, font=("Helvetica", 14, "bold"))
button4.grid(row=3, column=0, sticky=W)
button5 = Button(root, text='5', command=lambda: number_pressed(5), bg="gainsboro",
                 bd=3, padx=12, pady=5, font=("Helvetica", 14, "bold"))
button5.grid(row=3, column=1, sticky=W)
button6 = Button(root, text='6', command=lambda: number_pressed(6), bg="gainsboro",
                 bd=3, padx=12, pady=5, font=("Helvetica", 14, "bold"))
button6.grid(row=3, column=2, sticky=W)
button7 = Button(root, text='7', command=lambda: number_pressed(7), bg="gainsboro",
                 bd=3, padx=12, pady=5, font=("Helvetica", 14, "bold"))
button7.grid(row=4, column=0, sticky=W)
button8 = Button(root, text='8', command=lambda: number_pressed(8), bg="gainsboro",
                 bd=3, padx=12, pady=5, font=("Helvetica", 14, "bold"))
button8.grid(row=4, column=1, sticky=W)
button9 = Button(root, text='9', command=lambda: number_pressed(9), bg="gainsboro",
                 bd=3, padx=12, pady=5, font=("Helvetica", 14, "bold"))
button9.grid(row=4, column=2, sticky=W)
button0 = Button(root, text='0', command=lambda: number_pressed(0), bg="gainsboro",
                 bd=3, padx=12, pady=5, font=("Helvetica", 14, "bold"))
button0.grid(row=5, column=0, sticky=W)
button_float = Button(root, text='.', command=lambda: number_pressed('.'), bg="gainsboro",
                      bd=3, padx=15, pady=5, font=("Helvetica", 14, "bold"))
button_float.grid(row=5, column=1)

#   Math signs
button_plus = Button(root, text='+', command=lambda: math_pressed('+'), bg="gray70",
                     bd=3, padx=11, pady=5, font=("Helvetica", 14, "bold"))
button_plus.grid(row=2, column=3, sticky=W)
button_minus = Button(root, text='-', command=lambda: math_pressed('-'),  bg="gray70",
                      bd=3, padx=11, pady=4, font=("Verdana", 14, "bold"))
button_minus.grid(row=3, column=3, sticky=W)
button_multiply = Button(root, text='*', command=lambda: math_pressed('*'), bg="gray70",
                         bd=3, padx=13, pady=5, font=("Helvetica", 14, "bold"))
button_multiply.grid(row=4, column=3, )
button_division = Button(root, text='/', command=lambda: math_pressed('/'),  bg="gray70",
                         bd=3, padx=14, pady=5, font=("Helvetica", 14, "bold"))
button_division.grid(row=5, column=3, )
button_equal = Button(root, text='=', command=lambda: result(), bg='orange',
                      bd=3, padx=12, pady=5, font=("Arial", 14))
button_equal.grid(row=5, column=2, )

button_percent = Button(root, text='%', command=lambda: percent(),  bg="gray70",
                         bd=3, padx=8, pady=5, font=("Helvetica", 14, "bold"))
button_percent.grid(row=1, column=3, )

button_clear = Button(root, text='C', command=lambda: clear(), bg='gray70',
                      bd=3, padx=11, pady=5, font=("Helvetica", 14))
button_clear.grid(row=1, column=0)
button_sqrt = Button(root, text='√', command=lambda: squareroot(), bg="gray70",
                        bd=3, padx=12, pady=5, font=("Helvetica", 14, "bold"))
button_sqrt.grid(row=1, column=1, sticky=W)
button_x = Button(root, text='x^y', command=lambda: x(), bg="gray70",
                  bd=3, padx=6, pady=5, font=("Helvetica", 14))
button_x.grid(row=1, column=2, sticky=W)

root.mainloop()
