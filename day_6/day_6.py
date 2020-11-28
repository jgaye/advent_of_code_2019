from anytree import Node, RenderTree, findall, Walker


class DefaultNodeDict(dict):
    def __missing__(self, key):
        res = self[key] = Node(key)
        return res


if __name__ == "__main__":

    # with open("example_1") as f:
    with open("input_1") as f:
        input_m = [line.rstrip() for line in f]

    # print(f"input {input_m}")

    nodes = DefaultNodeDict()

    for input_orbit in input_m:
        center, satellite = input_orbit.split(")")
        nodes[satellite].parent = nodes[center]

    print(RenderTree(nodes["COM"]))
    w = Walker()
    # upward, common, downward = w.walk(nodes["YOU"], nodes["SAN"])
    # print(len(upward) + len(downward) - 2)

    # Part 1 below ###
    total = 0
    for node in nodes.values():
        upward, common, downward = w.walk(node, nodes["COM"])
        total += len(upward) + len(downward)
    print(total - len(nodes))
