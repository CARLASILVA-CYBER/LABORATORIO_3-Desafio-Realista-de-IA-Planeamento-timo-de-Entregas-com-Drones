from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier

X, y = load_digits(return_X_y=True)

X_train, X_test, y_train, y_test = train_test_split(X, y)

model = MLPClassifier()
model.fit(X_train, y_train)

print("Accuracy:", model.score(X_test, y_test))
