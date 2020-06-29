<div align="center">

![Logo](images/logos/lightning_logo.svg)

# PyTorch Lightning
**The lightweight PyTorch wrapper for ML researchers. Scale your models. Write less boilerplate.**

## PyTorch Lightning Template
**This repository is PyTorch Lightning template for MNIST Classifier problem**
</div>

---  
## What do I do ?
- Add learning rate scheduler and logger
- Add custom callback class
- Add early stopping callback
- Add Model Checkpoint
- Add TensorBoard for visualisation metric
- Show how to training, validation, testing, and inference the model


## Refactoring your PyTorch code + benefits + full walk-through
[![Watch the video](images/general/tutorial_cover.jpg)](https://www.youtube.com/watch?v=QHww1JH7IDU)

## What is it?
[READ THIS QUICK START PAGE](https://pytorch-lightning.readthedocs.io/en/stable/new-project.html)

Lightning is a way to organize your PyTorch code to decouple the science code from the engineering.
It's more of a PyTorch style-guide than a framework. 

In Lightning, you organize your code into 3 distinct categories:

1. Research code (goes in the LightningModule).
2. Engineering code (you delete, and is handled by the Trainer).
3. Non-essential research code (logging, etc... this goes in Callbacks).

Here's an example of how to refactor your research code into a [LightningModule](https://pytorch-lightning.readthedocs.io/en/latest/lightning-module.html).

![PT to PL](images/lightning_module/pt_to_pl.png)

The rest of the code is automated by the [Trainer](https://pytorch-lightning.readthedocs.io/en/latest/trainer.html)!
![PT to PL](images/lightning_module/pt_trainer.png)

## What does lightning control for me?

Everything in Blue!
This is how lightning separates the science (red) from engineering (blue).

![Overview](images/general/pl_overview.gif)

## Why do I want to use lightning?
Although your research/production project might start simple, once you add things like GPU AND TPU training, 16-bit precision, etc, you end up spending more time engineering than researching. Lightning automates AND rigorously tests those parts for you.
