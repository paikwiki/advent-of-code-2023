def split_n_strip(line: str, sep: str):
    return list(filter(lambda line: line, [ln.strip() for ln in line.split(sep)]))


def parse_card(line: str):
    [_, rawline] = split_n_strip(line.strip(), ":")
    raws = split_n_strip(rawline, "|")
    (winnings, holds) = [split_n_strip(raw, " ") for raw in raws]

    return (winnings, holds)


def solve1(lines: str):
    total = 0
    for winnings, holds in [parse_card(line) for line in lines.strip().splitlines()]:
        point = 0
        for hold in holds:
            try:
                winnings.index(hold)
            except:
                continue
            point = point * 2 if point else 1

        total += point

    return total


def test(lines):
    result = solve1(lines)
    print(f"result: {result}")


if __name__ == "__main__":
    with open("input") as input:
        test(input.read())
