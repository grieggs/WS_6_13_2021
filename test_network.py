import torch
import torchvision
import torchvision.transforms as transforms
from net import Net
import torch.optim as optim
import torch.nn as nn
import torch.nn.functional as F
import os
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

# def imshow(img, preds = None):
#     # img = img / 2 + 0.5  # unnormalize
#     npimg = img
#     plt.imshow(npimg)
#     plt.show()

def imshow(img,probs=None):
    if probs is not None:
        fig, axs = plt.subplots(2)
        img = img / 2 + 0.5     # unnormalize
        npimg = img.numpy()
        axs[0].imshow(np.transpose(npimg, (1, 2, 0)))
        axs[1].bar(list(range(0,10)),probs.detach().numpy())
        axs[1].set_xticks(np.arange(0, 10, 1.0))
        plt.show()


print(os.getcwd())
net = torch.load("net.pt")

test = Image.open("data\\MNIST\\3.jpg")

transform = transforms.Compose(
        [transforms.ToTensor(),
         transforms.Normalize(0.5, 0.5, 0.5)])
test = transform(test)
test = torch.unsqueeze(test, dim=0)

probs = net(test)
print(probs)
imshow(test[0],probs[0])
