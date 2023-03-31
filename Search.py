from Solution import Solution
from Problem import Problem
from datetime import datetime

import math


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
            state = priority_queue.pop()
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

        cuttoff = 10000
        while True:
            cuttoff *= 2
            while len(priority_queue) > 0:
                priority_queue.sort(key=lambda x: x.f_n, reverse=True)
                state = priority_queue.pop()
                hashed_state = state.__hash__()
                explored[hashed_state] = state
                neighbors = prb.successor(state)
                for c in neighbors:
                    if c.f_n > cuttoff:
                        continue
                    if prb.is_goal(c):
                        return Solution(c, prb, start_time)
                    if c.__hash__() not in explored:
                        priority_queue.append(c)
        return None

    @staticmethod
    def BDS(prb: Problem) -> Solution:

        start_time = datetime.now()

        i_explored = {}
        g_explored = {}

        i_stack = []
        g_stack = []

        I_state = prb.initState
        i_stack.append(I_state)

        G_state = Search.RBFS(prb).state
        g_stack.append(G_state)

        while len(i_stack) and len(g_stack):

            fring_list_i2g = prb.successor(i_stack.pop())
            fring_list_g2i = prb.successor(g_stack.pop())

            for c1 in fring_list_i2g:
                if c1.__hash__() not in i_explored:
                    i_explored[c1.__hash__()] = c1
                    i_stack.append(c1)
                    for c2 in fring_list_g2i:
                        if c2.__hash__() not in g_explored:
                            g_explored[c2.__hash__()] = c2
                            g_stack.append(c2)
                            if c1.__hash__() == c2.__hash__():
                                return Solution(G_state, prb, start_time)
        print("fail")
