import numpy as np
import argparse
from utils.crp import CRP

parser = argparse.ArgumentParser()
parser.add_argument("-N", type=int, default=10)
parser.add_argument("-alpha", type=float, default=0.05)
args = parser.parse_args()

N = args.N
alpha = args.alpha

print(f"Running with N={N} and alpha={alpha}")

crp = CRP(alpha)
for i in range(1, N):
    crp.seat()

print(f"NUM CLUSTERS: {len(crp.tables)}")
print(f"COUNTS: {crp.tables}")
