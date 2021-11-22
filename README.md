# MCBiomes
## Installation
```bash
pip install https://github.com/vyakl110011/MCBiomes/archive/refs/heads/master.zip
```
## Base usage (get chunk data, see [https://github.com/toolbox4minecraft/amidst/wiki/Biome-Color-Table](https://github.com/toolbox4minecraft/amidst/wiki/Biome-Color-Table))
```python
from mcbiomes import genLayer as gl

layer = gl.genLayer()
print(layer.getInts())
```