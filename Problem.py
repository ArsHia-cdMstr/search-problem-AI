import copy
import inspect
from State import State


class Problem:
    def __init__(self, *args):
        self.path_cost = [1, 1, 1, 1]
        if type(args[0]) == State:
            self.initState = args[0]
        else:
            self.initState = State(args[0], args[1])
        if type(args[-1]) == list:
            self.set_path_cost(args[-1])

    @staticmethod
    def is_goal(state: State) -> bool:  # this method check this state is goal or not
        for i in state.pipes:
            if not i.is_one_color() or (not (i.is_full() or i.is_empty())):
                return False
        return True

    def _can_move(self, state, i, j) -> bool:
        return not state.pipes[j].is_full() and not state.pipes[i].is_empty()
    
    # this method for every state gives every possible states form this self and return it
    def successor(self, state: State) -> list:
        child = []
        for i in range(len(state.pipes)):
            for j in range(len(state.pipes)):
                if i == j:
                    continue
                if self._can_move(state, i, j):
                    # want's todo: get the caller_name, if ucs
                    # curframe = inspect.currentframe()
                    # calframe = inspect.getouterframes(curframe, 2)
                    # caller_name = calframe[1][3]
                    # self.get_cost_from_change_ucs(state, i, j), (i, j), state.depth+1)
                    s = State(
                            copy.deepcopy(state.pipes), state, 
                            self.get_cost_from_change(state, i),
                            (i, j), state.depth+1)
                    s.change_between_two_pipe(i, j)
                    child.append(s)
        return child

    @staticmethod
    def print_state(state: State):
        for i in state.pipes:
            i.print_pipe()

    @staticmethod
    def get_state_for_gui(state: State):
        out = ""
        for i in range(len(state.pipes)):
            out += 'p' + str(i + 1) + '=' + state.pipes[i].get_pipe_for_gui() + ','
        out = out[:len(out) - 1] + '\n'
        return out

    def get_cost_from_change(self, state: State, pipe_src_ind: int) -> int:
        if state.pipes[pipe_src_ind].stack[-1] == 'red':
            return state.g_n + self.path_cost[0]
        elif state.pipes[pipe_src_ind].stack[-1] == 'blue':
            return state.g_n + self.path_cost[1]
        elif state.pipes[pipe_src_ind].stack[-1] == 'green':
            return state.g_n + self.path_cost[2]
        elif state.pipes[pipe_src_ind].stack[-1] == 'yellow':
            return state.g_n + self.path_cost[3]
    
    def get_cost_from_change_ucs(self, state: State, pipe_src_ind: int, pipe_dis_ind: int):
        return state.g_n + abs(pipe_dis_ind - pipe_src_ind)

    def get_cost_from_change_heuristic(self, state):
        return self.path_cost[0] + state.f_n

    def set_path_cost(self, cost: list):
        self.path_cost = cost
