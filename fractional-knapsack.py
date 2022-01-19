

def frac_knapsack(li: dict):
    knapsack: dict = {}
    weight: int = 240
    curr_weight: int = 0
    total_value: float = 0.0
    for l in li.items():
        if l[1]["Weight"] + curr_weight <= weight:
            curr_weight += l[1]["Weight"]
            total_value += l[1]["Value"]
            knapsack += dict(l)
        else:
            remain: int = weight - curr_weight
            total_value += l[1]["Value"] * \
                float(float(remain)/float(l[1]["Weight"]))
            break

    print(knapsack)
    print(f"Total value :{total_value}")


def printItems(li: dict) -> None:
    print("Item", end="\t")
    print("Value", end="\t")
    print("Weight", end="\t")
    print("Ratio", end="\n")
    print()
    i = 0
    for l in li.items():
        print(i, end="\t")
        print(l[1]["Value"], end="\t")
        print(l[1]["Weight"], end="\t")
        print(l[1]["Ratio"], end="\n")
        i += 1
    print()


def main():
    items = {}
    items[0] = {"Value": 60, "Weight": 10}
    items[1] = {"Value": 50, "Weight": 20}
    items[2] = {"Value": 120, "Weight": 30}
    items[3] = {"Value": 100, "Weight": 50}
    for i in range(0, len(items)):
        items[i]["Ratio"] = items[i]["Value"] / items[i]["Weight"]
    printItems(items)
    s_items = dict(
        sorted(items.items(), key=lambda x: (x[1]["Ratio"]), reverse=True))
    printItems(s_items)
    frac_knapsack(s_items)


if __name__ == '__main__':
    main()
