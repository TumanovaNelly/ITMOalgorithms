from typing import Optional, List
from Lab4.Task13.src.Queue import Queue


class TreeNode:
    def __init__(self):
        self.children: List[TreeNode] = []


class Tree:
    def __init__(self, root: TreeNode):
        self.root = root

    @property
    def height(self) -> int:
        queue = Queue()
        queue.push(self.root)

        height = 0
        while not queue.is_empty():
            level_size = len(queue)
            for _ in range(level_size):
                node = queue.pop()
                for child in node.children:
                    queue.push(child)
            height += 1

        return height


def build_tree(elements_data: List[int]) -> Optional[Tree]:
    nodes: List[TreeNode] = list(map(lambda _: TreeNode(), elements_data))
    tree: Optional[Tree] = None

    for number, value in enumerate(elements_data):
        if value == -1:
            tree = Tree(nodes[number])
            continue

        nodes[value].children.append(nodes[number])

    return tree

