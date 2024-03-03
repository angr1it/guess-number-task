import torch
from torch import nn

version = torch.__version__


def create_model():
    # Linear layer mapping from 784 features, so it should be 784->256->16->10

    # your code here

    # return model instance (None is just a placeholder)

    model = nn.Sequential(
        nn.Linear(784, 256, bias=True),
        nn.ReLU(),
        nn.Linear(256, 16, bias=True),
        nn.ReLU(),
        nn.Linear(16, 10, bias=True),
    )

    return model


def count_parameters(model):
    # your code here
    # return integer number (None is just a placeholder)

    return sum(p.numel() for p in model.parameters())
