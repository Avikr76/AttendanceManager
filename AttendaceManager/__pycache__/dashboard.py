from tkinter import *
print("hello1")
#import click_pictures
print("hello2")
root = Tk()
root.title("Attendance Manager")

print("hello3")
def button_click():
    myLabel = Label(root, text="Hello ")
    myLabel.pack()
print("hello4")
button_1 = Button(root, text="Scan", padx=40, pady=20, command=lambda:exec(open('click_pictures.py').read())).grid(row =4 , column=0)
button_2 = Button(root, text="Training", padx=40, pady=20, command=lambda:button_click()).grid(row =4 , column=1)
button_3 = Button(root, text="Take Image", padx=40, pady=20, command=lambda:button_click()).grid(row =4 , column=2)
print("hello5")
root.mainloop()