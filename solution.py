import enchant


def find_neighbors_not_visited(grid, pos, visited):
    x, y = pos
    n, m = len(grid), len(grid[0])

    neighbors = []
    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            if (i, j) == (x, y):
                continue
            if 0 <= i < n and 0 <= j < m and (i, j) not in visited:
                neighbors.append((i, j))

    return neighbors


def find_all_words(grid, pos, prefix, visited, words_found):
    if len(prefix) >= 3 and d.check(prefix) and prefix not in words_found:
        words_found.add(prefix)
        print('Found word ' + prefix)

    neighs = find_neighbors_not_visited(grid, pos, visited)

    i, j = pos
    curr_letter = grid[i][j]
    for neigh in neighs:
        visited.add(neigh)
        find_all_words(grid, neigh, prefix + curr_letter, visited, words_found)
        visited.remove(neigh)


if __name__ == "__main__":
    grid = [
        ['R', 'A', 'E', 'L'],
        ['M', 'O', 'F', 'S'],
        ['T', 'E', 'O', 'K'],
        ['N', 'A', 'T', 'I']
    ]
    d = enchant.Dict("en_US")

    words_found = set()
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            find_all_words(grid, (i, j), "", {(i, j)}, words_found)

    print("Words formed by any sequence of up, down, left right")
    print(words_found)
