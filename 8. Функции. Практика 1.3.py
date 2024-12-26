import tkinter as tk
import math

# Логика

def get_values():
    num1 = int(number1_entry.get())
    num2 = int(number2_entry.get())
    return num1, num2

def insert_values(value):
    answer_entry.delete(0, 'end')
    answer_entry.insert(0, value)

def add():
    num1, num2 = get_values()
    res = num1 + num2
    insert_values(res)

def sub():
    num1, num2 = get_values()
    res = num1 - num2
    insert_values(res)

def div():
    num1, num2 = get_values()
    res = num1 / num2
    insert_values(res)

def mul():
    num1, num2 = get_values()
    res = num1 * num2
    insert_values(res)

# Интерфейс

window = tk.Tk()
window.title('Калькулятор')
window.geometry('500x500')
window.resizable(False, False)
button_add = tk.Button(window, text='+', width=15, height=3, command=add)
button_add.place(x=75, y=300)
button_sub = tk.Button(window, text='-', width=15, height=3, command=sub)
button_sub.place(x=75, y=375)
button_mul = tk.Button(window, text='*', width=15, height=3, command=mul)
button_mul.place(x=200, y=300)
button_div = tk.Button(window, text='/', width=15, height=3, command=div)
button_div.place(x=200, y=375)
number1_entry = tk.Entry(window, width=50)
number1_entry.place(x=100, y=50)
number2_entry = tk.Entry(window, width=50)
number2_entry.place(x=100, y=100)
answer_entry = tk.Entry(window, width=50)
answer_entry.place(x=100, y=200)
number1 = tk.Label(window, text='Первое число:')
number1.place(x=25, y=25)
number2 = tk.Label(window, text='Второе число:')
number2.place(x=25, y=75)
answer = tk.Label(window, text='Ответ:')
answer.place(x=50, y=175)
window.mainloop()