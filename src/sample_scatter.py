import argparse
from pathlib import Path
import json

import matplotlib.pyplot as plt


# Define parser
parser = argparse.ArgumentParser()

parser.add_argument('--in', type=str, required=True)
parser.add_argument('--out', type=str, required=True)
parser.add_argument('--train_size', type=int, default=1000)
parser.add_argument('--test_size', type=int, default=100)
parser.add_argument('--batch_size', type=int, default=32)
parser.add_argument('--dims', type=int, default=2)

xor_sampler = XORSampler(
    batch_size=100)

x, y = xor_sampler.sample()

fig = plt.figure()
plt.scatter(x[:,0], x[:,1], c=y)
plt.savefig('sample_scatter.png')
plt.close(fig)
