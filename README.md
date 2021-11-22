# MCBiomes
## Installation
```bash
pip install -U https://github.com/vyakl110011/MCBiomes/archive/refs/heads/master.zip
```
## Base usage (get chunk data, see [https://github.com/toolbox4minecraft/amidst/wiki/Biome-Color-Table](https://github.com/toolbox4minecraft/amidst/wiki/Biome-Color-Table))
```python
from mcbiomes import genLayer as gl

seed = 12345
layer = gl.genlayer(seed)
print(layer.getInts())
```