COLOR_MAP = {
    0: [0, 0, 112],
    1: [141, 179, 96],
    2: [250, 148, 24],
    3: [96, 96, 96],
    4: [5, 102, 33],
    5: [11, 102, 89],
    6: [7, 249, 178],
    7: [0, 0, 255],
    8: [191, 59, 59],
    9: [128, 128, 255],
    10: [112, 112, 214],
    11: [160, 160, 255],
    12: [255, 255, 255],
    13: [160, 160, 160],
    14: [255, 0, 255],
    15: [160, 0, 255],
    16: [250, 222, 85],
    17: [210, 95, 18],
    18: [34, 85, 28],
    19: [22, 57, 51],
    20: [114, 120, 154],
    21: [83, 123, 9],
    22: [44, 66, 5],
    23: [98, 139, 23],
    24: [0, 0, 48],
    25: [162, 162, 132],
    26: [250, 240, 192],
    27: [48, 116, 68],
    28: [31, 95, 50],
    29: [64, 81, 26],
    30: [49, 85, 74],
    31: [36, 63, 54],
    32: [89, 102, 81],
    33: [69, 79, 62],
    34: [80, 112, 80],
    35: [189, 178, 95],
    36: [167, 157, 100],
    37: [217, 69, 21],
    38: [176, 151, 101],
    39: [202, 140, 101],
    40: [128, 128, 255],
    41: [128, 128, 255],
    42: [128, 128, 255],
    43: [128, 128, 255],
    44: [0, 0, 172],
    45: [0, 0, 144],
    46: [32, 32, 112],
    47: [0, 0, 80],
    48: [0, 0, 64],
    49: [32, 32, 56],
    50: [64, 64, 144],
    127: [0, 0, 0],
    129: [181, 219, 136],
    130: [255, 188, 64],
    131: [136, 136, 136],
    132: [45, 142, 73],
    133: [51, 142, 129],
    134: [47, 255, 218],
    140: [180, 220, 220],
    149: [123, 163, 49],
    151: [138, 179, 63],
    155: [88, 156, 108],
    156: [71, 135, 90],
    157: [104, 121, 66],
    158: [89, 125, 114],
    160: [129, 142, 121],
    161: [109, 119, 102],
    162: [120, 152, 120],
    163: [229, 218, 135],
    164: [207, 197, 140],
    165: [255, 109, 61],
    166: [216, 191, 141],
    167: [242, 180, 141],
    168: [118, 142, 20],
    169: [59, 71, 10],
    170: [94, 56, 48],
    171: [221, 8, 8],
    172: [73, 144, 123],
    173: [64, 54, 54],
}

