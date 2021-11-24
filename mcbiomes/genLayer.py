from copy import deepcopy
import numpy as np

from javarandom import Random
from PIL import Image

import mcbiomes.GenLayerAddIsland as g3
import mcbiomes.GenLayerAddMushroomIsland as g8
import mcbiomes.GenLayerAddSnow as g6
import mcbiomes.GenLayerBiome as g11
import mcbiomes.GenLayerBiomeEdge as g12
import mcbiomes.GenLayerDeepOcean as g9
import mcbiomes.GenLayerEdge as g7
import mcbiomes.GenLayerHills as g13
import mcbiomes.GenLayerIsland as g1
import mcbiomes.GenLayerRareBiome as g16
import mcbiomes.GenLayerRemoveTooMuchOcean as g5
import mcbiomes.GenLayerRiver as g14
import mcbiomes.GenLayerRiverInit as g10
import mcbiomes.GenLayerRiverMix as g18
import mcbiomes.GenLayerShore as g17
import mcbiomes.GenLayerSmooth as g15
import mcbiomes.GenLayerVoronoiZoom as g19
import mcbiomes.GenLayerZoom as g4

from constants import COLOR_MAP


def getFeatureChunkInRegion(config, seed, regX, regZ):
    # https://github.com/Cubitect/cubiomes/blob/849839af55dc3650a00017368761d9189a2ea11a/finders.h#L718
    pos = []
    K = 0x5DEECE66D
    M = (1 << 48) - 1
    b = 0xB
    seed = seed + regX * 341873128712 + regZ * 132897987541 + config["salt"]
    seed = seed ^ K
    seed = (seed * K + b) & M
    r = config["chunkRange"]
    if r & (r - 1):
        pos.append(int(seed >> 17) % r)
        seed = (seed * K + b) & M
        pos.append(int(seed >> 17) % r)
    else:
        pos.append(int((r * (seed >> 17)) >> 31))
        seed = (seed * K + b) & M
        pos.append(int((r * (seed >> 17)) >> 31))
    return pos


def getFeaturePos(config, seed, regX, regZ):
    # https://github.com/Cubitect/cubiomes/blob/849839af55dc3650a00017368761d9189a2ea11a/finders.h#L757
    pos = getFeatureChunkInRegion(config, seed, regX, regZ)
    pos[0] = int((int(regX) * config["regionSize"] + pos[0]) << 4)
    pos[1] = int((int(regZ) * config["regionSize"] + pos[1]) << 4)
    return pos


def isSlimeChunk(seed, chunkX, chunkZ):
    # https://github.com/Cubitect/cubiomes/blob/849839af55dc3650a00017368761d9189a2ea11a/finders.h#L340
    rnd = seed
    rnd += int(chunkX * 0x5AC0DB)
    rnd += int(chunkX * chunkX * 0x4C1906)
    rnd += int(chunkZ * 0x5F24F)
    rnd += int(chunkZ * chunkZ) * 0x4307A7
    rnd ^= 0x3AD8025F
    random = Random(rnd)
    return random.nextInt(10) == 0


def getMineshafts(seed, cx0, cz0, cx1, cz1):
    # https://github.com/Cubitect/cubiomes/blob/71ca41e171749799978f3473a052427c9b9f9c96/finders.c#L268
    random = Random(seed)
    a = random.nextLong()
    b = random.nextLong()
    out = []
    for i in range(cx0, cx1):
        aix = i * a ^ seed
        for j in range(cz0, cz1):
            random = Random(aix ^ j * b)
            if random.nextDouble() < 0.004:
                x = i << 4
                z = j << 4
                out.append([x, z])
    return out


def getImage(ints, aW, aH) -> Image.Image:
    ints = np.split(ints, aW)
    image = Image.new("RGB", (aW, aH))
    for x, line in enumerate(ints):
        for y, color in enumerate(line):
            image.putpixel((x, y), tuple(COLOR_MAP[color]))
    return image


