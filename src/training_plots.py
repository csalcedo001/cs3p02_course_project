import argparse
from pathlib import Path
import os

import matplotlib.pyplot as plt
import pickle



### Parser

# Define parser
parser = argparse.ArgumentParser()

parser.add_argument('--model-dir0', type=str, required=True)
parser.add_argument('--model-dir1', type=str, required=True)
parser.add_argument('--model-name0', type=str, required=True)
parser.add_argument('--model-name1', type=str, required=True)
parser.add_argument('--output', type=str, required=True)

args = parser.parse_args()


# Get arguments
model_dirs = [args.model_dir0, args.model_dir1]
model_names = [args.model_name0, args.model_name1]

model_losses = {}
model_accuracy = {}
for i, model_name in enumerate(model_names):
    losses_path = os.path.join(model_dirs[i], 'losses.pkl')
    accuracy_path = os.path.join(model_dirs[i], 'accuracy.pkl')

    with open(losses_path, 'rb') as in_file:
        losses = pickle.load(in_file)

    with open(accuracy_path, 'rb') as in_file:
        accuracy = pickle.load(in_file)
    
    model_losses[model_name] = losses
    model_accuracy[model_name] = accuracy



### Plot

# Make dir
savedir = args.output
Path(savedir).mkdir(parents=True, exist_ok=True)

# Plot training loss
loss_path = os.path.join(savedir, 'training_loss.png')

fig = plt.figure()
plt.title('Training loss')
for model_name in model_names:
    plt.plot(model_losses[model_name], label=model_name)
plt.ylabel('Loss')
plt.xlabel('Timestep')
plt.legend()
plt.savefig(loss_path)
plt.close(fig)


# Plot training accuracy
acc_path = os.path.join(savedir, 'training_acc.png')

fig = plt.figure()
plt.title('Training accuracy')
for model_name in model_names:
    plt.plot(model_accuracy[model_name], label=model_name)
plt.ylabel('Accuracy')
plt.xlabel('Timestep')
plt.legend()
plt.savefig(acc_path)
plt.close(fig)