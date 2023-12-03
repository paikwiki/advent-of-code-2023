def generate_table(lines: str):
    lines = lines.strip().splitlines()

    return [list(line) for line in lines]


def issymbol(chr: str):
    if chr.isdigit() or chr == ".":
        return False

    return True


def check_adjacent(pos: (int, int), table: list[list[str]]):
    (row_idx, col_idx) = pos
    digit_cells = []
    for r_idx in range(row_idx - 1, row_idx + 2):
        for c_idx in range(col_idx - 1, col_idx + 2):
            if r_idx == row_idx and c_idx == col_idx:
                continue
            if table[r_idx][c_idx].isdigit():
                digit_cells.append((r_idx, c_idx))

    return digit_cells


def solve1(lines):
    table = generate_table(lines)

    adjacents = set()
    digits_list = []
    digits = []
    for row_idx, row in enumerate(table):
        for col_idx, cell in enumerate(row):
            if issymbol(cell):
                adjacents.update(check_adjacent((row_idx, col_idx), table))
            if cell.isdigit():
                digits.append((row_idx, col_idx))
            else:
                if len(digits) > 0:
                    digits_list.append(digits)
                    digits = []

    part_nums = []
    for digits in digits_list:
        for digit in digits:
            if digit in adjacents:
                part_nums.append(int("".join([table[x][y] for (x, y) in digits])))
                break

    return sum(part_nums)


def test(lines):
    result = solve1(lines)
    print(f"result: {result}")


if __name__ == "__main__":
    with open("input") as input:
        test(input.read())
