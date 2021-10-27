import os
from pathlib import Path

from sklearn import datasets, neighbors, metrics, mixture, svm
from sklearn.model_selection import train_test_split, GridSearchCV
import matplotlib.pyplot as plt
import numpy as np

dataset = datasets.load_iris()

x = dataset.data
y = dataset.target
class_names = dataset.target_names

X_train, X_test, Y_train, Y_test = train_test_split(x, y, test_size=0.3, random_state=0)

parameter = [{'n_neighbors': range(30)}]

knn_classifier = neighbors.KNeighborsClassifier()

gscv_classifier = GridSearchCV(
    estimator=knn_classifier,
    param_grid=parameter,
    cv=5,  # k-fold cross validation
    scoring='accuracy'
)

gscv_classifier.fit(X_train, Y_train)

means = gscv_classifier.cv_results_['mean_test_score']
stds = gscv_classifier.cv_results_['std_test_score']
results = gscv_classifier.cv_results_['params']

print("Grid scores on validation set:")
print()

for mean, std, param in zip(means, stds, results):
    print("Parameter: %r, accuracy: %0.3f (+/-%0.03f)" % (param, mean, std*2))
print()
print("Best parameter:", gscv_classifier.best_params_)

y_pred = gscv_classifier.predict(X_test)
# • Plot confusion matrix and accuracy
accuracy = metrics.accuracy_score(Y_test, y_pred) * 100
plotcm = metrics.plot_confusion_matrix(gscv_classifier, X_test, Y_test, display_labels=class_names)
plotcm.ax_.set_title('Accuracy = {0:.2f}%'.format(accuracy))


def generate_image_from_plot():

    file_name = "myplot.png"
    file_dir = str(Path.home())
    # completeName = os.path.join(file_dir, file_name)
    complete_file_path = file_dir + '\\' + file_name
    print("image file created at: " + file_dir + '\\' + file_name)
    plt.savefig(complete_file_path, format='png')

print(plotcm.confusion_matrix)
# generate_image_from_plot()
plt.show()
