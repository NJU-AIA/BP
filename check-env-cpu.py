import torch

print("PyTorch 版本:", torch.__version__)

# 测试张量运算
try:
    x = torch.rand(3, 3)
    print("张量运算成功:\n", x)
except Exception as e:
    print("张量运算失败:", e)