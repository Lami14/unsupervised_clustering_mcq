from sklearn.cluster import KMeans, AgglomerativeClustering

def kmeans_cluster(X, n_clusters=5):
    """Fit K-Means and return the model"""
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    kmeans.fit(X)
    return kmeans

def hierarchical_cluster(X, n_clusters=5, linkage='ward'):
    """Fit Agglomerative Clustering and return labels"""
    cluster = AgglomerativeClustering(n_clusters=n_clusters, linkage=linkage)
    labels = cluster.fit_predict(X)
    return labels
