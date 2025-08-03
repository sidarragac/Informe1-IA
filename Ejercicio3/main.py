from collections import deque
import time, tracemalloc

def bfs(actions, initial, goal) -> None:
    class Node:
        def __init__(self, state, parent=None, action=None):
            self.state = state
            self.parent = parent
            self.action = action

    class Problem:
        def __init__(self, initial, goal, actions, result, is_goal):
            self.initial = initial
            self.goal = goal
            self.actions = actions
            self.result = result
            self.is_goal = is_goal

    def expand(problem, node):
        s = node.state
        for action in problem.actions(s):
            s_prime = problem.result(s, action)
            yield Node(state=s_prime, parent=node, action=action)
    
    def bfs_implementation(problem):
        initial_node = Node(state=problem.initial)
    
        frontier = deque([initial_node])
        explored = set()

        while frontier:
            node = frontier.popleft()
            if problem.is_goal(node.state):
                return node
            
            explored.add(node.state)
            
            for child in expand(problem, node):
                if child.state not in explored and child not in frontier:
                    frontier.append(child)

        return None
    
    def result(state, action):
        return action
    
    def is_goal(state):
        return state == goal
    
    problem = Problem(initial, goal, lambda s: actions.get(s, []), result, is_goal)

    solution = bfs_implementation(problem)

    if solution:
        path = []
        while solution:
            path.append(solution.state)
            solution = solution.parent
        path.reverse()
        print(f'Camino de {initial} a {goal} -> {path}')
    else:
        print(f'No se encontró un camino de {initial} a {goal}')

def bfs_execution(initial, goal, actions):
    tracemalloc.start()
    start_time = time.time()
    
    bfs(actions, initial, goal)
    
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    elapsed_time = time.time() - start_time
    print(f'Tiempo de ejecución: {elapsed_time:.6f} segundos')
    print(f'Memoria usada: {current / 10**6:.6f} MB; Pico de memoria: {peak / 10**6:.6f} MB')


def main():
    initial = input("Enter the initial state: ") or "A"
    goal = input("Enter the goal state: ") or "J"
    actions = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B', 'G'],
        'E': ['B', 'H', 'I'],
        'F': ['C', 'J'],
        'G': ['D'],
        'H': ['E'],
        'I': ['E', 'J'],
        'J': ['F', 'I']
    }
    bfs_execution(initial, goal, actions)


if __name__ == "__main__":
    main()