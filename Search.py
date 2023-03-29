from Solution import Solution
from Problem import Problem
from datetime import datetime


class Search:
    def __init__(self) -> None:
        self.test = "Dfsafa"

    @staticmethod
    def bfs(prb: Problem) -> Solution:  # this method get a first state of Problem and do bfs for find solution if no
        # solution is find return None else return the solution
        start_time = datetime.now()
        queue = []
        state = prb.initState
        queue.append(state)
        while len(queue) > 0:
            state = queue.pop(0)
            neighbors = prb.successor(state)
            for c in neighbors:
                if prb.is_goal(c):
                    return Solution(c, prb, start_time)
                queue.append(c)
        return None

    @staticmethod
    def dfs(prb: Problem) -> Solution:
        start_time = datetime.now()
        stack = []
        explored = {}
        state = prb.initState
        stack.append(state)
        while len(stack) > 0:
            state = stack.pop(-1)
            hashed_state = state.__hash__()
            if hashed_state not in explored:
                explored[hashed_state] = state
                neighbors = prb.successor(state)
                for c in neighbors:
                    if prb.is_goal(c):
                        return Solution(c, prb, start_time)
                    if c.__hash__() not in explored:
                        stack.append(c)
        return None

    @staticmethod
    def limited_dfs(prb: Problem, limit) -> Solution:
        start_time = datetime.now()
        explored = {}
        stack = []
        state = prb.initState
        stack.append(state)
        while len(stack) > 0:
            state = stack.pop(-1)
            hashed_state = state.__hash__()
            if hashed_state not in explored:
                explored[hashed_state] = state
                neighbors = prb.successor(state)
                for c in neighbors:
                    if c.__hash__() not in explored:
                        if c.depth > limit:
                            break
                        if prb.is_goal(c):
                            return Solution(c, prb, start_time)
                        stack.append(c)
        return None

    @staticmethod
    def ids(prb: Problem) -> Solution:
        start_time = datetime.now()
        d = 0
        while True:
            explored = {}
            stack = []
            state = prb.initState
            stack.append(state)
            while len(stack) > 0:
                state = stack.pop(-1)
                state_hash = state.__hash__()
                if state_hash not in explored:
                    explored[state_hash] = state
                    neighbors = prb.successor(state)
                    for c in neighbors:
                        if c.depth > d:
                            break
                        if prb.is_goal(c):
                            return Solution(c, prb, start_time)
                        if c.__hash__() not in explored:
                            stack.append(c)
            d += 1

    @staticmethod
    def ucs(prb: Problem) -> Solution:
        start_time = datetime.now()
        queue = []
        explored = {}
        state = prb.initState
        queue.append(state)
        while len(queue) > 0:
            queue.sort(key=lambda x: x.g_n)
            state = queue.pop(0)
            hashed_state = state.__hash__()
            if hashed_state not in explored:
                explored[hashed_state] = state
                neighbors = prb.successor(state)
                for c in neighbors:
                    if c.__hash__() not in explored:
                        if prb.is_goal(c):
                            return Solution(c, prb, start_time)
                        queue.append(c)
        return None

    @staticmethod
    def heuristic_A_star(prb: Problem) -> Solution:
        start_time = datetime.now()
        priority_queue = []
        explored = {}
        state = prb.initState
        priority_queue.append(state)
        while len(priority_queue) > 0:
            priority_queue.sort(key=lambda x: x.f_n, reverse=True)
            state = priority_queue.pop(0)
            hashed_state = state.__hash__()
            if hashed_state not in explored:
                explored[hashed_state] = state
                neighbors = prb.successor(state)
                for c in neighbors:
                    if c.__hash__() not in explored:
                        if prb.is_goal(c):
                            return Solution(c, prb, start_time)
                        priority_queue.append(c)
        return None

    @staticmethod
    def heuristic_iterative_A_star(prb: Problem) -> Solution:
        start_time = datetime.now()
        priority_queue = []
        explored = {}
        state = prb.initState
        priority_queue.append(state)
        while len(priority_queue) > 0:
            priority_queue.sort(key=lambda x: x.f_n, reverse=True)
            state = priority_queue.pop(0)
            cuttoff = state.f_n
            hashed_state = state.__hash__()
            explored[hashed_state] = state
            neighbors = prb.successor(state)
            for c in neighbors:
                if prb.is_goal(c):
                    return Solution(c, prb, start_time)
                if c.__hash__() not in explored:
                    priority_queue.append(c)
        return None

    @staticmethod
    def RBFS(prb: Problem) -> Solution:
        explored = {}
        state = prb.initState
        explored[state.__hash__()] = state

        return Search.RBFS_helper(prb, state, explored, state.h_n_1)

    @staticmethod
    def RBFS_helper(prb: Problem, parent_state, explored, h_value):
        start_time = datetime.now()
        children = prb.successor(parent_state)
        children.sort(key=lambda x: x.h_n_1)

        for j in range(len(children)):
            state = children[j]

            if state.h_n_1 >= h_value:
                for z in range(j):
                    st = children[z]
                    if st.__hash__() in explored:
                        explored.pop(st.__hash__())
                return None

            hashed_state = state.__hash__
            if hashed_state not in explored:
                if prb.is_goal(state):
                    return Solution(state, prb, start_time)
                explored[hashed_state] = state

            s = Search.RBFS_helper(prb, state, explored, min(h_value, state.h_n_1))
            if type(s) == Solution:
                return s
