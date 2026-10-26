from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt

iris = load_iris()
X, y = iris.data, iris.target

clf = DecisionTreeClassifier()
clf.fit(X, y)

plt.figure(figsize=(10, 6))
plot_tree(clf, filled=True,
          feature_names=iris.feature_names,
          class_names=iris.target_names)
plt.show()