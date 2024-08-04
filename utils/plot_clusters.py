import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np

def plot_clusters(data, target, figsize):
    tups = [(i, i+1) for i in range(data.shape[1]-1)]
    fig, ax = plt.subplots(1, len(tups), figsize = figsize)
    ax = ax.flatten()
    unique_classes = np.unique(target)
    class_color = mcolors.TABLEAU_COLORS
    # breakpoint()
    for i, tup in enumerate(tups):
        x = data[:, tup[0]]
        y = data[:, tup[1]]

        plot_label_clusters(
            x, y, target, ax[i], unique_classes, class_color
        )

    plt.tight_layout()
    plt.show()

def plot_label_clusters(x, y, classes, ax, unique_classes, class_color):
    for _cls, color in zip(unique_classes, class_color):
        # breakpoint()
        mask = classes == _cls
        ax.scatter(
            x[mask],
            y[mask],
            c = color,
            label=f"Class: {_cls}"
        )

    ax.legend()


if __name__=="__main__":

    from sklearn.datasets import load_iris

    iris_data = load_iris()
    data = iris_data['data']
    target = iris_data['target']

    plot_clusters(
        data=data, target=target, figsize=(14,7)
    )


