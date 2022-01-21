class PathFinder:

    def __init__(self, graph):
        self.graph = graph

    def print_path(self, entry_node_id, exit_node_id):
        print(self.find_path(entry_node_id, exit_node_id))

    def search(self, current_node, target_node):
        paths = []
        if current_node.id == target_node.id:
            return PathFinder.Path([current_node])

        for exit_arc in current_node.exits:
            steps = [current_node, exit_arc]
            steps.extend(self.search(exit_arc.end, target_node).path_items)
            if map(lambda s: s.id, steps).__contains__(target_node.id):
                paths.append(PathFinder.Path(steps))
        if paths:
            paths.sort(key=lambda p: p.length(), reverse=True)
            return paths[0]
        return PathFinder.Path()

    def find_path(self, entry_node_id, exit_node_id):
        path = self.search(self.graph.nodes[entry_node_id], self.graph.nodes[exit_node_id])
        if path.path_items:
            return path
        else:
            raise Exception("Path not found")

    class Path:
        def __init__(self, path_items=None):
            if path_items is None:
                path_items = []
            self.path_items = path_items
            self.next_item_by_item_id = {}
            key_item = None
            for item in self.path_items:
                if key_item is not None:
                    self.next_item_by_item_id[key_item.id] = item
                key_item = item

        def get_next_item(self, item_id):
            return self.next_item_by_item_id[item_id]

        def __str__(self):
            return map(lambda i: i.id, self.path_items).__str__()

        def append(self, path_item):
            self.path_items.append(path_item)

        def append_all(self, path_items):
            for item in path_items:
                self.path_items.append(item)

        def length(self):
            length = 0
            for item in self.path_items:
                if item.type == 'Arc':
                    length = length + item.length
            return length
