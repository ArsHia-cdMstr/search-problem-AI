from Pipe import Pipe
from Problem import Problem
from State import State
from Search import Search
import unittest
import logging

class TestSearch(unittest.TestCase):

    def test_1_bfs(self):
        test_path = 'tests/test1.txt'
    
        file = open(test_path, 'r')
        p = []
        for i in file.readlines():
            a = i.replace('\n', '')
            a = a.replace(' ', '')
            a = a.split(',')
            p.append(Pipe(a[:-1], int(a[-1])))

        s = Search.bfs(Problem(State(p, None, 0, (0, 0), 0)))
        s.print_path()
        # s.execute_gui()
    
    def test_2_dfs(self):
        test_path = 'tests/test2.txt'
    
        file = open(test_path, 'r')
        p = []
        for i in file.readlines():
            a = i.replace('\n', '')
            a = a.replace(' ', '')
            a = a.split(',')
            p.append(Pipe(a[:-1], int(a[-1])))

        s = Search.dfs(Problem(State(p, None, 0, (0, 0), 0)))
        s.print_path()
        # s.execute_gui()
    
    def test_1_ucs(self):
        test_path = 'tests/test1.txt'
    
        file = open(test_path, 'r')
        p = []
        for i in file.readlines():
            a = i.replace('\n', '')
            a = a.replace(' ', '')
            a = a.split(',')
            p.append(Pipe(a[:-1], int(a[-1])))

        s = Search.ucs(Problem(State(p, None, 0, (0, 0), 0)))
        s.print_path()
        # s.execute_gui()
    
    def test_2_ucs(self):
        test_path = 'tests/test2.txt'
    
        file = open(test_path, 'r')
        p = []
        for i in file.readlines():
            a = i.replace('\n', '')
            a = a.replace(' ', '')
            a = a.split(',')
            p.append(Pipe(a[:-1], int(a[-1])))

        s = Search.ucs(Problem(State(p, None, 0, (0, 0), 0)))
        s.print_path()
        # s.execute_gui()

        
    def test_2_limited_dfs():
        test_path = 'tests/test2.txt'
    
        file = open(test_path, 'r')
        p = []
        for i in file.readlines():
            a = i.replace('\n', '')
            a = a.replace(' ', '')
            a = a.split(',')
            p.append(Pipe(a[:-1], int(a[-1])))

        MAX_DEPTH = 10
        for i in range(MAX_DEPTH):
            s = Search.limited_dfs(Problem(State(p, None, 0, (0, 0))), i)
            try:    
                s.print_path()
            except AttributeError:
                logging.error({f"with depth of {i}, limited dfs has not find solution"})
        # s.execute_gui()
    
    def test_1_ids(self):
        test_path = 'tests/test1.txt'
    
        file = open(test_path, 'r')
        p = []
        for i in file.readlines():
            a = i.replace('\n', '')
            a = a.replace(' ', '')
            a = a.split(',')
            p.append(Pipe(a[:-1], int(a[-1])))

        s = Search.ids(Problem(State(p, None, 0, (0, 0), 0)))
        s.print_path()
        # s.execute_gui()
    
    def test_2_ids(self):
        test_path = 'tests/test2.txt'
    
        file = open(test_path, 'r')
        p = []
        for i in file.readlines():
            a = i.replace('\n', '')
            a = a.replace(' ', '')
            a = a.split(',')
            p.append(Pipe(a[:-1], int(a[-1])))

        s = Search.ids(Problem(State(p, None, 0, (0, 0), 0)))
        s.print_path()
        # s.execute_gui()