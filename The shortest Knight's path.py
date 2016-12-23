def checkio(cells):
    move = ["03232345",
            "32123434",
            "21432345",
            "32323434",
            "23234345",
            "34343454",
            "43434545",
            "54545456"]
    if cells in ["h1-g2", "g2-h1", "h8-g7", "g7-h8", "a1-b2", "b2-a1", "a8-b7", "b7-a8"]:
        return 4
    x = abs(ord(cells[0]) - ord(cells[3]))
    y = abs(ord(cells[1]) - ord(cells[4]))
    return int(move[x][y])
