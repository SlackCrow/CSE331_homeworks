import heapq

class Solution:
    def __init__(self, start_node, end_node, graph):
        self.graph = graph
        self.start_node = start_node
        self.end_node = end_node

    def outputPath(self):
        distances = dict()
        # convert self.graph to more Dijkstra's algorithm friendly 
        for node, adj in self.graph.items():
            nodeToAdd = dict()
            count = 1
            while count < len(adj):
                eachAdj = adj[count]
                nodeToAdd[eachAdj] = self.graph[eachAdj][0]
                count = count + 1
            distances[node] = nodeToAdd
        return self.findShortestPath(self.start_node,self.end_node,distances)

    def findShortestPath(self,start,end,graph): 
        # generic Dijkstra's algorithm implementation using heapq
        checked = set()
        pqueue = [(0, start, [])]
        try:
            for _ in iter(int, 1):
                (weight, st, path) = heapq.heappop(pqueue)
                if st not in checked:
                    checked.add(st)
                    path = path + [st]
                    if st == end:
                        return path
                    for (next, nc) in graph[st].items():
                        heapq.heappush(pqueue, (weight + nc, next, path))
        except IndexError: # there is no path between start and end
            return []