from sklearn.metrics import silhouette_score, davies_bouldin_score

def silhouette(X, labels):
    """Compute silhouette score"""
    return silhouette_score(X, labels)

def db_index(X, labels):
    """Compute Davies-Bouldin Index"""
    return davies_bouldin_score(X, labels)
