from sklearn import datasets, neighbors, metrics, mixture, svm
from sklearn.model_selection import train_test_split, GridSearchCV
import matplotlib.pyplot as plt
import numpy as np

dataset = datasets.load_iris()

x = dataset.data
y = dataset.target
class_names = dataset.target_names

X_train, X_test, Y_train, Y_test = train_test_split(x, y, test_size=0.3, random_state=0)

parameter = [{'n_neighbors': [1, 2, 3, 4, 5]}]

knn_classifier = neighbors.KNeighborsClassifier()

gscv_classifier = GridSearchCV(
    estimator=knn_classifier,
    param_grid=parameter,
    cv=5,  # k-fold cross validation
    scoring='accuracy'
)

gscv_classifier.fit(X_train, Y_train)

print(gscv_classifier.best_params_)

print(gscv_classifier.cv_results_['mean_test_score'])
print(gscv_classifier.cv_results_['std_test_score'])
print(gscv_classifier.cv_results_['params'])

y_pred = gscv_classifier.predict(X_test)
# • Plot confusion matrix and accuracy
accuracy = metrics.accuracy_score(Y_test, y_pred) * 100
plotcm = metrics.plot_confusion_matrix(gscv_classifier, X_test, Y_test, display_labels=class_names)
plotcm.ax_.set_title('Accuracy = {0:.2f}%'.format(accuracy))
plt.show()
# plt.savefig('pic')
