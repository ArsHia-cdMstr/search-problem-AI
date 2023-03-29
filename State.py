# from main import global_init_status
# this class only for the first time setup init state for problem and is given to every search
class State:
    def __init__(self, pipes: list, parent, g_n: int, prev_action: tuple, depth: int):
        self.pipes = pipes
        self.parent = parent
        self.g_n = g_n
        self.prev_action = prev_action
        self.depth = depth

    def change_between_two_pipe(self, pipe_src_ind: int, pipe_dest_ind: int):
        self.pipes[pipe_dest_ind].add_ball(self.pipes[pipe_src_ind].remove_ball())

    def __hash__(self):
        hash_strings = []
        for i in self.pipes:
            hash_strings.append(i.__hash__())
        hash_strings = sorted(hash_strings)
        hash_string = ''
        for i in hash_strings:
            hash_string += i + '###'
        return hash_string

    @property
    def h_n_1(self):
        total_happiness = 0

        for pipe in self.pipes:
            pipe_happiness = 0
            value = 1

            if len(pipe.stack) > 0: #if pipe is empty skip this part

                pipe_init_color = pipe.stack[0]  # the first ball of each pipe

                for ball in pipe.stack:
                    if ball == pipe_init_color:
                        pipe_happiness += value
                        value += 0.1
                    else:
                        break
            total_happiness += pipe_happiness + (pipe.limit - len(pipe.stack))

        return -total_happiness

    @property
    def f_n(self):
        return self.g_n + self.h_n_1

    # @property
    # def reverse_h(self):
    #     count = 0
    #     for i, init_pipe in zip(self.pipes, global_init_status.pipes):
    #         count += i.max_same_color_recursiveMode(init_pipe)
    #     return count