def genlayer(seed, customized=[0]):
    # customized hold 0 for normal, 1 for large and 2 for fully cuztomized, 4 for default1.1, then it holds biomeSize and river size then chunk composition

    # first stack from 1:4096 to 1:256
    initialLayer = g1.GenLayerIsland(1)
    firstLayer = g4.GenLayerZoom(2000, initialLayer, 1, 1, 1)
    secondLayer = g3.GenLayerAddIsland(1, firstLayer, 1)
    thirdLayer = g4.GenLayerZoom(2001, secondLayer, 0, 1, 1)
    genlayeraddisland1 = g3.GenLayerAddIsland(2, thirdLayer, 1)
    genlayeraddisland1 = g3.GenLayerAddIsland(50, genlayeraddisland1, 1)
    genlayeraddisland1 = g3.GenLayerAddIsland(70, genlayeraddisland1, 1)
    genlayerremovetoomuchocean = g5.GenLayerRemoveTooMuchOcean(2, genlayeraddisland1, 1)
    genlayeraddsnow = g6.GenLayerAddSnow(2, genlayerremovetoomuchocean, 1)
    genlayeraddisland2 = g3.GenLayerAddIsland(3, genlayeraddsnow, 1)
    genlayeredge = g7.GenLayerEdge(2, genlayeraddisland2, "COOL_WARM", 1)
    genlayeredge = g7.GenLayerEdge(2, genlayeredge, "HEAT_ICE", 1)
    genlayeredge = g7.GenLayerEdge(3, genlayeredge, "SPECIAL", 1)
    genlayerzoom1 = g4.GenLayerZoom(2002, genlayeredge, 0, 1, 1)
    genlayerzoom1 = g4.GenLayerZoom(2003, genlayerzoom1, 0, 1, 1)
    genlayeraddisland3 = g3.GenLayerAddIsland(4, genlayerzoom1, 1)
    genlayeraddmushroomisland = g8.GenLayerAddMushroomIsland(5, genlayeraddisland3, 1)
    genlayerdeepocean = g9.GenLayerDeepOcean(4, genlayeraddmushroomisland, 1)
    genlayerdeepocean.initWorldSeed(seed)
    # End first stack

    # choosing type of generation
    i, j = 4, 4
    if customized[0] == 2:
        i, j = customized[1], customized[2]
    if customized[0] == 1:
        i = 6
    # end of choice

    # starting biome stack
    lvt81 = g11.GenLayerBiome(200, genlayerdeepocean, customized, 0)  # 19
    genlayer6 = g4.GenLayerZoom(1000, lvt81, 0, 1, 1)  # 20
    genlayer6 = g4.GenLayerZoom(1001, genlayer6, 0, 1, 1)  # 21
    genlayerbiomeedge = g12.GenLayerBiomeEdge(1000, genlayer6, 1)  # 22
    # end Biome stack

    # starting river stack
    genlayerriverinit = g10.GenLayerRiverInit(100, genlayerdeepocean, 0)  # 23
    lvt91_b = g4.GenLayerZoom(1000, genlayerriverinit, 0, 1, 1)  # 25
    lvt91 = g4.GenLayerZoom(1001, lvt91_b, 0, 1, 1)  # 20 and 21
    # merge point
    genlayerriver = deepcopy(lvt91)  # copy of 25 aka 36

    # merging and starting hills/rare/shore/smooth chain
    genlayerhills = g13.GenLayerHills(1000, genlayerbiomeedge, lvt91, 1)
    genlayerhills = g16.GenLayerRareBiome(1001, genlayerhills, 1)
    for k in range(i):
        genlayerhills = g4.GenLayerZoom(1000 + k, genlayerhills, 0, 1, 1)
        if not k:
            genlayerhills = g3.GenLayerAddIsland(3, genlayerhills, 1)
        if k == 1 or i == 1:
            genlayerhills = g17.GenLayerShore(1000, genlayerhills, 1)
    genlayersmooth1 = g15.GenLayerSmooth(1000, genlayerhills, 1)
    # end of biome chain

    # finishing river
    genpreriver = g4.GenLayerZoom.magnify(1000, genlayerriverinit, 2, 0, 1, 1)
    genlayer5 = g4.GenLayerZoom.magnify(1000, genpreriver, j, 0, 1, 1)  # 37,38,39,40
    genlayerriver = g14.GenLayerRiver(1, genlayer5, 1)
    genlayersmooth = g15.GenLayerSmooth(1000, genlayerriver, 1)  # 42
    # end river

    # merging river with biome
    genlayerrivermix = g18.GenLayerRiverMix(100, genlayersmooth1, genlayersmooth, 1)
    # zooming
    genlayer3 = g19.GenLayerVoronoiZoom(10, genlayerrivermix, 1)
    # initializing
    genlayer3.initWorldSeed(seed)
    last = genlayer3
    return last


def matchBiomes(self, master, indice, customized):
    seed, biomeId, px, pz = master[indice]

    genlayerFinal = self.genlayer(seed, customized)
    lr = genlayerFinal.getInts(px, pz, 1, 1)

    if biomeId == lr[0]:
        return True
    print(lr, master[indice])
    return False


def multiple():
    customized = [0, "", "", [""]]
    seed = 541515181818
    genlayerFinal = genlayer(seed, customized)

    size = 16
    r = Random(4227552225777)
    print("{", end="")
    for i in range(size):
        for j in range(size):
            x = r.nextInt(512)
            z = r.nextInt(512)
            map = genlayerFinal.getInts(x, z, 1, 1)
            print("{{{0}, {1}, {2}}}, ".format(x, z, map[0]), end="")
    print("};")


def one():
    customized = [0, "", "", [""]]
    seed = 541515181818
    genlayerFinal = genlayer(seed, customized)
    x = 171
    z = 497
    map = genlayerFinal.getInts(x, z, 1, 1)
    print("{{{0}, {1}, {2}}}, ".format(x, z, map[0]), end="\n")


if __name__ == "__main__":
    multiple()
    # one()
