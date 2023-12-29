#print("At BNV")
import networkx as nx
import matplotlib.pyplot as plt
import configparser
import numpy as np
import ast

class BayesianNetwork(object):
    def __init__(self):
        pass


    def getGraphDetails(self,filePath):
        config =  configparser.ConfigParser()
        config.read(filePath)
        graph1EdgeList=""
        try:
            graph1EdgeList = config.get('Details', 'graph1')
        except configparser.Error as e:
            print(f"Error: {e}")
        print(graph1EdgeList)
        edge_list= tuple(ast.literal_eval(graph1EdgeList))
        G=nx.Graph()
        G.add_edges_from(edge_list)
        nx.draw_spring(G,with_labels=True)
        plt.show()

    #def graphCheckIfBayesian(self):




if __name__ == "__main__":
    print("The Bayesian Network is:")
    filePath = "/Users/prathyushamallela/Documents/ThesisLearning/ParticleFilter/bn_pythonproject/ConfigurationFile.ini"
    g1 = BayesianNetwork
    filePath1="ConfigurationFile.ini"
    g1.getGraphDetails(g1,filePath1)


