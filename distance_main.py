import numpy as np
import argparse
from utils.crp import DCRP
from utils.traverse_by_idx import traverse_by_idx
from sklearn.datasets import load_iris
from sklearn.metrics import adjusted_rand_score
from sklearn.utils import shuffle

parser = argparse.ArgumentParser()
parser.add_argument("-alpha", type=float, default=0.05)
parser.add_argument("-n_iters", type=int, default=5)
args = parser.parse_args()

alpha = args.alpha
n_iters = args.n_iters
print(f"running for {n_iters} with alpha={alpha}")

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
    dcrp = DCRP(alpha)
    for row in iris_data['data']:
        dcrp.seat(row)
    
    # print(dcrp.customer_list)
    ## get results:
    # num_clusters.append(len(dcrp.customer_list))
    # accuracy.append(np.sum(np.array(dcrp.assignments)==iris_data['target']) / iris_data['target'].shape[0])
    clusters = traverse_by_idx(dcrp.assignments)
    adj_rand.append(adjusted_rand_score(iris_data['target'], np.array(clusters)))
# print(dcrp.assignments)
# clusters = traverse_by_idx(dcrp.assignments)
print(adj_rand)
# breakpoint()
# ## average results
# avg_num_clusters, std_num_clusters = np.round(np.mean(num_clusters),2), np.round(np.std(num_clusters),2)
# avg_accuracy, std_accuracy = np.round(np.mean(accuracy),2), np.round(np.std(accuracy), 2)
# avg_adj_rand, std_adj_rand = np.round(np.mean(adj_rand),2), np.round(np.std(adj_rand), 2)

# print(f"NUM CLUSTERS: {avg_num_clusters} +/- {std_num_clusters}")
# print(f"ACCURACY: {avg_accuracy} +/- {std_accuracy}")
# print(f"ADJUSTED_RAND_SCORE: {avg_adj_rand} +/- {std_adj_rand}")

