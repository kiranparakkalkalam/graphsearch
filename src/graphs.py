#
# Graph class to represen the graph in adjcency matrix
#
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np


class Graph:
    '''
    This class represents the graph, which is read from a file.
    The file contains the adjcency matrix representation of the graph.
    '''
    def __init__(self, filename):
        self._graph = []
        with open(filename, "r") as fw:
            rows = fw.read().splitlines()
            for row in rows:
                self._graph.append([int(each) for each in row.split(" ")])
                #self._graph.append(list(map(lambda x: int(x), row.split(" "))))

    def visualize(self):
        '''Use numpy, networkx to plot the graph.'''
        # Get the numpy representation.
        self._adj_matrix = nx.from_numpy_matrix(np.array(self._graph))
        nx.draw_networkx(self._adj_matrix, with_labels=True)
        plt.show()


    def repr(self):
        ''' Print the adjcency matrix'''
        print(self._graph)

