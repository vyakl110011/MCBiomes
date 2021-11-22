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
## Specificate biome type
```python
from mcbiomes import genLayer as gl

seed = 12345
customized = [2, 4, 6] # customized hold 0 for normal, 1 for large and 2 for fully cuztomized, 4 for default1.1, then it holds biomeSize and river size then chunk composition
layer = gl.genlayer(seed, customized)
x = 0
y = 0
width = 16
height = 16
print(layer.getInts(x, y, width, height))
```
## My contacts
-  https://t.me/code_writing_machine