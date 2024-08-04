import numpy as np
import argparse
from utils.crp import DCRP
from utils.traverse_by_idx import traverse_by_idx
from utils.plot_clusters import plot_clusters
from utils.distance_utils import DistanceFunc, euc_dist
from sklearn.cluster import KMeans, DBSCAN
from sklearn.datasets import load_iris
from sklearn.metrics import adjusted_rand_score
from sklearn.utils import shuffle

parser = argparse.ArgumentParser()
parser.add_argument("-alpha", type=float, default=0.05)
parser.add_argument("-n_iters", type=int, default=5)
parser.add_argument("-algo", type=str, help = "Choose one of DCRP, KMEANS or DBSCAN", default="DCRP")

## DCRP args
parser.add_argument("-distance_expon", type=int, default=2)

## Kmeans args
parser.add_argument("-k", type=int, default=3)

## dbscan args
parser.add_argument("-eps", type=float, default = 0.5)
parser.add_argument("-min_samples", type=float, default = 5)
parser.add_argument("-metric", type=str, default = "euclidean")

args = parser.parse_args()

alpha = args.alpha
n_iters = args.n_iters
algo = args.algo
print(f"running for {n_iters} iters with {algo}")

distance_func = DistanceFunc(euc_dist, {'d': args.distance_expon})

num_clusters = []
accuracy = []
adj_rand = []

iris_data = load_iris()
## rearrange the data
(
    iris_data['data'], 
    iris_data['target']
) = shuffle(iris_data['data'], iris_data['target'])

for i in range(n_iters):
    if algo == 'DCRP':
        dcrp = DCRP(alpha, distance_func=distance_func)
        for row in iris_data['data']:
            dcrp.seat(row)
        
        clusters = traverse_by_idx(dcrp.assignments)
        adj_rand.append(adjusted_rand_score(iris_data['target'], np.array(clusters)))
    
    if algo == 'KMEANS':
        kmeans = KMeans(n_clusters=args.k, random_state=1234)

        kmeans.fit(iris_data['data'])
        clusters = kmeans.predict(iris_data['data'])
        adj_rand.append(adjusted_rand_score(iris_data['target'], clusters))

    if algo == "DBSCAN":
        dbscan = DBSCAN(
            eps = args.eps,
            min_samples = args.min_samples,
            metric=args.metric)


        clusters = dbscan.fit_predict(iris_data['data'])
        adj_rand.append(adjusted_rand_score(iris_data['target'], clusters))



print(adj_rand)
plot_clusters(
    data = iris_data['data'],
    target = clusters,
    figsize = (14, 7)
)


