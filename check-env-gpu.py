import torch

print("PyTorch 版本:", torch.__version__)

# 测试张量运算
try:
    x = torch.rand(3, 3)
    print("张量运算成功:\n", x)
except Exception as e:
    print("张量运算失败:", e)
    
# 检测 CUDA
print("CUDA 可用:", torch.cuda.is_available())
if torch.cuda.is_available():
    print("CUDA 版本:", torch.version.cuda)
    print("GPU 名称:", torch.cuda.get_device_name(0))