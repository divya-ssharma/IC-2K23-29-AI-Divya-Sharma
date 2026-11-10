import torch
import torch.nn as nn
import matplotlib.pyplot as plt

X = torch.tensor([[1.0], [2.0], [3.0], [4.0], [5.0], [6.0], [7.0], [8.0]])
y = torch.tensor([[3.0], [5.0], [7.0], [9.0], [11.0], [13.0], [15.0], [17.0]])

# X = torch.tensor([1,2,3,4,5,6,7,8]).float().unsqueeze(1)

model = nn.Linear(1, 1)
loss_fn = nn.MSELoss()
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)

losses = []

for epoch in range(200):
    pred = model(X)
    loss = loss_fn(pred, y)

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    losses.append(loss.item())

    if epoch % 50 == 0:
        print(epoch, loss.item())

print(model.weight.item(), model.bias.item())

plt.plot(losses)
plt.savefig('loss.png')
plt.close()

with torch.no_grad():
    pred = model(X)

plt.scatter(X.numpy(), y.numpy())
plt.plot(X.numpy(), pred.numpy())
plt.savefig('fit.png')
plt.close()
