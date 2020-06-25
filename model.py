import torch
import pytorch_lightning as pl
import os

from torch import nn
from torch.nn import functional as F
from torch.utils.data import TensorDataset, DataLoader, random_split
from torchvision.datasets import MNIST
from torchvision import datasets, transforms

from pytorch_lightning.callbacks import EarlyStopping, LearningRateLogger, ModelCheckpoint


class LightningMNISTClassifier(pl.LightningModule):

  def __init__(self, lr_rate):
    super(LightningMNISTClassifier, self).__init__()
    
    # mnist images are (1, 28, 28) (channels, width, height) 
    self.layer_1 = torch.nn.Linear(28 * 28, 128)
    self.layer_2 = torch.nn.Linear(128, 256)
    self.layer_3 = torch.nn.Linear(256, 10)
    self.lr_rate = lr_rate

  def forward(self, x):
      batch_size, channels, width, height = x.size()
      
      # (b, 1, 28, 28) -> (b, 1*28*28)
      x = x.view(batch_size, -1)

      # layer 1 (b, 1*28*28) -> (b, 128)
      x = self.layer_1(x)
      x = torch.relu(x)

      # layer 2 (b, 128) -> (b, 256)
      x = self.layer_2(x)
      x = torch.relu(x)

      # layer 3 (b, 256) -> (b, 10)
      x = self.layer_3(x)

      # probability distribution over labels
      x = torch.softmax(x, dim=1)

      return x

  def cross_entropy_loss(self, logits, labels):
    return F.nll_loss(logits, labels)

  def training_step(self, train_batch, batch_idx):
      x, y = train_batch
      logits = self.forward(x)
      loss = self.cross_entropy_loss(logits, y)

      logs = {'train_loss': loss}
      return {'loss': loss, 'log': logs}

  def validation_step(self, val_batch, batch_idx):
      x, y = val_batch
      logits = self.forward(x)
      loss = self.cross_entropy_loss(logits, y)
      return {'val_loss': loss}

  def test_step(self, val_batch, batch_idx):
      x, y = val_batch
      logits = self.forward(x)
      loss = self.cross_entropy_loss(logits, y)
      return {'test_loss': loss}

  def validation_epoch_end(self, outputs):
      avg_loss = torch.stack([x['val_loss'] for x in outputs]).mean()
      tensorboard_logs = {'val_loss': avg_loss}
      return {'avg_val_loss': avg_loss, 'log': tensorboard_logs}

  def test_epoch_end(self, outputs):
      avg_loss = torch.stack([x['test_loss'] for x in outputs]).mean()
      tensorboard_logs = {'test_loss': avg_loss}
      return {'avg_test_loss': avg_loss, 'log': tensorboard_logs}

  def configure_optimizers(self):
    optimizer = torch.optim.Adam(self.parameters(), lr=self.lr_rate)
    lr_scheduler = {'scheduler': torch.optim.lr_scheduler.ExponentialLR(optimizer, gamma = 0.95),
                    'name': 'expo_lr'}
    return [optimizer], [lr_scheduler]
