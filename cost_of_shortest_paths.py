import math

class Solution:
    def __init__(self, origin, incoming_edges, outgoing_edges):
        self.origin = origin
        self.incoming_edges = incoming_edges
        self.outgoing_edges = outgoing_edges
        self.distance = dict()
        self.pred = dict()

    def relax(self,u,v,w):
        if self.distance[u] != math.inf and self.distance[u] + w < self.distance[v]:
            self.distance[v] = self.distance[u] + w
            self.pred[v] = u

    def output(self):
        ############### YOUR CODE GOES HERE ##################
        count = 0
        while count < len(self.outgoing_edges):
            self.distance[count] = math.inf
            self.pred[count] = None
            count = count + 1
        
        self.distance[self.origin] = 0
        count = 1
        while count < len(self.outgoing_edges):
            count2 = 0
            while count2 < len(self.outgoing_edges):
                for incomingNode in self.incoming_edges[count2]:
                    w = self.incoming_edges[count2][incomingNode]
                    self.relax(incomingNode,count2,w)
                count2 = count2 + 1
            count = count + 1
        
        return list(self.distance.values())
