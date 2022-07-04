import argparse
from pathlib import Path
import json
import pickle
import os

import torch
import torch.nn as nn
import torch.optim as optim
from tqdm import tqdm
import matplotlib.pyplot as plt

from model import SimpleNet



### Parser

# Define parser
parser = argparse.ArgumentParser()

parser.add_argument('--input', type=str, required=True)
parser.add_argument('--output', type=str, required=True)
parser.add_argument('--dims', type=int, default=1000)
parser.add_argument('--model', type=str, default='simplenet')
parser.add_argument('--size_hidden', type=int, default=16)
parser.add_argument('--num_hidden', type=int, default=1)
parser.add_argument('--epochs', type=int, default=5)

args = parser.parse_args()



### Data

# Get training data
with open(args.input, 'r') as in_file:
    data = json.load(in_file)

(x_train, y_train), (_, _) = data

# Preprocess training data
x_train = torch.Tensor(x_train).float()
y_train = torch.unsqueeze(torch.Tensor(y_train), axis=1).float()



### Model

# Get model parameters
n_h = args.size_hidden
n_l = args.num_hidden + 2
n_hs = [n_h for _ in range(n_l)]

# Initialize model
if args.model == 'simplenet':
    model = SimpleNet(
        n_x=args.dims,
        n_y=1,
        n_hs=n_hs)
else:
    raise Exception("Unknown model '{}'".format(args.model))
    
model.train()



### Training

# Training setup
optimizer = optim.Adam(model.parameters())
criterion = nn.BCELoss()

losses = []
accuracy = []


# Training loop
print("Starting training for '{}'".format(args.model))
for epoch in tqdm(range(args.epochs)):
    y_hat = model(x_train)
    loss = criterion(y_hat, y_train)

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    losses.append(loss.item())

    # Compute accuracy
    acc = torch.sum(torch.round(y_hat) == y_train)
    accuracy.append(acc)



### Results

# Make dir
savedir = args.output
Path(savedir).mkdir(parents=True, exist_ok=True)

# Save model
model_path = os.path.join(savedir, 'model.pt')
torch.save(model.state_dict(), model_path)

# Save losses
losses_path = os.path.join(savedir, 'losses.pkl')
with open(losses_path, 'wb') as out_dir:
    pickle.dump(losses, out_dir)

# Save accuracy
accuracy_path = os.path.join(savedir, 'accuracy.pkl')
with open(accuracy_path, 'wb') as out_dir:
    pickle.dump(accuracy, out_dir)