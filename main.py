import numpy as np
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-N", type=int, default=10)
parser.add_argument("-alpha", type=float, default=0.05)
args = parser.parse_args()

N = args.N
alpha = args.alpha

print(f"Running with N={N} and alpha={alpha}")

## first attempt from here:
## https://compcogsci-3016.djnavarro.net/technote_chineserestaurantprocesses.pdf
assignments = np.zeros((N, 1))
counts = np.zeros((N, 1)) # counts for clusters, N is max possible K
assignments[0] = 1
counts[0] = 1
counts[1] = alpha
K = 1 # num unique clusters
x=[i for i in range(0, N)]

for i in range(1, N):
    
    assignment = np.random.choice(x, p=(counts/counts.sum(axis=0)).ravel())
    if assignment == np.max(np.where(counts > 0)[0]):
        counts[assignment] += 1 - alpha
        counts[assignment + 1] += alpha
    else:
        counts[assignment] += 1
    assignments[i] = assignment
    
    
print(f"ASSIGNMENTS: {assignments.T.tolist()}")
print(f"COUNTS: {counts.T.tolist()}")
