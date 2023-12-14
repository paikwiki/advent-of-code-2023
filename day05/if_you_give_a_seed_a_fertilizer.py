import sys

key_seeds = "seeds"
key_seed2soil = "seed-to-soil"
key_soil2fert = "soil-to-fertilizer"
key_fert2water = "fertilizer-to-water"
key_water2light = "water-to-light"
key_light2temp = "light-to-temperature"
key_temp2humi = "temperature-to-humidity"
key_humi2loca = "humidity-to-location"

ordered_keys = [
    key_seed2soil,
    key_soil2fert,
    key_fert2water,
    key_water2light,
    key_light2temp,
    key_temp2humi,
    key_humi2loca,
]


def split_n_strip(line: str, sep: str):
    return list(filter(lambda line: line, [ln.strip() for ln in line.split(sep)]))


def solve1(lines: str):
    raws = []
    for line in split_n_strip(lines, "\n\n"):
        [key_raw, raw_rules] = split_n_strip(line, ":")
        key = key_raw.replace(" map", "")
        raw_rules = split_n_strip(raw_rules, "\n")
        rules = [split_n_strip(rule, " ") for rule in raw_rules]
        raws.append((key, rules))

    seeds = []
    rules = {}
    for key, raw_rules in raws:
        if key == key_seeds:
            seeds = [int(seed) for seed in raw_rules[0]]
            continue

        rules_at_key = []
        for raw_rule in raw_rules:
            dst = int(raw_rule[0])
            src = int(raw_rule[1])
            size = int(raw_rule[2])
            rule = {"min": src, "max": src + size - 1, "distance": dst - src}
            rules_at_key.append(rule)
        rules[key] = rules_at_key

    nearby = sys.maxsize
    for seed in seeds:
        next_input = seed
        for key in ordered_keys:
            curr_input = next_input
            rules_at_key = [i for i in rules[key]]
            for rule in rules_at_key:
                if rule["min"] <= curr_input <= rule["max"]:
                    next_input = curr_input + rule["distance"]

        nearby = min(nearby, next_input)

    return nearby


def solve2(lines: str):
    raws = []
    for line in split_n_strip(lines, "\n\n"):
        [key_raw, raw_rules] = split_n_strip(line, ":")
        key = key_raw.replace(" map", "")
        raw_rules = split_n_strip(raw_rules, "\n")
        rules = [split_n_strip(rule, " ") for rule in raw_rules]
        raws.append((key, rules))

    seeds_list = []
    rules = {}
    max_max = 0
    min_min = sys.maxsize
    for key, raw_rules in raws:
        if key == key_seeds:
            for i in range(0, len(raw_rules[0]), 2):
                seeds_list.append(
                    range(
                        int(raw_rules[0][i]),
                        int(raw_rules[0][i]) + int(raw_rules[0][i + 1]),
                    )
                )
            continue
        rules_at_key = []
        for raw_rule in raw_rules:
            dst = int(raw_rule[0])
            src = int(raw_rule[1])
            size = int(raw_rule[2])
            rule = {"min": src, "max": src + size - 1, "distance": dst - src}
            min_min = min(min_min, src)
            max_max = max(max_max, src + size - 1)
            rules_at_key.append(rule)
        rules[key] = rules_at_key

    nearby = sys.maxsize

    for seeds in seeds_list:
        for seed in seeds:
            next_input = seed
            if seed >= max_max:
                nearby = next_input
                continue
            for key in ordered_keys:
                curr_input = next_input
                rules_at_key = [i for i in rules[key]]
                for rule in rules_at_key:
                    if rule["min"] <= curr_input <= rule["max"]:
                        next_input = curr_input + rule["distance"]
                        break
            nearby = min(nearby, next_input)
    return nearby


def test(lines):
    result = solve1(lines)
    print(f"result: {result}")

    result = solve2(lines)
    print(f"result: {result}")


if __name__ == "__main__":
    with open("input") as input:
        test(input.read())
