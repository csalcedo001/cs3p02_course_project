import argparse
from pathlib import Path
import json

import numpy as np


class XORSampler():
    def __init__(self, dims=2):
        self.dims = dims

    def sample(self, num):
        points = np.random.uniform(0, 1, [num, self.dims])
        labels = np.sum(np.round(points), axis=1) % 2

        return points.tolist(), labels.tolist()


# Define parser
parser = argparse.ArgumentParser()

parser.add_argument('--out', type=str, required=True)
parser.add_argument('--dims', type=int, default=2)
parser.add_argument('--train_size', type=int, default=1000)
parser.add_argument('--test_size', type=int, default=100)


# Parse arguments
args = parser.parse_args()

# Make sure path exists
Path(args.out).parent.mkdir(parents=True, exist_ok=True)

# Generate data
xor_sampler = XORSampler(dims=args.dims)

train = xor_sampler.sample(args.train_size)
test = xor_sampler.sample(args.test_size)
data = [train, test]

# Save data
with open(args.out, 'w') as out_file:
    json.dump(data, out_file)