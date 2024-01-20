from torch import nn


class Classifier(nn.Module):
    def __init__(self):
        super().__init__()
        """
        [TODO]: the classifier should be implemented by the students and different variations of it can be tested
        in order to understand which is the most performing one """
        self.classifier= nn. Sequential(
        nn.Linear(1024, 512),
        nn.ReLU(),
        nn.Dropout(0.5),
        nn.Linear(512, 512),
        nn.ReLU(),
        nn.Dropout(0.5),
        nn.Linear(512, 8))

    def forward(self, x):
      return self.classifier(x), {}

