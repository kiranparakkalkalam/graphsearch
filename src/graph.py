from __future__ import absolute_import
#
# Graph class to represen the graph in adjcency matrix
#
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

from settings import BASE_DIR

class Graph:
    '''
    This class represents the graph, which is read from a file.
    The file contains the adjcency matrix representation of the graph.
    '''
    def __init__(self, filename=None):
        self._graph = []
        # If the adjecency matrix is available
        if filename:
            with open(filename, "r") as fw:
                rows = fw.read().splitlines()
                for row in rows:
                    self._graph.append([int(each) for each in row.split(" ")])
                    #self._graph.append(list(map(lambda x: int(x), row.split(" "))))
            self._graph = np.array(self._graph)

    def visualize(self):
        '''Use numpy, networkx to plot the graph.'''
        self._adj_matrix = nx.from_numpy_matrix(self._graph)
        nx.draw_networkx(self._adj_matrix, with_labels=True)
        plt.show()


    def repr(self):
        ''' Print the adjcency matrix'''
        print(self._graph)
