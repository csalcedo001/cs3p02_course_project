import torch
import torch.nn as nn


class SimpleNet(nn.Module):
    def __init__(self, n_x, n_y, n_hs:list):
        super().__init__()
    
        sizes = [n_x] + n_hs + [n_y]
        n_l = len(sizes)

        layers = []
        for i in range(n_l - 2):
            layers.append(nn.Linear(sizes[i], sizes[i + 1]))
            layers.append(nn.ReLU())
        
        layers.append(nn.Linear(sizes[-2], sizes[-1]))
        layers.append(nn.Sigmoid())

        self.model = nn.Sequential(*layers)
    
    def forward(self, x):
        y_hat = self.model(x)
        return y_hat