BIOMES = {
    "ocean": 0,
    0: "ocean",
    "plains": 1,
    1: "plains",
    "desert": 2,
    2: "desert",
    "mountains": 3,
    3: "mountains",
    "forest": 4,
    4: "forest",
    "taiga": 5,
    5: "taiga",
    "swamp": 6,
    6: "swamp",
    "river": 7,
    7: "river",
    "nether_wastes": 8,
    8: "nether_wastes",
    "the_end": 9,
    9: "the_end",
    "frozen_ocean": 10,
    10: "frozen_ocean",
    "frozen_river": 11,
    11: "frozen_river",
    "snowy_tundra": 12,
    12: "snowy_tundra",
    "snowy_mountains": 13,
    13: "snowy_mountains",
    "mushroom_fields": 14,
    14: "mushroom_fields",
    "mushroom_field_shore": 15,
    15: "mushroom_field_shore",
    "beach": 16,
    16: "beach",
    "desert_hills": 17,
    17: "desert_hills",
    "wooded_hills": 18,
    18: "wooded_hills",
    "taiga_hills": 19,
    19: "taiga_hills",
    "mountain_edge": 20,
    20: "mountain_edge",
    "jungle": 21,
    21: "jungle",
    "jungle_hills": 22,
    22: "jungle_hills",
    "jungle_edge": 23,
    23: "jungle_edge",
    "deep_ocean": 24,
    24: "deep_ocean",
    "stone_shore": 25,
    25: "stone_shore",
    "snowy_beach": 26,
    26: "snowy_beach",
    "birch_forest": 27,
    27: "birch_forest",
    "birch_forest_hills": 28,
    28: "birch_forest_hills",
    "dark_forest": 29,
    29: "dark_forest",
    "snowy_taiga": 30,
    30: "snowy_taiga",
    "snowy_taiga_hills": 31,
    31: "snowy_taiga_hills",
    "giant_tree_taiga": 32,
    32: "giant_tree_taiga",
    "giant_tree_taiga_hills": 33,
    33: "giant_tree_taiga_hills",
    "wooded_mountains": 34,
    34: "wooded_mountains",
    "savanna": 35,
    35: "savanna",
    "savanna_plateau": 36,
    36: "savanna_plateau",
    "badlands": 37,
    37: "badlands",
    "wooded_badlands_plateau": 38,
    38: "wooded_badlands_plateau",
    "badlands_plateau": 39,
    39: "badlands_plateau",
    "small_end_islands": 40,
    40: "small_end_islands",
    "end_midlands": 41,
    41: "end_midlands",
    "end_highlands": 42,
    42: "end_highlands",
    "end_barrens": 43,
    43: "end_barrens",
    "warm_ocean": 44,
    44: "warm_ocean",
    "lukewarm_ocean": 45,
    45: "lukewarm_ocean",
    "cold_ocean": 46,
    46: "cold_ocean",
    "deep_warm_ocean": 47,
    47: "deep_warm_ocean",
    "deep_lukewarm_ocean": 48,
    48: "deep_lukewarm_ocean",
    "deep_cold_ocean": 49,
    49: "deep_cold_ocean",
    "deep_frozen_ocean": 50,
    50: "deep_frozen_ocean",
    "the_void": 127,
    127: "the_void",
    "sunflower_plains": 129,
    129: "sunflower_plains",
    "desert_lakes": 130,
    130: "desert_lakes",
    "gravelly_mountains": 131,
    131: "gravelly_mountains",
    "flower_forest": 132,
    132: "flower_forest",
    "taiga_mountains": 133,
    133: "taiga_mountains",
    "swamp_hills": 134,
    134: "swamp_hills",
    "ice_spikes": 140,
    140: "ice_spikes",
    "modified_jungle": 149,
    149: "modified_jungle",
    "modified_jungle_edge": 151,
    151: "modified_jungle_edge",
    "tall_birch_forest": 155,
    155: "tall_birch_forest",
    "tall_birch_hills": 156,
    156: "tall_birch_hills",
    "dark_forest_hills": 157,
    157: "dark_forest_hills",
    "snowy_taiga_mountains": 158,
    158: "snowy_taiga_mountains",
    "giant_spruce_taiga": 160,
    160: "giant_spruce_taiga",
    "giant_spruce_taiga_hills": 161,
    161: "giant_spruce_taiga_hills",
    "gravelly_mountains+": 162,
    162: "gravelly_mountains+",
    "shattered_savanna": 163,
    163: "shattered_savanna",
    "shattered_savanna_plateau": 164,
    164: "shattered_savanna_plateau",
    "eroded_badlands": 165,
    165: "eroded_badlands",
    "modified_wooded_badlands_plateau": 166,
    166: "modified_wooded_badlands_plateau",
    "modified_badlands_plateau": 167,
    167: "modified_badlands_plateau",
    "bamboo_jungle": 168,
    168: "bamboo_jungle",
    "bamboo_jungle_hills": 169,
    169: "bamboo_jungle_hills",
    "soul_sand_valley": 170,
    170: "soul_sand_valley",
    "crimson_forest": 171,
    171: "crimson_forest",
    "warped_forest": 172,
    172: "warped_forest",
    "basalt_deltas": 173,
    173: "basalt_deltas",
}

LARGE_STRUCT = 1
CHUNK_STRUCT = 2

