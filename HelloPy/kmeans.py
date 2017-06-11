from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

c_count = 10
s_count = 150

X, Y = make_blobs(n_samples=s_count,
                  n_features=2,
                  centers=c_count,
                  cluster_std=0.5,
                  shuffle=True,
                  random_state=0)
#
# plt.scatter(X[:, 0],
#             X[:, 1],
#             c='red',
#             marker='o',
#             s=50)

km = KMeans(n_clusters=c_count,
            init='random',
            n_init=10,
            max_iter=300,
            tol=1e-04,
            random_state=0)

y_km = km.fit_predict(X)

colors = ['blue', 'black', 'yellow', 'green', 'pink']
sharpe = ['s', 'o', 'v', '*']

for i in range(c_count):
    plt.scatter(X[y_km == i, 0],
                X[y_km == i, 1],
                s=50,
                c=colors[i % len(colors)],
                marker=sharpe[i % len(sharpe)],
                label='cluster ' + str(i))

plt.scatter(km.cluster_centers_[:, 0],
            km.cluster_centers_[:, 1],
            s=250,
            marker='*',
            c='red',
            label='centroids')

plt.legend()
plt.grid()
plt.show()
