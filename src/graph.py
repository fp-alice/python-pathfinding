import itertools
import operator
from queue import Queue


class Graph:
    def __init__(self, width, height, obstacles=None):
        self.width = width
        self.height = height
        self.obstacles = obstacles if obstacles is not None else []

    def points(self):
        return list(itertools.product(range(self.width), range(self.height)))

    def traversable_points(self):
        return [point for point in self.points() if self.is_point_traversable(point)]

    def is_point_in_bounds(self, point):
        (x, y) = point
        return 0 <= x < self.width and 0 <= y < self.height

    def is_point_traversable(self, point):
        return point not in self.obstacles

    def get_point_neighbors(self, point):
        (x, y) = point

        transformations = [(x, y + 1), (x + 1, y), (x - 1, y), (x, y - 1)]

        return [point for point in transformations
                if self.is_point_in_bounds(point) and self.is_point_traversable(point)]

    # I tried writing this function entirely myself, but I spent too much time trying to do it better and just couldn't
    # So this is basically copied with small alterations
    # Original is located at https://www.redblobgames.com/pathfinding/a-star/introduction.html
    def breadth_first_path_dict(self, from_point, to_point):
        queue = Queue()
        queue.put(from_point)
        came_from = {from_point: None}

        while not queue.empty():
            current = queue.get()

            if current == to_point:
                break

            for neighbor in self.get_point_neighbors(current):
                if neighbor not in came_from:
                    queue.put(neighbor)
                    came_from[neighbor] = current

        return came_from

    def find_path(self, from_point, to_point):
        path_dict = self.breadth_first_path_dict(from_point, to_point)

        def walk_graph(current, path):
            if current != from_point:
                return walk_graph(path_dict[current], [current] + path)
            else:
                return [from_point] + path

        return walk_graph(to_point, [])

    def graph_to_str(self, from_point=None, to_point=None):
        path = self.find_path(from_point, to_point) if from_point and to_point else []

        def point_to_str(point):
            if point in path:
                return "@"
            elif self.is_point_traversable(point):
                return "."
            else:
                return "|"

        sorted_list = zip(itertools.groupby(self.points(), operator.itemgetter(0)))
        rows = [[list(y) for (_, y) in row] for row in sorted_list if row is not []]
        string_rows = zip(*[[point_to_str(point) for point in row] for [row] in rows])

        return "\n".join(["".join(row) for row in string_rows])
