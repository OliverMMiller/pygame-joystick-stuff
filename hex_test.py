def hexagon(pos):
        x, y = map(abs, pos)
        return y < 3**0.5 * min(s - x, s / 2)


s = int(input("radius: "))


for y in range(-s, s+1):
    print(''.join('⬜⬛'[hexagon((x, y))] for x in range(-s, s+1)))

#
