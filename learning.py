# demo_list=[5,4,4,6,8,12,12,1,5]
# unique_list=list(set(demo_list))
# print(unique_list)

# import numpy as np
# arr=np.array([1,2,3,4,5])
# print(arr.argsort()[ -5: ][::-1])

import tkinter as tk

def button_click(number):
  global entry
  entry.insert(tk.END, number)

root = tk.Tk()
root.title("Simple Keypad")

entry = tk.Entry(root, width=30,)
entry.grid(row=0, column=0, columnspan=3)

buttons = [
  '1', '2', '3',
  '4', '5', '6',
  '7', '8', '9',
  '*', '0', '#'
]

row = 1
col = 0
for button_text in buttons:
  button = tk.Button(root, text=button_text, width=10, command=lambda num=button_text: button_click(num))
  button.grid(row=row, column=col)
  col += 1
  if col > 2:
    col = 0
    row += 1

root.mainloop()