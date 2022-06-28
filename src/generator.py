import argparse
from pathlib import Path
import random
import json

parser = argparse.ArgumentParser()

parser.add_argument('--out', type=str, required=True)

args = parser.parse_args()

Path(args.out).parent.mkdir(parents=True, exist_ok=True)

json.dump([random.randint(0, 100) for _ in range(5)], open(args.out, 'w'))