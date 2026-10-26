from sklearn.cluster import KMeans
from sklearn.datasets import load_iris

X, _ = load_iris(return_X_y=True)

k = KMeans(n_clusters=3)
k.fit(X)

print(k.labels_)