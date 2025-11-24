#crea un array numpy utilizzaindo arange e vorifica il tipo di dato (dtype) e la forma (shape) dell'array
import numpy as np

arr = np.arange(11,50)

print(arr)
print(f"il tipo è {arr.dtype}")

arr.dtype = np.float64

print(f"il tipo è {arr.dtype}")
print(f"lo shape è {arr.shape}")


