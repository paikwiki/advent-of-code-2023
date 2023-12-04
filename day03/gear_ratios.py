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


def isgear(cell: str):
    return cell == "*"


def get_adjacent_digits(pos, row: list[str]):
    digits = [pos]
    (row_idx, col_idx) = pos

    cursor = col_idx - 1
    while True:
        try:
            if row[cursor].isdecimal():
                digits.insert(0, (row_idx, cursor))
                cursor -= 1
            else:
                break
        except IndexError:
            break

    cursor = col_idx + 1
    while True:
        try:
            if row[cursor].isdecimal():
                digits.append((row_idx, cursor))
                cursor += 1
            else:
                break
        except IndexError:
            break

    return digits


def calc_digits(pos, table: list[list[str]]):
    (row_idx, col_idx) = pos
    digits_list = []
    for r_idx in range(row_idx - 1, row_idx + 2):
        for c_idx in range(col_idx - 1, col_idx + 2):
            if r_idx == row_idx and c_idx == col_idx:
                continue
            if table[r_idx][c_idx].isdigit():
                adjacent_digits = get_adjacent_digits((r_idx, c_idx), table[r_idx])
                if adjacent_digits not in digits_list:
                    digits_list.append(adjacent_digits)

    return digits_list


def calc_ratio(digits_list: list[tuple[int, int]], table: list[list[str]]):
    if len(digits_list) != 2:
        return 0

    nums = []
    for digits in digits_list:
        digits = [table[x][y] for (x, y) in digits]
        nums.append(int("".join(digits)))

    return nums[0] * nums[1]


def solve2(lines: str):
    table = generate_table(lines)
    result = 0
    for row_idx, row in enumerate(table):
        for col_idx, cell in enumerate(row):
            if isgear(cell):
                digits_list = calc_digits((row_idx, col_idx), table)
                result += calc_ratio(digits_list, table)

    return result


def test(lines):
    result = solve1(lines)
    print(f"result: {result}")

    result = solve2(lines)
    print(f"result: {result}")


if __name__ == "__main__":
    with open("input") as input:
        test(input.read())
