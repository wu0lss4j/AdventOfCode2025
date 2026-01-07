# Advent of Code 2025
# Day 11 part 2 | 2026.01.06 - 2026.01.07

"""
now I need to check all paths between 'srv' and 'out' and filter out those
which contain the nodes 'dac' and 'fft' in any order

I think this one is simpler, I can generate all paths and then count those paths
which have those two nodes

Without saving paths and just counting memo values, I found that between
"svr" and "out" there are 146.227.339.062.493.693 paths! If this is correct this
is an absurdly large number of paths to comb through for "fft" and "dac"

The coding logic on my script simply cannot handle that many number of paths
across 605 nodes. There must be another way to prune faster. Maybe DFS cannot
be used here, and I need to use BFS... assuming both "fft" and "dac" are closer.

Maybe, I should try to find "fft" and "dac" first, like how many paths there are
 from fft to dac and from dac to fft. These must be mutually exclusive. Then I
could search for the paths from srv to fft and srv to dac, then the paths from
fft to out and from dac to out.

I was too tired yesterday, but still I ran the calculate paths method 6 times and interrupted 1 of them, and aborted 2 others. I ran FFT-DAC and it returned a memo of 7 M+, then the DAC-FFT returned 0. I found that odd but understandable, maybe there are no cycles, and more importantly it is a directed graph and as it is structured it will return FFT-DAC paths but not the opposite. Then I just searched for SVR-FFT and DAC-OUT, just for kicks I tried to find SVR-DAC and it was taking forever, so I assumed it made no sense to continue and interrupted that search, which left me with the final two searches which I did not even run (they are commented in the code.)

"""


class Node:
    def __init__(self, id: str, parents: list, children: list):
        self.id = id
        self.parents: list = parents or []
        self.children: list = children or []

    def add_parent(self, parent: str):
        self.parents.append(parent)

    def add_child(self, child: str):
        self.children.append(child)

    def __str__(self):
        return f"Node {self.id} has {self.parents} parents {self.children} children"

    def __repr__(self):
        return (
            f"Node(id={self.id!r}, "
            f"parents={self.parents!r}, "
            f"children={self.children!r})"
        )


class Nodes:
    def __init__(self, nodes: None):
        nodes = nodes or []
        self.nodes: dict = {node.id: node for node in nodes}

    def __str__(self):
        for node in self.nodes.values():
            print(f"{node}")
        return f"Total nodes: {len(self.nodes)}"

    def __iter__(self):
        return iter(self.nodes.values())

    def __repr__(self):
        return f"Nodes(nodes={list(self.nodes.values())!r})"

    def make_graph(self):
        new_node_counter: int = 0
        new_parent_counter: int = 0
        for node in list(self.nodes.values()):
            for child_id in node.children:
                if child_id not in self.nodes:
                    # print(f' creating missing node "{child_id}"')
                    new_node_counter += 1
                    self.nodes[child_id] = Node(child_id, [], [])

                # print(f' adding "{node.id}" as parent of "{child_id}"')
                new_parent_counter += 1
                self.nodes[child_id].add_parent(node.id)
        print(f" graph building complete {new_parent_counter=} {new_node_counter=}")


class Path:
    def __init__(self, id: str, nodes: list[Node]):
        self.id = id
        self.nodes: list = nodes

    def add_node(self, node: Node):
        self.nodes.append(node)

    def __str__(self):
        path_tmp = " ==> ".join(self.nodes)
        return f"{self.id}: {path_tmp}"

    def __repr__(self):
        return f"Path(id={self.id!r}, nodes={self.nodes!r}, "


