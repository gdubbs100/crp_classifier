import numpy as np
import argparse
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score
from sklearn.utils import shuffle

parser = argparse.ArgumentParser()
parser.add_argument("-k", type=int, default=3)
args = parser.parse_args()

k = args.k

iris_data = load_iris()
## rearrange the data
(
    iris_data['data'], 
    iris_data['target']
) = shuffle(iris_data['data'], iris_data['target'])

kmeans = KMeans(n_clusters=k, random_state=1234)

kmeans.fit(iris_data['data'])
preds = kmeans.predict(iris_data['data'])
    
## get results:
accuracy = (np.sum(preds==iris_data['target']) / iris_data['target'].shape[0])
adj_rand = (adjusted_rand_score(iris_data['target'], preds))

print(f"ACCURACY: {accuracy}")
print(f"ADJUSTED_RAND_SCORE: {adj_rand}")
