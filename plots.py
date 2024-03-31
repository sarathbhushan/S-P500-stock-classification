import matplotlib.pyplot as plt

def plot_elbow_curve(wcss, max_k):
    plt.plot(range(1, max_k + 1), wcss, marker='o')
    plt.title('Elbow Curve')
    plt.xlabel('Number of clusters')
    plt.ylabel('WCSS')
    plt.show()