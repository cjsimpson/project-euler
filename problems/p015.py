'''
Project Eurler Problem 15
http://projecteuler.net/problem=15
'''
from collections import deque


class GridPoint():
    def __init__(self, position):
        self.right = None
        self.down = None
        self.position = position  # x,y, 0,0 = top left

    def children(self):
        if self.right is None and self.down is None:
            return ()
        return [self.right, self.down]


def create_grid_points(width, height):
    grid = set()
    for x in xrange(width):
        for y in xrange(height):
            grid.add((x, y))
    return grid


def make_route_tree(grid_width, grid_height):
    #1 more point than block
    grid_width += 1
    grid_height += 1

    grid = create_grid_points(grid_width, grid_height)

    point_cache = dict()
    bottom_right = GridPoint((grid_width - 1, grid_height - 1))
    point_cache[(grid_width - 1, grid_height - 1)] = bottom_right

    for x in range(grid_width - 1, -1, -1):        # Start x at right hand side
        for y in range(grid_height - 1, -1, -1):   # Start y at bottom
            current_point = GridPoint((x, y))
            if (x + 1, y) in grid:
                current_point.right = point_cache[(x + 1, y)]

            if (x, y + 1) in grid:
                current_point.down = point_cache[(x, y + 1)]
            point_cache[(x, y)] = current_point

    return point_cache


def find_all_paths(start_node, tree):
    to_process_nodes = deque([start_node.position])
    routes = deque()
    current_route = deque()

    while to_process_nodes:
        current = tree[to_process_nodes.popleft()]
        current_route.append(current.position)
        node_children = [x.position for x in current.children() if x is not None]
        if node_children == []:
            routes.append(tuple(current_route))
            current_route.clear()
        to_process_nodes.extendleft(node_children)

    return routes



def solve():
    pass

if __name__ == '__main__':
    solve()
    #size = (12, 12)
    #x_cord, y_cord = size
    #print size
    #print
    #pc = make_route_tree(x_cord, y_cord)
    #root = pc[(0, 0)]
    #all_paths = find_all_paths(root, pc)
    #count = len(all_paths)
    #print count
