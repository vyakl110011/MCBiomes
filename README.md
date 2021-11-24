# MCBiomes
## Installation
```bash
pip install -U https://github.com/vyakl110011/MCBiomes/archive/refs/heads/master.zip
```
## Base usage (get chunk data, see [Biome-Color-Table](https://github.com/toolbox4minecraft/amidst/wiki/Biome-Color-Table))
```python
from mcbiomes import genLayer as gl

layer = gl.genlayer(seed=12345)
print(layer.getInts(aX=0, aY=0, aW=16, aH=16))
```
## Specificate biome type
```python
from mcbiomes import genLayer as gl

layer = gl.genlayer(seed=12345, customized=[2, 4, 6]) # customized hold 0 for normal, 1 for large and 2 for fully cuztomized, 4 for default1.1, then it holds biomeSize and river size then chunk composition
print(layer.getInts(aX=0, aY=0, aW=16, aH=16))
```
## Generate image
```python
from mcbiomes import genLayer as gl

layer = gl.genlayer(seed=12345)
image = gl.getImage(ints=layer.getInts(aX=0, aY=0, aW=512, aH=512), aW=512, aH=512)
image.save("image.jpg")
```
## Telegram
-  https://t.me/code_writing_machine
