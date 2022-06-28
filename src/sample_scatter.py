import argparse
from pathlib import Path
import json
import os

import numpy as np
import matplotlib.pyplot as plt


# Define parser
parser = argparse.ArgumentParser()

parser.add_argument('--input', type=str, required=True)
parser.add_argument('--output', type=str, required=True)


# Parse arguments
args = parser.parse_args()

# Make sure path exists
Path(args.output).mkdir(parents=True, exist_ok=True)

with open(args.input) as in_file:
    data = json.load(in_file)

title = ['train', 'test']
for i, (x, y) in enumerate(data):
    x = np.array(x)
    y = np.array(y)
    
    filename = 'sample_scatter_{}.png'.format(title[i])
    filepath = os.path.join(args.output, filename)

    fig = plt.figure()
    plt.scatter(x[:,0], x[:,1], c=y)
    plt.savefig(filepath)
    plt.close(fig)
