import tkinter as tk

window = tk.Tk()
window.title('Programming for Data Science')
# width x height + x_offset + y_offset:
window.geometry("700x250+100+100")

# Set font
myFont = "Arial, 16"
# Add a label
lbl_header = tk.Label(text="A Simple GUI App", font=myFont, height=1)
lbl_header.place(x=150, y=10)
# Add label
lbl = tk.Label(text="Select a colour: ", fg="navy", anchor="w", width=25, height=1, font=myFont)
lbl.place(x=10, y=50)


# Add variable var and 2 radio buttons
dataset_name = tk.StringVar(value="red")

rb1 = tk.Radiobutton(text="red", variable=dataset_name, value='red', font=myFont)
rb1.place(x=180, y=50)
# rb1.deselect()

rb2 = tk.Radiobutton(text="blue", variable=dataset_name, value='blue', font=myFont)
rb2.place(x=250, y=50)
# rb2.deselect()
# Label to display output when button is clicked
lb_output = tk.Label(text="", fg="navy", anchor="w", width=25, height=1, font=myFont)
lb_output.place(x=10, y=100)

# Add variable var and 2 radio buttons
dataset_name = tk.StringVar(value="iris")

rb1 = tk.Radiobutton(text="Iris", variable=dataset_name, value='iris', font=myFont)
rb1.place(x=180, y=50)

rb2 = tk.Radiobutton(text="Breast Cancer", variable=dataset_name, value='breast_cancer', font=myFont)
rb2.place(x=250, y=50)

rb3 = tk.Radiobutton(text="Wine", variable=dataset_name, value='wine', font=myFont)
rb3.place(x=450, y=50)

# Label to display output when button is clicked
lb_output = tk.Label(text="", fg="navy", anchor="w", width=25, height=1, font=myFont)
lb_output.place(x=10, y=100)


#################################

def select_dataset():
    selected = dataset_name.get()
    if selected == 'iris':
        output = 'Iris selected'
    elif selected == 'breast_cancer':
        output = 'Breast Cancer selected'
    elif selected == 'wine':
        output = 'Wine selected'
    else:
        output = "Please select a dataset"

    lb_output.config(text=output)
#################################


# Add button
button = tk.Button(text="Run Model", fg="black", bg="lightblue", width=10, height=1, font=myFont, command=select_dataset)
button.place(x=10, y=150)

window.mainloop()
