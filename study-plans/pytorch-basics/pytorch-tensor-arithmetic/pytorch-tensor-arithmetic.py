import torch

def tensor_op(x: torch.Tensor, y: torch.Tensor, op: str) -> torch.Tensor:
    if op == "add":
        return x + y 
    elif op == "matmul":
        return x @ y 
    elif op == "power":
        return x ** y 
    elif op == "multiply":
        return x * y 
    else:
        return torch.maximum(x,y)