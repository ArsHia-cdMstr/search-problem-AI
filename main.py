from Pipe import Pipe
from Problem import Problem
from State import State
from Search import Search

if __name__ == '__main__':
    test_path = 'tests/test4.txt'
    # test_path = 'tests/test3.txt'
    
    file = open(test_path, 'r')
    p = []
    for i in file.readlines():
        a = i.replace('\n', '')
        a = a.replace(' ', '')
        a = a.split(',')
        p.append(Pipe(a[:-1], int(a[-1])))

    global_init_status = State(p, None, 0, (0, 0), 0)

    t_path = 'tests/goal1.txt'

    file = open(test_path, 'r')
    p1 = []
    for i in file.readlines():
        a = i.replace('\n', '')
        a = a.replace(' ', '')
        a = a.split(',')
        p1.append(Pipe(a[:-1], int(a[-1])))

    global_goal_status = State(p1, None, 0, (0, 0), 0)

    s = Search.BDS(Problem(State(p, None, 0, (0, 0), 0)), global_goal_status)
    s.print_path()
    # s.execute_gui()