class Paths:
    def __init__(self, paths: None):
        paths = paths or []
        self.paths: dict = {path.id: path for path in paths}

    def __len__(self):
        return len(self.paths)

    def __str__(self):
        for i, path in enumerate(self.paths.values()):
            print(f"Path {i}: {path}")
        return f"Total paths: {len(self.paths)}"

    def __iter__(self):
        return iter(self.paths.values())

    def __repr__(self):
        return f"Paths(paths={list(self.paths.values())!r})"

    def calculate_paths(self, nodes_list: Nodes, node_from: str, node_to: str) -> None:
        print(f" looking for path from {node_from} to {node_to}")
        print(f"{nodes_list.nodes[node_from]=}")
        print(f"{nodes_list.nodes[node_to]=}")

        node_curr = node_from

        done: bool = False

        nodes_visited: dict | None = {}

        def pretty_print_nodes_visited(nodes_visited):
            # print("<!> function call pretty_print_nodes_visited <!>")
            lines = []
            for node, info in nodes_visited.items():
                memo = info["memo"]
                paths = info["paths"]

                lines.append(f"{node}: memo={memo}")
                for i, path in enumerate(paths, start=1):
                    lines.append(f"    path {i}: {path}")

            return "\n".join(lines)

        # helper function to add a path to the nodes_visited dictionary
        def add_path(node: Node, path: list) -> None:
            # print(f"<!> function call add_path {node=} {path=} <!>")
            if node not in nodes_visited:
                nodes_visited[node] = {"memo": 0, "paths": []}

            # nodes_visited[node]["memo"] += 1

            nodes_visited[node]["paths"].append(path)

        def backtrack() -> Node:
            # print(f"<!> function call backtrack {path_curr=} <!>")
            # print(f"    Backtrack to previous Node on the current path {path_curr}")

            if node_curr == node_from:
                # print("Trying to backtrack from start, end now.")
                # print(pretty_print_nodes_visited(nodes_visited))
                # print(f"\n{nodes_visited[node_from]["memo"]=}")

                # self.paths nodes_visited[node_from]["paths"]
                node_from_memo = nodes_visited[node_from]["memo"]
                for path_i in range(
                    0,
                    node_from_memo,
                ):
                    # print(f"{path_i}: {nodes_visited[node_from]['paths'][path_i]}")
                    # XXX to speed up
                    # self.paths[path_i] = nodes_visited[node_from]["paths"][path_i]
                    self.paths[path_i] = []

                return None

            node = path_curr.pop()  # remove last element from path
            # print(f"popping last node >{node}< from {path_curr}")
            # node = path_curr.pop()
            node = path_curr[-1]
            # print(f"setting next current node as >{node}< from {path_curr}")
            return node

        def check_children(node: Node) -> Node:
            # print(f"<!> function call check_children for |{node}| <!>")
            for child in nodes_list.nodes[node].children:
                # print(f"     {child=}")

                if child in nodes_visited:
                    # print(f"     Node |{child}| has been visited, check the next one")
                    pass
                else:
                    # print(
                    #     f"     Node |{child}| has NOT been visited, go visit this child"
                    # )
                    node = child
                    break
            else:
                # print(
                #     f"    Node |{node}| has {len(nodes_list.nodes[node].children)} children"
                # )
                # print(
                #     f"    All child nodes of {node} have been visited, backtrack and add all children's memo values and copy their associated paths"
                # )

                # print(f"    Backtrack to previous Node on the {path_curr=}\n")

                for child in nodes_list.nodes[node].children:
                    # print(
                    #     f"        Child Node |{child}| memo = {nodes_visited[child]['memo']}"
                    # )
                    nodes_visited[node]["memo"] += nodes_visited[child]["memo"]

                    if nodes_visited[child]["memo"] != 0:
                        # print(
                        #     f"memo should be greater than zero, or >>> {nodes_visited[child]['memo']=}"
                        # )
                        child_memo = nodes_visited[child]["memo"]
                        for path_i in range(0, child_memo, 1):
                            # print(f"Node |{child}| ... {path_i=} of {child_memo=}")

                            tmp_path: list = [node]
                            # print(f"{tmp_path=}")
                            # print(nodes_visited[child]["paths"][path_i])

                            # XXX to speed up...
                            # tmp_path.extend(nodes_visited[child]["paths"][path_i])
                            # print(f"{tmp_path=}")
                            add_path(node, tmp_path)

                    else:
                        # print(
                        #     f"memo should be zero, or >>> {nodes_visited[child]['memo']=}"
                        # )
                        # print(f"do not add child Node |{child}|'s paths")
                        pass

                if nodes_visited[node]["memo"] > 0:
                    with open("input_day11_p2_tmp_file2.txt", "a") as f:
                        step = (
                            node
                            + ": "
                            + str(nodes_visited[node]["memo"])
                            + " "
                            # + str(len(nodes_visited[node]["paths"]))
                            # + ",".join(map(str, nodes_visited[node]["paths"]))
                            + "\n"
                        )
                        f.write(step)

                # print(
                #     f"        Total passed to |{node}| = {nodes_visited[node]['memo']}"
                # )

                node = backtrack()
            return node

        path_curr: list | None = []
        it: int = 0

        while not done:
            it += 1

            if node_curr is None:
                done = True
                continue

            # print("\n >>> ############################################################")
            print(
                f" >>> {node_from}-{node_to} iteration {it} at the current Node |{node_curr}|"
            )
            print(f" >>> nodes visited: {len(nodes_visited)}")
            # print(f" >>> Current path is: {path_curr}\n")

            if node_curr in nodes_visited:  # NODE VISITED
                # print(f"  Node |{node_curr}| has been visited before")
                # print(f"  Check Node |{node_curr}| memo value")
                # print(
                #     f"  Node |{node_curr}| has memo value of: {nodes_visited[node_curr]['memo']}"
                # )
                if nodes_visited[node_curr]["memo"] == 0:
                    # print(f"  Check Node |{node_curr}|'s children")
                    node_curr = check_children(node_curr)

                else:  # MEMO GREATER THAN ZERO!
                    print(f">>>>>>>>> PSSSSSSSSSSSSSSSSSSSSSST {node_curr}")
                    # node_curr = backtrack()
                    input("\n\n... STOP HERE ...")
                    quit()

            else:  # NODE NOT YET VISITED
                # print(f"  Node |{node_curr}| has NOT been visited before")
                nodes_visited[node_curr] = {"memo": 0, "paths": []}
                path_curr.append(node_curr)

                # is the current node the target node?
                # print(f"   Is Node |{node_curr}| the target Node |{node_to}|?")
                if node_curr == node_to:
                    # print(
                    #     f"    TARGET REACHED !!! Node |{node_curr}| matches the target node |{node_to}|"
                    # )
                    nodes_visited[node_curr]["memo"] = 1
                    # nodes_visited[node_curr]["paths"].append(node_curr)
                    add_path(node_curr, [node_curr])  # sneaky str needs to be list

                    # print(f"\n\n{nodes_visited}\n\n")
                    # print(f"    Backtrack on the {path_curr=}")
                    node_curr = backtrack()
                else:
                    # print(
                    #     f"    Node {node_curr} is not {node_to}, check |{node_curr}|'s children"
                    # )
                    # if not, let's check each child
                    node_curr = check_children(node_curr)

            print(f"\n <<< iteration {it} ended, next Node is |{node_curr}|\n")

            # print(pretty_print_nodes_visited(nodes_visited))
            # input("press any key to continue...")


