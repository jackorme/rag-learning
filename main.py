#语法 for a, b in zip(x,y)
#     x, y in enumerate(z)
#     [if for]
#     {a:b for}
#    [:,1::2]
import torch
scores = torch.tensor([[1,2,3],[4,5,6],[7,8,9]])
x = scores[:, -2:]
print(x)
