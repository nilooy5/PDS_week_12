# First i am going to import the modules which are needed to make this module work. 
# This module is to work according to the options selcted by the user on t
# tkinter screen.


import matplotlib.pyplot as plt  # Module for plot
from sklearn import datasets, neighbors, metrics, mixture, svm  # modeule for
# different machine learning  teachniques
from sklearn.model_selection import train_test_split, GridSearchCV  # module for


# grid search and to spelt the data in test and training


# This function is going to give me output for accuracy mtarix and plot
def output(selected_dataset, selected_classifier, selected_fold):
    # These 3 values are : data set which is selected , techniques and folds

    # My first step is i am loading there data which is selected by user
    if selected_dataset == "iris":  # To check the data which is selected
        dataset = datasets.load_iris()  # to load the selected data
    elif selected_dataset == "breast_data":
        dataset = datasets.load_breast_cancer()
    elif selected_dataset == "wine":
        dataset = datasets.load_wine()

    if selected_classifier == "KNN":  # To check the technique which is selected
        classifier = neighbors.KNeighborsClassifier()  # Load classifier and its
        # parameter for cross-validation
        parameter = [{'n_neighbors': range(30)}]
        # param_name = "Parameter KNN"
        y_parameter = "Value of K for KNN"  # To assign parameter name so that we can
        # use in graph
    elif selected_classifier == "SVM":  # To check which method is selected
        classifier = svm.SVC(gamma=0.3)  # Load classifier and its parameter
        # for cross-validation
        parameter = [{'gamma': [0.0001, 0.001, 0.01, 0.1, 1.0]}]
        # param_name = "Parameter SVM"
        y_parameter = "Parameter C"  # To assign parameter name so that we can
        # use in graph
    cv_Input = int(selected_fold)  # To get value of folds but as an integer

    final_data = dataset.data
    final_target = dataset.target
    class_names = dataset.target_names

    # Split the dataset into training and testing sets
    final_data_train, final_data_test, final_target_train, final_target_test = train_test_split(
        final_data, final_target, test_size=0.2, random_state=0)

    # Training the data
    classifier.fit(final_data_train, final_target_train)

    # Testing the data by calculating predicted values by model
    y_pred = classifier.predict(final_data_test)
    print(y_pred)  # Printing the predicted values

    # Load grid search cross validation
    gscv_classifier = GridSearchCV(
        estimator=classifier,
        param_grid=parameter,
        cv=cv_Input,  # to get values of fold whihc is selected by user.
        scoring='accuracy'
    )

    gscv_classifier.fit(final_data_train, final_target_train)

    print("Grid scores on validation set:")
    print()
    means = gscv_classifier.cv_results_['mean_test_score']  # To get the mean values
    stds = gscv_classifier.cv_results_['std_test_score']
    results = gscv_classifier.cv_results_['params']
    # This loop will print all the values on screen
    for mean, std, param in zip(means, stds, results):
        print("Parameter: %r, accuracy: %0.3f (+/-%0.03f)" % (param, mean, std * 2))
    # print()

    # This will give use the best accuracy value
    print("Best parameter:", gscv_classifier.best_params_)

    predicted_value = gscv_classifier.predict(final_data_test)
    # This will give us the accuracy score
    accuracy = metrics.accuracy_score(final_target_test, predicted_value) * 100
    # This will plot the confusion matrix which will tell us how many values
    # were predicted wrong and it will show the accuracy of model.
    plotcm = metrics.plot_confusion_matrix(gscv_classifier, final_data_test, final_target_test,
                                           display_labels=class_names)
    plotcm.ax_.set_title('Accuracy = {0:.2f}%'.format(accuracy))
    # To show the plot on screen
    plt.show()
    x_axis_parameter = list(parameter[0].values())[0]  # To assign values to x-axis
    print(x_axis_parameter)     # same thing
    print(parameter[0]['n_neighbors'])      # same thing
    y_axis_parameter = means  # to assign values to y-axis according to model and
    # calculation done above
    line_type = 'g--'  # to get green dashed line for plot
    # ax.plot(x2, y2, s2)
    ax = plt.axes()
    plt.title("Graph between CV score and Technique selected")  # To give us ttitle
    # of plot
    plt.xlabel(y_parameter)  # to assign x-axis label according to model selected
    plt.ylabel("CV Score")  # to assign y-axis label
    # delete it ax.set(xlabel=param_name, ylabel='Score', title='Score Vs Parameter')
    p = ax.plot(x_axis_parameter, y_axis_parameter, line_type)  # To plot the plot

    # di -stack side by side
    # di - fig.canvas.manager.window.wm_geometry("+%d+%d" % (750, 100))

    plt.show()  # To show the plot on screen
