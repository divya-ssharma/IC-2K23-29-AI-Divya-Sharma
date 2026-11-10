import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

np.random.seed(7)
X = np.random.randn(100, 5)
X[:, 1] = X[:, 0] * 0.8 + np.random.randn(100) * 0.1
X[:, 2] = X[:, 0] * 0.5 + np.random.randn(100) * 0.2

pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)

print(X.shape, X_pca.shape)
print(pca.explained_variance_ratio_)

plt.scatter(X_pca[:, 0], X_pca[:, 1])
plt.savefig('pca.png')
plt.close()
