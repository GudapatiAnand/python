# demo_list=[5,4,4,6,8,12,12,1,5]
# unique_list=list(set(demo_list))
# print(unique_list)

# import numpy as np
# arr=np.array([1,2,3,4,5])
# print(arr.argsort()[ -5: ][::-1])

# import tkinter as tk

# def button_click(number):
#   global entry
#   entry.insert(tk.END, number)

# root = tk.Tk()
# root.title("Simple Keypad")

# entry = tk.Entry(root, width=30,)
# entry.grid(row=0, column=0, columnspan=3)

# buttons = [
#   '1', '2', '3',
#   '4', '5', '6',
#   '7', '8', '9',
#   '*', '0', '#'
# ]

# row = 1
# col = 0
# for button_text in buttons:
#   button = tk.Button(root, text=button_text, width=10, command=lambda num=button_text: button_click(num))
#   button.grid(row=row, column=col)
#   col += 1
#   if col > 2:
#     col = 0
#     row += 1

# root.mainloop()

# def longest_unique_substring(s):
#     char_index_map = {}
#     start = max_length = 0

#     for end, char in enumerate(s):
#         if char in char_index_map:
#             start = max(start, char_index_map[char] + 1)
#         char_index_map[char] = end
#         max_length = max(max_length, end - start + 1)

#     return max_length

# # Example usage
# s = input("enter the string:")
# print("The length of the longest substring is:", longest_unique_substring(s))


# # Sample list
# lst = [1, 3, 7, 7, 2, 7, 4, 5]

# # Step 1: Find the maximum value
# max_value = max(lst)

# # Step 2: Count the occurrences of the maximum value using list comprehension
# max_count = sum([1 for x in lst if x == max_value])

# print(f"The maximum value is {max_value} and it appears {max_count} times.")


def make_pretty(func):
    print("I got decorated")
    func()

@make_pretty
def ordinary():
    print("I am ordinary")