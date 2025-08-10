import heapq

class Node:
    def __init__(self, state, parent=None, action=None, path_cost=0):
        self.state = state 
        self.parent = parent 
        self.action = action 
        self.path_cost = path_cost  

    def __lt__(self, other): 
        return self.path_cost < other.path_cost

def expand(problem, node, action_costs):
    for action in problem.actions(node.state): 
        next_state = problem.result(node.state, action)
        cost = problem.action_cost(node.state, action, next_state, action_costs)
        yield Node(next_state, node, action, node.path_cost + cost)

class Problem:
    def __init__(self, initial, goal, actions, result, action_cost, is_goal, target_distance):
        self.initial = initial 
        self.goal = goal 
        self.actions = actions 
        self.result = result 
        self.action_cost = action_cost 
        self.is_goal = is_goal
        self.target_distance = target_distance

def result(state, action):
    return action

def action_cost(state, action, result, action_costs): 
    return action_costs.get((state, action), action_costs.get((action, state), float('inf')))

def is_goal(state, goal):
    return state == goal

def h(node, target_distance):
    return target_distance.get(node.state, float('inf'))

def f(node, target_distance):
    return node.path_cost + h(node, target_distance)  

def A_algorithm(problem, goal, action_costs):
    nodo_inicio = Node(problem.initial)
    frontera = []
    heapq.heappush(frontera, (f(nodo_inicio, problem.target_distance), nodo_inicio))
    explorados = set()

    while frontera:
        _, nodo_actual = heapq.heappop(frontera)

        if problem.is_goal(nodo_actual.state, goal):
            return nodo_actual

        explorados.add(nodo_actual.state)

        for hijo in expand(problem, nodo_actual, action_costs):
            if hijo.state not in explorados:
                heapq.heappush(frontera, (f(hijo, problem.target_distance), hijo))

    return None


def main():
    initial = 'Arad'
    goal = 'Bucharest'

    actions = {
        'Arad': ['Sibiu', 'Timisoara', 'Zerind'],
        'Sibiu': ['Arad', 'Fagaras', 'Rimnicu Vilcea'],
        'Timisoara': ['Arad', 'Lugoj'],
        'Zerind': ['Arad', 'Oradea'],
        'Fagaras': ['Sibiu', 'Bucharest'],
        'Rimnicu Vilcea': ['Sibiu', 'Pitesti', 'Craiova'],
        'Lugoj': ['Timisoara', 'Mehadia'],
        'Oradea': ['Zerind', 'Sibiu'],
        'Pitesti': ['Rimnicu Vilcea', 'Bucharest'],
        'Craiova': ['Rimnicu Vilcea', 'Drobeta', 'Pitesti'],
        'Mehadia': ['Lugoj', 'Drobeta'],
        'Drobeta': ['Mehadia', 'Craiova'],
        'Bucharest': ['Fagaras', 'Pitesti', 'Urziceni', 'Giurgiu'],
        'Giurgiu': ['Bucharest'],
        'Urziceni': ['Bucharest', 'Hirsova', 'Vaslui'],
        'Hirsova': ['Urziceni', 'Eforie'],
        'Eforie': ['Hirsova'],
        'Vaslui': ['Urziceni', 'Iasi'],
        'Iasi': ['Vaslui', 'Neamt'],
        'Neamt': ['Iasi']
    }

    action_costs = {
        ('Arad', 'Sibiu'): 140, ('Arad', 'Timisoara'): 118, ('Arad', 'Zerind'): 75,
        ('Sibiu', 'Fagaras'): 99, ('Sibiu', 'Rimnicu Vilcea'): 80,
        ('Timisoara', 'Lugoj'): 111, ('Zerind', 'Oradea'): 71,
        ('Fagaras', 'Bucharest'): 211, ('Rimnicu Vilcea', 'Pitesti'): 97,
        ('Rimnicu Vilcea', 'Craiova'): 146, ('Lugoj', 'Mehadia'): 70,
        ('Oradea', 'Sibiu'): 151, ('Pitesti', 'Bucharest'): 101,
        ('Craiova', 'Drobeta'): 120, ('Craiova', 'Pitesti'): 138,
        ('Mehadia', 'Drobeta'): 75, ('Bucharest', 'Urziceni'): 85,
        ('Bucharest', 'Giurgiu'): 90, ('Urziceni', 'Hirsova'): 98,
        ('Urziceni', 'Vaslui'): 142, ('Hirsova', 'Eforie'): 86,
        ('Vaslui', 'Iasi'): 92, ('Iasi', 'Neamt'): 87
    }

    target_distance = {
        'Arad': 366, 'Bucharest': 0, 'Craiova': 160, 'Drobeta': 242, 'Eforie': 161,
        'Fagaras': 176, 'Giurgiu': 77, 'Hirsova': 151, 'Iasi': 226, 'Lugoj': 244,
        'Mehadia': 241, 'Neamt': 234, 'Oradea': 380, 'Pitesti': 100, 'Rimnicu Vilcea': 193,
        'Sibiu': 253, 'Timisoara': 329, 'Urziceni': 80, 'Vaslui': 199, 'Zerind': 374
    }

    problem = Problem(initial, goal, lambda s: actions.get(s, []), result, action_cost, is_goal, target_distance)
    solution = A_algorithm(problem, goal, action_costs)

    if solution:
        path = []
        while solution:
            path.append(solution.state)
            solution = solution.parent
        path.reverse()
        print("Solution path:", path)
    else:
        print("No solution found")


if __name__ == "__main__":
    main()