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
x = 0
y = 0
width = 16
height = 16
print(layer.getInts(x, y, width, height))
```