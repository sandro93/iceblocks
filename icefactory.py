from block import Block
import itertools
from consts import WINDOW_H, WINDOW_W


def flatten(listOfLists):
    "Flatten one level of nesting"
    return itertools.chain.from_iterable(listOfLists)


class Row:
    def __init__(self, numblocks, startpos, blockw):
        x, y = startpos
        positions = [(x + i * blockw, y) for i in range(numblocks)]
        self.blocks = [Block(*p) for p in positions]


class Level:
    def __init__(self, rows):
        nestedBlocks = [row.blocks for row in rows]
        self.blocks = flatten(nestedBlocks)


class BlockFactory:
    def __init__(self):
        self.levels = ((10, 9, 8, 9, 10), (10, 9, 8, 9, 10),
                       (10, 9, 8, 9, 10), (10, 9, 8, 9, 10), (10, 9, 8, 9, 10))

    def get_level(self, n):
        block = Block(1, 1)
        blockw = block.width
        voffset = 40

        rows = []
        blockNums = self.levels[n]
        i = 1
        for n in blockNums:
            startpos = ((WINDOW_W - n * blockw) / 2, WINDOW_H - i * voffset)
            rows.append(Row(n, startpos, blockw))
            i += 1
        return Level(rows)
