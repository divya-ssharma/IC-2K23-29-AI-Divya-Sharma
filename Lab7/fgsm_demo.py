import torch
import torch.nn as nn
import torch.nn.functional as F

class SmallNet(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear(10, 16)
        self.fc2 = nn.Linear(16, 2)

    def forward(self, x):
        x = F.relu(self.fc1(x))
        return self.fc2(x)

torch.manual_seed(3)
model = SmallNet()
model.eval()

x = torch.randn(1, 10, requires_grad=True)
target = torch.tensor([1])

# 0.3 too big

epsilon = 0.1

out = model(x)
loss = F.cross_entropy(out, target)
model.zero_grad()
loss.backward()

x_adv = x + epsilon * x.grad.sign()

print(model(x).argmax().item(), model(x_adv).argmax().item())
