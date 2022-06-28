import argparse
from pathlib import Path
import random
import json


# Define parser
parser = argparse.ArgumentParser()

parser.add_argument('--out', type=str, required=True)
parser.add_argument('--min', type=int, default=0)
parser.add_argument('--max', type=int, default=100)
parser.add_argument('--num', type=int, default=5)


# Parse arguments
args = parser.parse_args()

# Make sure path exists
Path(args.out).parent.mkdir(parents=True, exist_ok=True)

# Generate data
data = [random.randint(args.min, args.max) for _ in range(args.num)]

# Save data
with open(args.out, 'w') as out_file:
    json.dump(data, out_file)