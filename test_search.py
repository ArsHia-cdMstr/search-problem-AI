from Pipe import Pipe
from Problem import Problem
from State import State
from Search import Search
import unittest

class TestSearch(unittest.TestCase):

    def test_1_bfs():
        test_path = 'tests/test1.txt'
    
        file = open(test_path, 'r')
        p = []
        for i in file.readlines():
            a = i.replace('\n', '')
            a = a.replace(' ', '')
            a = a.split(',')
            p.append(Pipe(a[:-1], int(a[-1])))

        s = Search.bfs(Problem(State(p, None, 0, (0, 0))))
        s.print_path()
        s.execute_gui()
    
    def test_2_bfs():
        test_path = 'tests/test2.txt'
    
        file = open(test_path, 'r')
        p = []
        for i in file.readlines():
            a = i.replace('\n', '')
            a = a.replace(' ', '')
            a = a.split(',')
            p.append(Pipe(a[:-1], int(a[-1])))

        s = Search.bfs(Problem(State(p, None, 0, (0, 0))))
        s.print_path()
        s.execute_gui()