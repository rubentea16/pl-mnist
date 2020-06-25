<div align="center">

![Logo](images/logos/lightning_logo.svg)

# PyTorch Lightning
**The lightweight PyTorch wrapper for ML researchers. Scale your models. Write less boilerplate.**

## PyTorch Lightning Template
**This repository is PyTorch Lightning template for MNIST Classifier problem**
</div>

---  
## Refactoring your PyTorch code + benefits + full walk-through
[![Watch the video](docs/source/_images/general/tutorial_cover.jpg)](https://www.youtube.com/watch?v=QHww1JH7IDU)

## What is it?
[READ THIS QUICK START PAGE](https://pytorch-lightning.readthedocs.io/en/stable/new-project.html)

Lightning is a way to organize your PyTorch code to decouple the science code from the engineering.
It's more of a PyTorch style-guide than a framework. 

In Lightning, you organize your code into 3 distinct categories:

1. Research code (goes in the LightningModule).
2. Engineering code (you delete, and is handled by the Trainer).
3. Non-essential research code (logging, etc... this goes in Callbacks).
