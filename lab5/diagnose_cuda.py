import torch
import sys
import os

with open('diag.txt', 'w') as f:
    f.write(f"Python: {sys.version}\n")
    f.write(f"Torch: {torch.__version__}\n")
    f.write(f"CUDA available: {torch.cuda.is_available()}\n")
    if torch.cuda.is_available():
        f.write(f"CUDA version: {torch.version.cuda}\n")
        f.write(f"Device count: {torch.cuda.device_count()}\n")
        f.write(f"Device name: {torch.cuda.get_device_name(0)}\n")
    else:
        f.write("CUDA not available in Torch.\n")
    
    # Try to see if nvidia-smi exists
    import subprocess
    try:
        res = subprocess.check_output(['nvidia-smi', '-L'], stderr=subprocess.STDOUT, shell=True)
        f.write(f"GPU Hardware:\n{res.decode()}\n")
    except Exception as e:
        f.write(f"NVIDIA hardware check failed: {e}\n")
