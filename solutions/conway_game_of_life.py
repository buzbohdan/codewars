"""https://www.codewars.com/kata/52423db9add6f6fc39000354/train/python"""
from copy import deepcopy
from functools import reduce


EMPTY, CELL = 0, 1
# A data type to contain coorditanes of alive cells. All cells with the same `y`
# coordinate are grouped together into a set that contains their `x` coordinates
GENERATION = dict[int, set[int]]


def get_neighbours(x: int, y: int) -> list[tuple[int, int]]:
    return [
        (_x, _y)
        for _x in range(x - 1, x + 2)
        for _y in range(y - 1, y + 2)
        if (_x, _y) != (x, y)
    ]


def get_cell(gen: GENERATION, x: int, y: int) -> int:
    return CELL if x in gen.get(y, set()) else EMPTY


def set_cell(gen: GENERATION, x: int, y: int) -> None:
    if y not in gen:
        gen[y] = set()
    gen[y].add(x)


def count_neigbours(gen: GENERATION, x: int, y: int) -> int:
    neighbours = get_neighbours(x, y)
    return sum(get_cell(gen, x, y) for x, y in neighbours)


def convert_generation_to_matrix(gen: GENERATION) -> list[list[int]]:
    # Get range of `x` and `y` coordinates to determine a size of result matrix
    all_x = reduce(lambda a, b: a.union(b), gen.values())
    min_x, max_x = min(all_x), max(all_x)
    min_y, max_y = min(gen.keys()), max(gen.keys())
    size_x = max_x - min_x + 1
    size_y = max_y - min_y + 1
    # Create empty matrix of appropriate size and fill if with alive cells
    result = [[EMPTY] * size_x for _ in range(size_y)]
    for y, x_coords in gen.items():
        for x in x_coords:
            result[y - min_y][x - min_x] = CELL
    return result


def convert_matrix_to_generation(cells: list[list[int]]) -> GENERATION:
    result: GENERATION = {}
    for y, line in enumerate(cells):
        for x, value in enumerate(line):
            if value == CELL:
                set_cell(result, x, y)
    return result


def get_generation(cells, generations):
    current_gen: GENERATION = convert_matrix_to_generation(cells)

    for _ in range(generations):
        new_gen: GENERATION = {}
        for y, x_coords in current_gen.items():
            for x in x_coords:
                # Check dead neighbours of this alive cell
                for neighbour_x, neighbour_y in get_neighbours(x, y):
                    if (
                        get_cell(current_gen, neighbour_x, neighbour_y) == EMPTY
                        and count_neigbours(current_gen, neighbour_x, neighbour_y) == 3
                    ):
                        set_cell(new_gen, neighbour_x, neighbour_y)

                # Determine a state of thi alive cell in the next generation
                count = count_neigbours(current_gen, x, y)
                if count in [2, 3]:
                    set_cell(new_gen, x, y)
        current_gen = deepcopy(new_gen)

    return convert_generation_to_matrix(current_gen)


get_generation(
    [
        [0, 1, 0],
        [1, 1, 1],
    ],
    2,
)
