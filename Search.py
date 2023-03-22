from Solution import Solution
from Problem import Problem
from datetime import datetime
from custome_exceptions import BreakOuterLoopException

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
            if state.g_n > limit:
                limit += 1
                continue
            hashed_state = state.__hash__()
            explored[hashed_state] = state
            neighbors = prb.successor(state)
            for c in neighbors:
                if prb.is_goal(c):
                    return Solution(c, prb, start_time)
                if c.__hash__() not in explored:
                    stack.append(c)
        return None

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
            explored[hashed_state] = state
            neighbors = prb.successor(state)
            for c in neighbors:
                if prb.is_goal(c):
                    return Solution(c, prb, start_time)
                if c.__hash__() not in explored:
                    queue.append(c)
        return None
