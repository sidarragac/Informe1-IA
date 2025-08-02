import heapq

class Node:
    def __init__(self, position, parent=None, action=None, path_cost=0):
        self.position = position
        self.parent = parent
        self.action = action
        self.path_cost = path_cost

    def __lt__(self, other):
        return self.path_cost < other.path_cost

class Problem:
    def __init__(self, start, end, actions):
        self.initial = start
        self.goal = end
        self.actions = actions

def find_exit(maze):
    start = (1, 1)
    goal = (1, 6)

    actions = {
        (-1, 0): "Up",
        (1, 0): "Down",
        (0, -1): "Left",
        (0, 1): "Right"
        }

    problem=Problem(start, goal, actions)

    def manhatan_distance(pos, goal):
        return abs(pos[0] - goal[0]) + abs(pos[1] - goal[1])

    def get_neighbors(pos):
        neighbors = {}
        for move in [x for x in problem.actions.keys()]:
            neighbor = (pos[0] + move[0], pos[1] + move[1])
            if maze[neighbor[0]][neighbor[1]] != "#":
              neighbors[neighbor] = problem.actions[move]
        return neighbors

    start_node = Node(start, path_cost=0)
    frontier = [(manhatan_distance(start, goal), start_node)]
    heapq.heapify(frontier)
    reached = {start: start_node}

    while frontier:
        _, node = heapq.heappop(frontier)
        if node.position == goal:
            return reconstruct_path(node)

        for neighbor, move in get_neighbors(node.position).items():
            new_cost = node.path_cost + 1
            if neighbor not in reached or new_cost < reached[neighbor].path_cost:
                reached[neighbor] = Node(neighbor, parent=node, action=move, path_cost=new_cost)
                heapq.heappush(frontier, (manhatan_distance(neighbor, goal), reached[neighbor]))

    return None

def reconstruct_path(node):
    path = []
    moves = []
    while node:
        path.append(node.position)
        moves.append(node.action)
        node = node.parent
    path.reverse()
    moves.reverse()
    moves = moves[1:]
    return path, moves

def main():
    maze = [
        ["#", "#", "#", "#", "#", "#", "#","#"],
        ["#", "S", "#", " ", "#", " ", "E","#"],
        ["#", " ", " ", " ", "#", " ", " ","#"],
        ["#", " ", "#", " ", " ", " ", "#","#"],
        ["#", "#", "#", "#", "#", "#", "#","#"],
        ["#", "#", "#", "#", "#", "#", "#","#"]
    ]
    path, moves = find_exit(maze)
    print("Path to exit:", path)
    print("Actions taken:", moves)

if __name__ == "__main__":
    main()