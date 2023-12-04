def solve1(lines: str):
    sum = 0
    for line in lines.strip().splitlines():
        digits = [chr for chr in line if chr.isdigit()]
        sum += int(digits[0] + digits[-1])

    return sum


def solve2(lines: str):
    def parse(line: str):
        SPELLED_DIGITS = [
            "one",
            "two",
            "three",
            "four",
            "five",
            "six",
            "seven",
            "eight",
            "nine",
        ]
        first = last = ""
        for i, cell in enumerate(line):
            if first != "":
                break
            if cell.isdecimal():
                first = cell
            else:
                for spelled in SPELLED_DIGITS:
                    target = line[i : len(spelled) + i]
                    if target == spelled:
                        first = str(SPELLED_DIGITS.index(spelled) + 1)
                        break

        for i, _ in enumerate(line, 0):
            if last != "":
                break
            reverse_i = len(line) - 1 - i
            if line[reverse_i].isdecimal():
                last = line[reverse_i]
            else:
                for spelled in SPELLED_DIGITS:
                    target = line[reverse_i - len(spelled) + 1 : reverse_i + 1]
                    if target == spelled:
                        last = str(SPELLED_DIGITS.index(spelled) + 1)
                        break

        return first + last

    sum = 0
    for line in lines.strip().splitlines():
        sum += int(parse(line))

    return sum


def test(lines):
    result = solve1(lines)
    print(f"result: {result}")
    result = solve2(lines)
    print(f"result: {result}")


if __name__ == "__main__":
    with open("input") as input:
        test(input.read())
