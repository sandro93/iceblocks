from block import Block
import itertools
from consts import WINDOW_H

def flatten(listOfLists):
    "Flatten one level of nesting"
    return itertools.chain.from_iterable(listOfLists)

class Row:
    def __init__(self, numblocks, startpos,
            offset, blockw):
        x, y = startpos
        positions = [(offset + x + i * blockw, y) for i in range(1, numblocks)]
        self.blocks = [Block(*p) for p in positions]

class Level:
    def __init__(self, rows):
        nestedBlocks = [row.blocks for row in rows]
        self.blocks = flatten(nestedBlocks)


class BlockFactory:
    def __init__(self):
        block = Block(1, 1)
        blockw = block.width
        blockh = block.height
        voffset = 40
        hoffset = blockw / 2

        rows = []
        blockNums = (10, 9, 8, 7, 6)
        i = 1
        for n in blockNums:
            rows.append(Row(n, (hoffset * i, WINDOW_H - i * voffset), hoffset,
                blockw))
            i+=1
        self.level0 = Level(rows)

