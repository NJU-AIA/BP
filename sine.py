import torch
import torch.nn as nn
import math

# 1. dataset


# 2. model


# 3. loss & optimizer


# 4. optimizer


# 5. train loop
for t in range(10000):
    # 5.1 forward pass

    # 5.2 compute loss

    # 5.3 backpropagation

    # 5.4 gradient update

# results
w = model.weight.data[0]
b = model.bias.data.item()
print(f"y = {b:.4f} + {w[0]:.4f}x + {w[1]:.4f}x^2 + {w[2]:.4f}x^3")
