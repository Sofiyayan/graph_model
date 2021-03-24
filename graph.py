class Node:
    def __init__(self, vertex: int):
        if not isinstance(vertex, int):
            raise TypeError("ERROR: Invalid annotation for vertex")
        self.vertex = vertex

    def __str__(self):
        return str(self.__dict__)

    def __repr__(self):
        return f"Node({self.vertex})"

    def __eq__(self, other):
        return self.vertex == other.vertex

    @staticmethod
    def vertices_dict(vertex_list: list):
        vertices_dict = {vertex.vertex: vertex for vertex in vertex_list}
        return vertices_dict


class Edge:
    def __init__(self, node_1: Node, node_2: Node, weight: int = 0):
        if node_1 == node_2:
            raise ValueError("ERROR: Graph should not contain loops")
        self.node_1 = Node(min([node_1.vertex, node_2.vertex]))
        self.node_2 = Node(max([node_1.vertex, node_2.vertex]))
        self.weight = weight

    def __str__(self):
        return f"{(self.node_1.vertex, self.node_2.vertex)}"

    def __repr__(self):
        return f"{self.node_1.vertex,self.node_2.vertex}"

    def to_tuple(self):
        return tuple([self.node_1.vertex, self.node_2.vertex])

    @staticmethod
    def edges_dict(edge_list: list):
        edges_dict = {edge.to_tuple(): edge.weight for edge in edge_list}
        return edges_dict


class Graph:
    def __init__(self, vertex_list: list, edge_list: list):
        self.vertices_dict = Node.vertices_dict(vertex_list)
        self.edges_dict = Edge.edges_dict(edge_list)
        self.neighbor_dict = Graph.__neighbor_dict_maker(vertex_list, edge_list)

    @staticmethod
    def __neighbor_dict_maker(vertex_list, edge_list):
        neighbor_dict = {vertex.vertex: [] for vertex in vertex_list}
        for edge in edge_list:
            neighbor_dict[edge.node_1.vertex].append(edge.node_2.vertex)
            neighbor_dict[edge.node_2.vertex].append(edge.node_1.vertex)
        return neighbor_dict

    def __str__(self):
        return str(self.__dict__)

    def add_vertex(self, i):
        if i in self.vertices_dict.keys():
            return "The vertex already exists"
        self.vertices_dict[i] = Node(i)
        self.neighbor_dict[i] = []

    def __delete_vertex_vertex(self, i):
        del self.vertices_dict[i]

    def __delete_vertex_edge(self, i):
        to_delete = []
        for key in self.edges_dict:
            if i in key:
                to_delete.append(key)
        for key in to_delete:
            del self.edges_dict[key]

    def __delete_vertex_neighbor(self, i):
        del self.neighbor_dict[i]

    def __delete_vertex_neighbors(self, i):
        for _, values in self.neighbor_dict.items():
            if i in values:
                values.remove(i)

    def delete_vertex(self, i):
        self.__delete_vertex_vertex(i)
        self.__delete_vertex_edge(i)
        self.__delete_vertex_neighbor(i)
        self.__delete_vertex_neighbors(i)

    def __add_edge_vertices(self, i, j):
        if i not in self.vertices_dict:
            self.add_vertex(i)
        if j not in self.vertices_dict:
            self.add_vertex(j)

    def __add_edge_edge(self, i, j, weight: int = 0):
        new_edge = Edge(Node(i), Node(j), weight)
        self.edges_dict[new_edge.to_tuple()] = new_edge.weight

    def __add_edge_neighbors(self, i, j):
        self.neighbor_dict[i].append(j)
        self.neighbor_dict[j].append(i)

    def add_edge(self, i, j, weight: int = 0):
        self.__add_edge_vertices(i, j)
        self.__add_edge_edge(i, j, weight)
        self.__add_edge_neighbors(i, j)

    def __contains__(self, item):
        if not isinstance(item, Graph):
            raise TypeError(f"ERROR: Expected {type(self)} found {type(item)}")

        for node in item.vertices_dict:
            if node not in self.vertices_dict:
                return False

        for edge in item.edges_dict:
            if edge not in self.edges_dict:
                return False

        return True


if __name__ == "__main__":
    graph = Graph(
        [Node(1), Node(2), Node(3)],
        [Edge(Node(1), Node(2)), Edge(Node(1), Node(2)), Edge(Node(1), Node(3), 5)],
    )
    graph_1 = Graph([Node(1), Node(2)], [Edge(Node(1), Node(2))])
    # print(graph in graph_1)
    # print(graph.vertices_dict)
    # graph.delete_vertex(2)
    # print(graph.edges_dict)
    # print(graph.neighbor_dict)
    # print(graph.vertices_dict)
    # print(">>>>>>>>>>>>>>>")
    # graph.add_edge(3,6,8)
    # print(graph.edges_dict)
    # print(graph.neighbor_dict)
    # print(graph.vertices_dict)
    # graph.delete_vertex(5)
    # print(graph.edges_dict)
    # print(graph.neighbor_dict)
    # print(graph.vertices_dict)
    # graph.add_edge(2, 1, 0)
    # print(graph.edges_dict)