FEATURE_CONFIG = {
    "salt": 14357617,
    "regionSize": 32,
    "chunkRange": 24,
    "structType": "Feature",
    "properties": 0,
}
IGLOO_CONFIG_112 = {
    "salt": 14357617,
    "regionSize": 32,
    "chunkRange": 24,
    "structType": "Igloo",
    "properties": 0,
}
SWAMP_HUT_CONFIG_112 = {
    "salt": 14357617,
    "regionSize": 32,
    "chunkRange": 24,
    "structType": "Swamp_Hut",
    "properties": 0,
}
DESERT_PYRAMID_CONFIG_112 = {
    "salt": 14357617,
    "regionSize": 32,
    "chunkRange": 24,
    "structType": "Desert_Pyramid",
    "properties": 0,
}
JUNGLE_PYRAMID_CONFIG_112 = {
    "salt": 14357617,
    "regionSize": 32,
    "chunkRange": 24,
    "structType": "Jungle_Pyramid",
    "properties": 0,
}
OCEAN_RUIN_CONFIG_115 = {
    "salt": 14357621,
    "regionSize": 16,
    "chunkRange": 8,
    "structType": "Ocean_Ruin",
    "properties": 0,
}
SHIPWRECK_CONFIG_115 = {
    "salt": 165745295,
    "regionSize": 15,
    "chunkRange": 7,
    "structType": "Shipwreck",
    "properties": 0,
}
DESERT_PYRAMID_CONFIG = {
    "salt": 14357617,
    "regionSize": 32,
    "chunkRange": 24,
    "structType": "Desert_Pyramid",
    "properties": 0,
}
IGLOO_CONFIG = {
    "salt": 14357618,
    "regionSize": 32,
    "chunkRange": 24,
    "structType": "Igloo",
    "properties": 0,
}
JUNGLE_PYRAMID_CONFIG = {
    "salt": 14357619,
    "regionSize": 32,
    "chunkRange": 24,
    "structType": "Jungle_Pyramid",
    "properties": 0,
}
SWAMP_HUT_CONFIG = {
    "salt": 14357620,
    "regionSize": 32,
    "chunkRange": 24,
    "structType": "Swamp_Hut",
    "properties": 0,
}
OUTPOST_CONFIG = {
    "salt": 165745296,
    "regionSize": 32,
    "chunkRange": 24,
    "structType": "Outpost",
    "properties": 0,
}
VILLAGE_CONFIG = {
    "salt": 10387312,
    "regionSize": 32,
    "chunkRange": 24,
    "structType": "Village",
    "properties": 0,
}
OCEAN_RUIN_CONFIG = {
    "salt": 14357621,
    "regionSize": 20,
    "chunkRange": 12,
    "structType": "Ocean_Ruin",
    "properties": 0,
}
SHIPWRECK_CONFIG = {
    "salt": 165745295,
    "regionSize": 24,
    "chunkRange": 20,
    "structType": "Shipwreck",
    "properties": 0,
}
MONUMENT_CONFIG = {
    "salt": 10387313,
    "regionSize": 32,
    "chunkRange": 27,
    "structType": "Monument",
    "properties": LARGE_STRUCT,
}
MANSION_CONFIG = {
    "salt": 10387319,
    "regionSize": 80,
    "chunkRange": 60,
    "structType": "Mansion",
    "properties": LARGE_STRUCT,
}
RUINED_PORTAL_CONFIG = {
    "salt": 34222645,
    "regionSize": 40,
    "chunkRange": 25,
    "structType": "Ruined_Portal",
    "properties": 0,
}
RUINED_PORTAL_N_CONFIG = {
    "salt": 34222645,
    "regionSize": 25,
    "chunkRange": 15,
    "structType": "Ruined_Portal_N",
    "properties": 0,
}
TREASURE_CONFIG = {
    "salt": 10387320,
    "regionSize": 1,
    "chunkRange": 1,
    "structType": "Treasure",
    "properties": CHUNK_STRUCT,
}
MINESHAFT_CONFIG = {
    "salt": 0,
    "regionSize": 1,
    "chunkRange": 1,
    "structType": "Mineshaft",
    "properties": CHUNK_STRUCT,
}
FORTRESS_CONFIG_115 = {
    "salt": 0,
    "regionSize": 16,
    "chunkRange": 8,
    "structType": "Fortress",
    "properties": 0,
}
FORTRESS_CONFIG = {
    "salt": 30084232,
    "regionSize": 27,
    "chunkRange": 23,
    "structType": "Fortress",
    "properties": 0,
}
BASTION_CONFIG = {
    "salt": 30084232,
    "regionSize": 27,
    "chunkRange": 23,
    "structType": "Bastion",
    "properties": 0,
}
END_CITY_CONFIG = {
    "salt": 10387313,
    "regionSize": 20,
    "chunkRange": 9,
    "structType": "End_City",
    "properties": LARGE_STRUCT,
}
END_GATEWAY_CONFIG = {
    "salt": 40013,
    "regionSize": 1,
    "chunkRange": 1,
    "structType": "End_Gateway",
    "properties": CHUNK_STRUCT,
}
