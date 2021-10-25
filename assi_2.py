import module_grid as mg  # Module which is created by me to run this programme
import matplotlib.pyplot as plt  # module for plots
import tkinter as tk  # module for tkinter app
from sklearn import datasets, neighbors, metrics, mixture, svm  # Module to load

# data

root = tk.Tk()  # Root is the name of  my window
root.title("Assignment 2 of python")  # Title for my root window
root.geometry("700x800+100+100")  # dimension of root window

##############################################################################
# now i am creating widgets and in here those widgets are either labels or buttons.
# This widget is the label which user can see and get to know about the application
label_header = tk.Label(text="Type of classifications", fg="#565287", font="Arial, 18 bold", height=1)
label_header.grid(row=0, column=0, columnspan=3)  # To select the placement of
# widget on screen


# Second widget as a label to select the option according to that.
# Widget to select the dataset.
label_data = tk.Label(text="Select the dataset", fg="#565287", anchor="w", width=25, height=1, font="Arial, 18 bold")
label_data.grid(row=1, column=0, columnspan=2)  # For placement of widget
label_data.place(x=10, y=50)

data_variable = tk.StringVar()  # To initialise data variable


def select_item():
    select_item = data_variable.get()
    if select_item == "iris":
        data_dataset = datasets.load_iris()
        output = "Iris data is selected"
    elif select_item == "breast_data":
        output = "Breast Cancer data is selected"
        data_dataset = datasets.load_breast_cancer()
    elif select_item == "wine":
        output = "Wine data is selected"
        data_dataset = datasets.load_wine()
    label_data_output.config(text=output)
    # di - output.config(text="")


myfont = "Arial, 16"  # To mention myyfornt in here so i can just use myfont for rest
# of the font options

#############################################################################
# To create widget as radio buttons to select the data of iris

radio_buttoni = tk.Radiobutton(text="Iris Data", variable=data_variable, value="iris", font=myfont, command=select_item)
radio_buttoni.place(x=20, y=90)  # for placement of widget
radio_buttoni.deselect()  # To show the option is selected initially

# To create widget as radio buttons to select the data of breast cancer data
radio_buttonb = tk.Radiobutton(text="Breast Cancer Data", variable=data_variable, value="breast_data", font=myfont,
                               command=select_item)
radio_buttonb.place(x=160, y=90)  # for placement of widget
radio_buttonb.deselect()  # To show the option is selected initially

# To create widget as radio buttons to select the data of breast wine data
radio_buttonw = tk.Radiobutton(text="Wine Data", variable=data_variable, value="wine", font=myfont, command=select_item)
radio_buttonw.place(x=390, y=90)  # for placement of widget
radio_buttonw.deselect()  # To show the option is selected initially

# widget as Label to display the output when option is selected
label_data_output = tk.Label(text="", fg="#003366", anchor="w", width=25, height=1, font=myfont)
label_data_output.place(x=10, y=140)  # For its placement

#################################################################################
# Now we are creating widgets to select the technique from svm and KNN

# This widget will create a label to select the technique so that user can know
# what needs to be option needs to be select
label_tech = tk.Label(text="Select the technique", fg="#565287", anchor="w", width=25, height=1, font="Arial, 18 bold")
label_tech.place(x=10, y=180)  # For the placement of widget

tech = tk.StringVar()  # To initialize tech variable so that we can use it below


# This function if to give us output according to the technique whihc is
# selected by user.
def selItemK():
    select_tech = tech.get()
    if select_tech == "KNN":
        output_tech = "KNN is selected"
    elif select_tech == "SVM":
        output_tech = "SVM is selected"
    label_tech_output.config(text=output_tech)
    # di - output.config(text="")


# To create widget a radio button for KNN technique
radio_button_KNN = tk.Radiobutton(text="K Nearest Neighbours", variable=tech, value="KNN", font=myfont,
                                  command=selItemK)
radio_button_KNN.place(x=20, y=220)  # For the placement of widget
radio_button_KNN.deselect()

# To create widget a radio button for SVM technique
radio_button_SVM = tk.Radiobutton(text="Support Vector Machine", variable=tech, value="SVM", font=myfont,
                                  command=selItemK)
radio_button_SVM.place(x=280, y=220)  # For the placement of widget
radio_button_SVM.deselect()

# Label to display which option is selcetd by user
label_tech_output = tk.Label(text="", fg="#003366", anchor="w", width=25, height=1, font=myfont)
label_tech_output.place(x=10, y=280)  # For the placement of widget

#################################################################################
# Now this part will deal with k-fold options

# This widget will create a label to tell user what are those numbers for.
label_folds = tk.Label(text="Select K folds: ", fg="#565287", anchor="w", width=25, height=1, font="Arial, 18 bold")
label_folds.place(x=10, y=320)  # for the placement of widget

knn_fold = tk.StringVar()  # To initialize the knn_fold variable so, that it can be
# used below
option_list = ["Select no. of folds", "3", "5", "7"]  # To provide the options for
# k-fold
knn_fold.set("Select no. of folds")  # To have select no. of folds showing in


# empty space of drop down by default.

# This function will deal with the folds selcetd
def selected_folds():
    output_folds = str(knn_fold.get())
    if output_folds != "Select no. of folds":
        # di-output_folds = output_folds + "number of folds"
        label_output_fold.config(text=output_folds)

    # di - output.config(text="")


# Label to display output when button is clicked
label_output_fold = tk.Label(text="", fg="red", anchor="w", width=25, height=1, font=myfont)
label_output_fold.place(x=10, y=400)

# Widget to tell user if any of the option is not selected.
output = tk.Label(text="", fg="#003366", anchor="w", width=25, height=1, font=myfont)
output.place(x=10, y=480)  # Placement of widget

# This is the widget to create dropdown menu for k-fold options
drop_down = tk.OptionMenu(root, knn_fold, *option_list, command=selected_folds())
drop_down.place(x=10, y=380)  # placement of widget


# This  function is to get the output accrodding to data selceted by callong a finction
# From different module which is created by me
def get_output():
    selected_dataset = data_variable.get()
    selected_technique = tech.get()
    selected_foldnumber = knn_fold.get()

    # This loop will compare the options selcetd by user
    if selected_dataset != '' and selected_technique != '' and selected_foldnumber != "Select no. of folds":
        # output.config(text="")
        # This command will call the function module if all the conditions satisfied
        mg.output(selected_dataset, selected_technique, selected_foldnumber)

    else:
        output.config(text="Please select the correct values")


# Add Run button so that we can get the output
run_button = tk.Button(text="Run", fg="#1006C8", bg="#D5C5E0", width=10, height=1, font=myfont, command=get_output)
run_button.place(x=10, y=520)  # placement of run button

root.mainloop()
