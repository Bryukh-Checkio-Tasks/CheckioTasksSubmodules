from fractions import Fraction as frac

def checkio(*data):
    xw1 = frac(data[0][0])
    yw1 = frac(data[0][1])
    xw2 = frac(data[1][0])
    yw2 = frac(data[1][1])
    xa = frac(data[2][0])
    ya = frac(data[2][1])
    xb = frac(data[3][0])
    yb = frac(data[3][1])
    if data[2] == data[3]:
        return -1
 
    #Ax+By+C=0
    dxw, dyw = xw2 - xw1, yw2 - yw1
    awall, bwall, cwall = dyw, -dxw, dxw * yw1 - dyw * xw1
    dxba, dyba = xb - xa, yb - ya
    abull, bbull, cbull = dyba, -dxba, dxba * ya - dyba * xa
    try:
        if bwall:
            x = (bbull * cwall / bwall - cbull) / (abull - bbull * awall / bwall)
            y = -1 * (awall * x + cwall) / bwall
        else:
            x = -1 * cwall / awall
            y = -1 * (abull * x + cbull) / bbull
    except ZeroDivisionError: #parallel
        #check if bullet line and wall line is same
        if bwall and bbull:
            cwall = cwall / bwall
            cbull = cbull / bbull
        else:
            cwall = cwall / awall
            cbull = cbull / abull
        if cwall == cbull:
            if min(xw1, xw2) <= xa <= max(xw1, xw2) and min(yw1, yw2) <= ya <= max(yw1, yw2):
                return True
 
            x, y = xw1, yw1 #shoot in end of wall
        else:
            return -1, None #parallell
        #check if x,y in wall
    mx, my = (xw1 + xw2) / 2, (yw1 + yw2) / 2
    dist = ((mx - x) ** 2 + (my - y) ** 2) ** 0.5
    wdist = ((mx - xw1) ** 2 + (my - yw1) ** 2) ** 0.5
    if min(xw1, xw2) <= x <= max(xw1, xw2) and min(yw1, yw2) <= y <= max(yw1, yw2):
        #check direction
        if min(x, xa) <= xb <= max(x, xa) and min(y, ya) <= yb <= max(y, ya):
            pass
        elif min(xa, xb) <= x <= max(xb, xa) and min(yb, ya) <= y <= max(yb, ya):
            pass
        else:
            return -1, None
    if dist > wdist:
        return -1, [float(x), float(y)]
    else:
        return 100 - round((dist / wdist) * 100), [float(x), float(y)]

T = [
    ((2, 2), (5, 7), (11, 2), (8, 3)),
    ((2, 2), (5, 7), (11, 2), (7, 2)),
    ((2, 2), (5, 7), (11, 2), (8, 4)),
    ((2, 2), (5, 7), (11, 2), (9, 5)),
    ((2, 2), (5, 7), (11, 2), (10.5, 3)),

    ((2, 2), (5, 7), (8, 3), (11, 2)),
    ((1, 1), (99, 99), (99, 1), (41, 39)),
    ((10, 10), (10, 90), (50, 90), (50, 50)),
    ((10, 10), (10, 90), (50, 60), (70, 60)),
    ((10, 10), (10, 90), (70, 60), (50, 60)),
    ((2, 2), (10, 2), (5, 10), (5, 5)),
    ((2, 2), (10, 2), (5, 10), (3, 5)),
    ((2, 2), (10, 2), (5, 10), (4, 5)),
    ((2, 10), (10, 2), (10, 10), (3, 10)),
    ((2, 10), (10, 2), (10, 10), (10, 4)),
    ((2, 10), (10, 2), (10, 10), (3, 10.1)),
    ((2, 10), (10, 2), (10, 10), (3, 9.9)),
]

for t in T:
    ans, ex = checkio(*t)
    print("""{{
    "input": {},
    "answer": {},
    "explanation": {}
    }},""".format(t, ans, ex))