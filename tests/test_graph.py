from __future__ import absolute_import
#
# Unit tests for Graph.
#

import os
import unittest
import numpy as np

from settings import BASE_DIR
from src.graph import Graph

DATA_FILE_PATH="graphsearch/tests/data/"

class TestGraph(unittest.TestCase):

    def setUp(self):
        pass

    def test_graph_initialization(self):
        input_file = os.path.join(BASE_DIR, DATA_FILE_PATH,
                                  'small_graph.txt')
        graph = Graph(input_file)
        first_row = np.array([0, 1, 1])
        self.assertEqual(len(graph._graph), 3)
        np.testing.assert_array_equal(graph._graph[0], first_row)


if __name__ == "__main__":
    unittest.main()

