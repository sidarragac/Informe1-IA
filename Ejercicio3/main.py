from collections import deque
import time, tracemalloc

def medicion_rendimiento(func):
    def wrapper(*args, **kwargs):
        tracemalloc.start()
        start_time = time.time()
        
        result = func(*args, **kwargs)
        
        _, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        
        elapsed_time = time.time() - start_time
        print(f'Tiempo de ejecución: {elapsed_time:.6f} segundos')
        print(f'Pico de memoria: {peak / 10**6:.6f} MB')
        
        return result
    return wrapper

@medicion_rendimiento
def bfs(initial, goal, actions):
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

@medicion_rendimiento
def ids(initial, goal, actions):
    class Node:
        def __init__(self, state, parent=None, action=None, depth=0):
            self.state = state
            self.parent = parent
            self.action = action
            self.depth = depth
        
    class Problem:
        def __init__(self, initial, goal, actions, result, is_goal):
            self.initial = initial
            self.goal = goal
            self.actions = actions
            self.result = result
            self.is_goal = is_goal
    
    def expand(problem, node):
        children = []
        for action in problem.actions(node.state):
            child_state = problem.result(node.state, action)
            child_node = Node(child_state, parent=node, action=action, depth=node.depth + 1)
            children.append(child_node)
        return children
    
    def is_cycle(node):
        current = node.parent
        while current is not None:
            if current.state == node.state:
                return True
            current = current.parent
        return False

    def depth_limited_search(problem, limit):
        frontier = deque([Node(problem.initial)])
        result = None

        while frontier:
            node = frontier.pop()

            if problem.is_goal(node.state):
                return node

            if node.depth > limit:
                result = 'cutoff'
            else:
                for child in expand(problem, node):
                    if not is_cycle(child):
                        frontier.append(child)

        return result
    
    def ids_implementation(problem):
        for depth in range(10):
            result = depth_limited_search(problem, depth)
            if result != 'cutoff':
                return result
        return None
    
    def result(state, action):
        return action
    
    def is_goal(state):
        return state == goal
    
    problem = Problem(initial, goal, lambda s: actions.get(s, []), result, is_goal)

    solution = ids_implementation(problem)

    if solution:
        path = []
        while solution:
            path.append(solution.state)
            solution = solution.parent
        path.reverse()
        print(f'Camino de {initial} a {goal} -> {path}')
    else:
        print(f'No se encontró un camino de {initial} a {goal}')

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
    bfs(initial, goal, actions)
    ids(initial, goal, actions)


if __name__ == "__main__":
    main()