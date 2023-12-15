import re


def split_n_strip(line: str, sep: str):
    splits = [ln.strip() for ln in line.split(sep)]
    return list(filter(lambda line: line, splits))


def parse_solve1(lines: str):
    temp = []
    for line in lines.strip().splitlines():
        [_, raws] = split_n_strip(line, ":")
        temp.append(split_n_strip(raws, " "))

    return [(int(mills), int(dist)) for (mills, dist) in zip(*temp)]


def parse_solve2(lines: str):
    mills_n_dist = []
    for line in lines.strip().splitlines():
        [_, raws] = split_n_strip(line, ":")
        mills_n_dist.append(re.sub("\s", "", raws))

    return [(int(mills_n_dist[0]), int(mills_n_dist[1]))]


def solve(races: list[tuple[int, int]]):
    result = 1
    for mills, dist in races:
        count = 0
        for hold_time in range(1, mills + 1):
            run_time = mills - hold_time
            if dist < (hold_time * run_time):
                count += 1
        result = result * count

    return result


def solve1(lines: str):
    races = parse_solve1(lines)
    return solve(races)


def solve2(lines: str):
    races = parse_solve2(lines)
    return solve(races)


def test(lines):
    result = solve1(lines)
    print(f"result: {result}")

    result = solve2(lines)
    print(f"result: {result}")


if __name__ == "__main__":
    with open("input") as input:
        test(input.read())