def xmas() -> None:
    xmas_tree = "\
         1\n\
        *1*\n\
       *****\n\
      *O**#**\n\
     ****O**.*\n\
    *§******@**\n\
        {$}\n\
       _{$}_   (bl)\n"

    print(xmas_tree)


def main():
    # open input file
    with open("input_day11.txt", "r") as f:
        raw_data = f.read()

    nodes_list = Nodes([])

    #
    for row in raw_data.splitlines():
        parts: list = row.split(" ")
        parts_len: int = len(parts)

        node_id: str = parts[0].strip(":")

        children: list = []
        for child in range(1, parts_len):
            children.append(parts[child])

        # print(f"{parts[0].strip(':')}, {[]}, {children}")
        nodes_list.nodes[node_id] = Node(node_id, [], children)

    print(" ... building graph.")
    nodes_list.make_graph()

    print(f"{nodes_list}")
    # print(f"insanity check, is nodes_list class Nodes? {isinstance(nodes_list, Nodes)}")

    # Day 11 part 2 specific entries
    node_from = "fft"  # "svr"
    node_to = "dac"  # "out"
    print(f"\n ... calculating all paths between {node_from} and {node_to}")

    # # if node_from not in nodes_list.nodes:
    # #     print(f"ERROR: {node_from=} is not found in the graph")
    # #     return 0

    # # if node_to not in nodes_list.nodes:
    # #     print(f"ERROR: {node_to=} is not found in the graph")
    # #     return 0

    # # print(
    # #     f'starting from "{node_from}" which children are: {nodes_list.nodes[node_from].children}'
    # # )

    paths_list = Paths([])
    paths_list.calculate_paths(nodes_list, node_from, node_to)
    # print(f"{paths_list}")
    # print()
    with open("input_day11_paths_FFT-DAC.txt", "w") as f:
        # for path in paths_list:
        #     step = ",".join(map(str, path)) + "\n"
        #     f.write(step)
        f.write(str(len(paths_list)))

    # node_from = "dac"
    # node_to = "fft"
    # print(f"\n ... calculating all paths between {node_from} and {node_to}")
    # paths_list = Paths([])
    # paths_list.calculate_paths(nodes_list, node_from, node_to)
    # with open("input_day11_paths_DAC-FFT.txt", "w") as f:
    #     # for path in paths_list:
    #     #     step = ",".join(map(str, path)) + "\n"
    #     #     f.write(step)
    #     f.write(str(len(paths_list)))

    # node_from = "svr"
    # node_to = "dac"
    # print(f"\n ... calculating all paths between {node_from} and {node_to}")
    # paths_list = Paths([])
    # paths_list.calculate_paths(nodes_list, node_from, node_to)
    # with open("input_day11_paths_SVR-DAC.txt", "w") as f:
    #     # for path in paths_list:
    #     #     step = ",".join(map(str, path)) + "\n"
    #     #     f.write(step)
    #     f.write(str(len(paths_list)))

    node_from = "svr"
    node_to = "fft"
    print(f"\n ... calculating all paths between {node_from} and {node_to}")
    paths_list = Paths([])
    paths_list.calculate_paths(nodes_list, node_from, node_to)
    with open("input_day11_paths_SVR-FFT.txt", "w") as f:
        # for path in paths_list:
        #     step = ",".join(map(str, path)) + "\n"
        #     f.write(step)
        f.write(str(len(paths_list)))

    node_from = "dac"
    node_to = "out"
    print(f"\n ... calculating all paths between {node_from} and {node_to}")
    paths_list = Paths([])
    paths_list.calculate_paths(nodes_list, node_from, node_to)
    with open("input_day11_paths_DAC-OUT.txt", "w") as f:
        # for path in paths_list:
        #     step = ",".join(map(str, path)) + "\n"
        #     f.write(step)
        f.write(str(len(paths_list)))

    # node_from = "fft"
    # node_to = "out"
    # print(f"\n ... calculating all paths between {node_from} and {node_to}")
    # paths_list = Paths([])
    # paths_list.calculate_paths(nodes_list, node_from, node_to)
    # with open("input_day11_paths_FFT-OUT.txt", "w") as f:
    #     # for path in paths_list:
    #     #     step = ",".join(map(str, path)) + "\n"
    #     #     f.write(step)
    #     f.write(str(len(paths_list)))


if __name__ == "__main__":
    main()
