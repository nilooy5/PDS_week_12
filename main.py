import tkinter as tk

window = tk.Tk()
window.title('Programming for Data Science')
# width x height + x_offset + y_offset:
window.geometry("500x250+100+100")

# Set font
myFont = "Arial, 16"
# Add a label
lbl_header = tk.Label(text="A Simple GUI App", font=myFont, height=1)
lbl_header.place(x=150, y=10)
# Add label
lbl = tk.Label(text="Select a colour: ", fg="navy", anchor="w", width=25, height=1, font=myFont)
lbl.place(x=10, y=50)
# Add variable var and 2 radio buttons
var = tk.StringVar()
rb1 = tk.Radiobutton(text="red", variable=var, value='r', font=myFont)
rb1.place(x=180, y=50)
rb1.deselect()

rb2 = tk.Radiobutton(text="blue", variable=var, value='b', font=myFont)
rb2.place(x=250, y=50)
rb2.deselect()
# Label to display output when button is clicked
lb_output = tk.Label(text="", fg="navy", anchor="w", width=25, height=1, font=myFont)
lb_output.place(x=10, y=100)


#################################

def select_item():
    selected = var.get()
    if selected == 'r':
        output = 'Red selected'
    elif selected == 'b':
        output = 'Blue selected'
    else:
        output = "Please select a colour"

    lb_output.config(text=output)
#################################


# Add button
button = tk.Button(text="Run", fg="black", bg="lightblue", width=10, height=1, font=myFont, command=select_item)
button.place(x=10, y=150)

window.mainloop()
