# encoding=utf8
import os, sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
style.use("ggplot")
from sklearn.cluster import KMeans

# X is a list of lat-long coordinate lists
X = np.array()

# 35 clusters
kmeans = KMeans(n_clusters=35)
kmeans.fit(X)

centroids = kmeans.cluster_centers_
labels = kmeans.labels_

print(centroids)
print(labels)

colors = 7*["g.","r.","c.","y.", "b."]

for i in range(len(X)):
    print("coordinate:", X[i], "label:", labels[i])
    plt.plot(X[i] [0], X[i] [1], colors[labels[i]], markersize=10)

plt.scatter(centroids[:, 0],centroids[:, 1], marker = "x", s=150, linewidths=5,\
zorder=10)
plt.show()
