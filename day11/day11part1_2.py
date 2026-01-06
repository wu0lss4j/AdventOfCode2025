# Advent of Code
# Day 11 | 2025.12.22 - 2026.01.06 (did nothing between X-mas and yesterday 05 JAN 2025
#                                   however, I did think long and hard about this challenge
#                                   and watched MIT open courseware about DFS, and read
#                                   some graph theory, but I was pretty much unsatisfied
#                                   that it could be so simple with recursion, or... that
#                                   it couldn't be optimized to prune alreay searched paths
#                                   I even designed a separate input_demo2.txt with dead-end
#                                   nodes... I did not test my code for cycles though...
#
#                                   directed graphs be damned...
#

"""
I figure since I just learned how to work with classes in python, I'd just try to determine the total number of paths in this problem using... classes. Ofc I could be wrong, but I cannot imagine not bruteforcing this.

I was trying to guessimate a formula, by looking a the graph and counting the number of children and everytime there is more than 1 child, that creates a whole new path... but...!!! there is an edge case to this hypothesis, when there is BB8 (or snowman shaped) graph, in which a bunch of branches converge on a node, before splitting up again, and converging at the end. I don't like this, so I think I will walk all paths, backtracking when necessary.

Also, I am now afraid that I will not finish all challenges before the night of the 24th.

Of course, today being the 26th it can only mean I was quite busy with the festivities.

I am now thinking if it is actually faster to do a reverse depth search, as in, I will start from the end and follow all paths to the start and count only those that begin with the start... because, the end node is actually a key in the graph, so it is lightning fast to get to it, then I only have to find the parents. On second thought I think approach may not be faster than starting at the start node and ending at end node.
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

    # Maybe sibling is not the right word, but if it kind of makes sense, because if a certain node has more than one parent then, the children of different parents with the same child should all become siblings... for algo purposes, I think. But on the other hand if I want to traverse blindly the whole graph, sometimes certain nodes are siblings and other times they are not, because one parent may have 3 children, 2 of which are common with another parent, and when I and travelling the path from the parent node with two children I don't want to see the 3rd child from the other parent, so in a way, siblings do not need to be determined at the graph building stage, rather, at the path finding stage.
    # def add_sibling(self, sibling: str):
    #     self.sibling.append(sibling)


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

    def __str__(self):
        for path in self.paths.values():
            print(f"{path}")
        return f"Total paths: {len(self.paths)}"

    def __iter__(self):
        return iter(self.paths.values())

    def __repr__(self):
        return f"Paths(paths={list(self.paths.values())!r})"

    def calculate_paths(self, nodes_list: Nodes, node_from: str, node_to: str) -> None:
        # must detect cycle
        # must detect loop to itself (special kind of cycle?)
        # must detect false ending
        print(f" looking for path from {node_from} to {node_to}")
        print(f"{nodes_list.nodes[node_from]=}")
        print(f"{nodes_list.nodes[node_to]=}")

        node_curr = node_from

        done: bool = False
        path_counter: int = 0
        nodes_visited: dict | None = {}

        def pretty_print_nodes_visited(nodes_visited):
            print("<!> function call pretty_print_nodes_visited <!>")
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
            print(f"<!> function call add_path {node=} {path=} <!>")
            if node not in nodes_visited:
                nodes_visited[node] = {"memo": 0, "paths": []}

            # nodes_visited[node]["memo"] += 1

            nodes_visited[node]["paths"].append(path)

        def backtrack() -> Node:
            print(f"<!> function call backtrack {path_curr=} <!>")
            print(f"    Backtrack to previous Node on the current path {path_curr}")

            if node_curr == node_from:
                print("Trying to backtrack from start, end now.")
                print(pretty_print_nodes_visited(nodes_visited))
                print(f"\n{nodes_visited[node_from]["memo"]=}")
                quit()

            node = path_curr.pop()  # remove last element from path
            print(f"popping last node >{node}< from {path_curr}")
            # node = path_curr.pop()
            node = path_curr[-1]
            print(f"setting next current node as >{node}< from {path_curr}")
            return node

        def check_children(node: Node) -> Node:
            print(f"<!> function call check_children for |{node}| <!>")
            for child in nodes_list.nodes[node].children:
                print(f"     {child=}")

                if child in nodes_visited:
                    print(f"     Node |{child}| has been visited, check the next one")
                else:
                    print(
                        f"     Node |{child}| has NOT been visited, go visit this child"
                    )
                    node = child
                    break
            else:
                print(
                    f"    Node |{node}| has {len(nodes_list.nodes[node].children)} children"
                )
                print(
                    f"    All child nodes of {node} have been visited, backtrack and add all children's memo values and copy their associated paths"
                )

                print(f"    Backtrack to previous Node on the {path_curr=}\n")

                for child in nodes_list.nodes[node].children:
                    print(
                        f"        Child Node |{child}| memo = {nodes_visited[child]['memo']}"
                    )
                    nodes_visited[node]["memo"] += nodes_visited[child]["memo"]

                    if nodes_visited[child]["memo"] != 0:
                        print(
                            f"memo should be greater than zero, or >>> {nodes_visited[child]['memo']=}"
                        )
                        child_memo = nodes_visited[child]["memo"]
                        for path_i in range(0, child_memo, 1):
                            print(f"Node |{child}| ... {path_i=} of {child_memo=}")

                            tmp_path: list = [node]
                            print(f"{tmp_path=}")
                            print(nodes_visited[child]["paths"][path_i])
                            tmp_path.extend(nodes_visited[child]["paths"][path_i])
                            print(f"{tmp_path=}")
                            add_path(node, tmp_path)

                        # for node, info in nodes_visited.items():
                        #     paths = info["paths"]
                        #     for i, path in enumerate(paths, start=1):

                        #         lines.append(f"    path {i}: {path}")

                    else:
                        print(
                            f"memo should be zero, or >>> {nodes_visited[child]['memo']=}"
                        )
                        print(f"do not add child Node |{child}|'s paths")

                print(
                    f"        Total passed to |{node}| = {nodes_visited[node]['memo']}"
                )

                # path_curr.pop()  # remove last element from path
                # node = path_curr.pop()

                node = backtrack()
            return node

        path_curr: list | None = []
        it: int = 0

        while not done:
            it += 1
            print("\n >>> ############################################################")
            print(
                f" >>> Starting iteration {it} at the current Node is |{node_curr}| which has {len(nodes_list.nodes[node_curr].children)} children"
            )
            print(f" >>> Current path is: {path_curr}\n")

            if node_curr in nodes_visited:  # NODE VISITED
                print(f"  Node |{node_curr}| has been visited before")
                print(f"  Check Node |{node_curr}| memo value")
                print(
                    f"  Node |{node_curr}| has memo value of: {nodes_visited[node_curr]['memo']}"
                )
                if nodes_visited[node_curr]["memo"] == 0:
                    print(f"  Check Node |{node_curr}|'s children")
                    node_curr = check_children(node_curr)

                else:  # MEMO GREATER THAN ZERO!
                    print(f">>>>>>>>> PSSSSSSSSSSSSSSSSSSSSSST {node_curr}")
                    # node_curr = backtrack()
                    input("\n\n... STOP HERE ...")
                    quit()

            else:  # NODE NOT YET VISITED
                print(f"  Node |{node_curr}| has NOT been visited before")
                nodes_visited[node_curr] = {"memo": 0, "paths": []}
                path_curr.append(node_curr)

                # is the current node the target node?
                print(f"   Is Node |{node_curr}| the target Node |{node_to}|?")
                if node_curr == node_to:
                    print(
                        f"    TARGET REACHED !!! Node |{node_curr}| matches the target node |{node_to}|"
                    )
                    nodes_visited[node_curr]["memo"] = 1
                    # nodes_visited[node_curr]["paths"].append(node_curr)
                    add_path(node_curr, [node_curr])  # sneaky str needs to be list

                    print(f"\n\n{nodes_visited}\n\n")
                    print(f"    Backtrack on the {path_curr=}")
                    node_curr = backtrack()
                else:
                    print(
                        f"    Node {node_curr} is not {node_to}, check |{node_curr}|'s children"
                    )
                    # if not, let's check each child
                    node_curr = check_children(node_curr)

            print(
                f"\n End of iteration {it}: {path_counter=} {path_curr}, next Node |{node_curr}|\n"
            )

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

    paths_list = Paths([])
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

    print('\n ... calculating all paths between "you" and "out "')
    node_from = "you"
    node_to = "out"

    if node_from not in nodes_list.nodes:
        print(f"ERROR: {node_from=} is not found in the graph")
        return 0

    if node_to not in nodes_list.nodes:
        print(f"ERROR: {node_to=} is not found in the graph")
        return 0

    print(
        f'starting from "{node_from}" which children are: {nodes_list.nodes[node_from].children}'
    )

    # path_id = "0"
    # stack: list = []
    # stack.append(nodes_list.nodes[node_from].id)
    # print(f"{stack=}")
    # paths_list.paths[path_id] = Path(path_id, stack)

    # starting node found, current path starts at "you"
    # print(f"{paths_list.paths.values()}")
    # print(f"{paths_list.paths['0']}")
    # print(f"{paths_list.paths}")
    # print(f"{paths_list}")
    # print(f"{paths_list=}")

    paths_list.calculate_paths(nodes_list, "you", "out")
    print(f"{paths_list}")
    print()

    # mapa.paths.append(parts[0].strip(":"))


if __name__ == "__main__":
    main()
