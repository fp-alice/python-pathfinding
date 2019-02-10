from graph import Graph
import matplotlib.pyplot as plt

from matplotlib.patches import Rectangle

obstacles1 = [
    [0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 0, 0, 0, 1, 1, 0, 0],
    [0, 1, 1, 0, 0, 0, 1, 1, 0, 0],
    [0, 1, 1, 0, 0, 0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 1, 0, 0],
]


def obstacles_str():
    rows = ["".join(["-" if point is 0 else "#" for point in row]) for row in obstacles1]
    return "\n".join(rows)


obstacles2 = [(x, y) for x in range(10) for y in range(10) if obstacles1[y][x] is 1]

graph = Graph(10, 10, obstacles2)
p = graph.find_path((0, 0), (9, 9))
print(graph.graph_to_str((0, 0), (9, 9)))


def plot_graph():
    def split_axes(c):
        xs = [x for (x, _) in c]
        ys = [y for (_, y) in c]
        return [xs, ys]

    a = plt.gca()
    [xs, ys] = split_axes(graph.obstacles)
    zz = zip(xs, ys)

    for (x, y) in zz:
        a.add_patch(Rectangle((x - .7, y - .7), 1.4, 1.4, facecolor='red'))

    plt.axis([0, graph.width - 1, 0, graph.height - 1])
    [wxs, wys] = split_axes(p)
    plt.plot(wxs, wys, linewidth=10)
    plt.gca().invert_yaxis()
    plt.show()


