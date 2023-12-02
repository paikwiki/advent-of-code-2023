def parse(line: str):
    [game_title, hands] = line.split(": ")
    hands = [hand.split(", ") for hand in hands.split("; ")]

    cubes = []
    for hand in hands:
        cube = {}
        for cube_raw in hand:
            [count, color] = cube_raw.split(" ")
            cube[color] = int(count)
        cubes.append(cube)

    return (int(game_title.replace("Game ", "")), cubes)

def isPossible(hands):
    MAX = {
        "red": 12,
        "green": 13,
        "blue": 14,
    }
    for hand in hands:
        if (
            ("red" in hand and MAX["red"] < hand["red"])
            or ("green" in hand and MAX["green"] < hand["green"])
            or ("blue" in hand and MAX["blue"] < hand["blue"])
        ):
            return False

    return True


def solve1(lines: str):
    lines = lines.strip().splitlines()
    sum = 0
    for line in lines:
        [game_id, hands] = parse(line)
        if isPossible(hands):
            sum += game_id

    return sum


def calculate(hands):
    result = {
        "red": 1,
        "green": 1,
        "blue": 1,
    }
    for hand in hands:
        for color in ["red", "green", "blue"]:
            if color in hand:
                result[color] = max(result[color], hand[color])
    return result["red"] * result["green"] * result["blue"]


def solve2(lines: str):
    lines = lines.strip().splitlines()
    sum = 0
    for line in lines:
        [_, hands] = parse(line)
        sum += calculate(hands)
    return sum


def test(lines):
    result = solve1(lines)
    print(f"result: {result}")

    result = solve2(lines)
    print(f"result: {result}")


if __name__ == "__main__":
    with open("input") as input:
        test(input.read())
