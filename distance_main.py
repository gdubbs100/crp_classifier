import numpy as np
import argparse
from utils.crp import DCRP
from sklearn.datasets import load_iris

parser = argparse.ArgumentParser()
parser.add_argument("-alpha", type=float, default=0.05)
args = parser.parse_args()

alpha = args.alpha

iris_data = load_iris()
dcrp = DCRP(alpha)
print(f"running with {alpha}")
for row in iris_data['data']:
    dcrp.seat(row)

print(f"NUM CLUSTERS: {len(crp.tables)}")
print(f"COUNTS: {crp.tables}")
