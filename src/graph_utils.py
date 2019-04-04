import random
import networkx as nx

from graph import Graph


def generate_random_graph(no_of_nodes, probability=0.5):
    '''
    This generates random graph based on the Erdos-Renyl G(N, P) model
    An edge exists between nodes for a probability P.
    :Parameters
    :no_of_nodes: <int> : No of vertices in the graph.
    :probability: <float>: Probability with which the edge exists. Def = 0.5
    :return: Graph
    '''
    random_graph = Graph()
    random_graph._graph = nx.to_numpy_matrix(nx.erdos_renyi_graph(
                                                    no_of_nodes, probability))
    return random_graph

