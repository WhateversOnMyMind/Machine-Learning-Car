points = [
    (520, 466), (520, 537), (533, 466), (533, 537), (550, 466), (550, 535), (575, 466), (576, 532), (605, 464), (610, 535),
    (643, 462), (646, 528), (674, 460), (682, 528), (705, 456), (712, 526),
    (729, 450), (742, 518), (752, 443), (790, 499), (782, 422), (819, 482),
    (804, 406), (848, 462), (834, 388), (879, 438), (849, 365), (913, 400),
    (862, 327), (932, 341), (874, 295), (946, 302), (881, 256), (952, 266),
    (883, 220), (956, 223), (882, 184), (950, 171), (862, 149), (920, 109),
    (831, 125), (864, 64), (794, 110), (807, 42), (756, 104), (756, 38),
    (713, 106), (700, 39), (685, 123), (641, 72), (667, 146), (611, 104),
    (650, 178), (594, 139), (633, 203), (577, 166), (611, 234), (563, 182),
    (563, 258), (543, 186), (505, 263), (502, 193), (457, 260), (458, 191),
    (397, 238), (426, 176), (350, 205), (395, 154), (319, 175), (360, 120),
    (288, 145), (327, 85), (255, 120), (282, 55), (223, 115), (226, 43),
    (188, 117), (173, 48), (156, 130), (124, 69), (118, 153), (78, 99),
    (103, 191), (34, 172), (95, 225), (29, 217), (90, 266), (19, 264),
    (90, 305), (16, 305), (96, 340), (24, 353), (109, 375), (45, 406),
    (139, 403), (87, 457), (177, 420), (137, 483), (220, 436), (186, 496),
    (258, 441), (257, 509), (317, 446), (312, 515), (359, 450), (354, 514),
    (416, 462), (401, 532), (465, 475), (466, 536)
]

def make_quads(i):
    # 2개씩 점이 겹치면서 4개씩 묶기: [i, i+1, i+3, i+2]
    quad = [points[i], points[i+1], points[i+3], points[i+2]]
    return quad
