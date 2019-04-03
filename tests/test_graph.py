from __future__ import absolute_import
#
# Unit tests for Graph.
#

import os
import unittest

from settings import BASE_DIR
from src.graph import Graph


class TestGraph(unittest.TestCase):

    def setUp(self):
        pass

    def test_graph_initialization(self):
        input_file = os.path.join(BASE_DIR, 'graphsearch/tests/data/',
                                  'small_graph.txt')
        graph = Graph(input_file)
        first_row = [0, 1, 1]
        self.assertEqual(len(graph._graph), 3)
        self.assertListEqual(graph._graph[0], first_row)


if __name__ == "__main__":
    unittest.main()

