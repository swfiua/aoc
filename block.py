

def blocks(filename):

    lines = open(filename).readlines()

    block = []
    for line in lines:
        if not line.strip():
            yield block
            block = []
        else:
            block.append(line.strip())

    if block:
        yield block
