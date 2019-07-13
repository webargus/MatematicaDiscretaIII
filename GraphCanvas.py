
"""
    Description:
        Elementary classes to draw simple undirected graphs on a tkinter Canvas
    Author:
        Edson Kropniczki - (c) jul/2019 - all rights reserved
    License:
        just keep this header in your copy and feel free to mess up with this code as you wish;
        project open source available at https://github.com/webargus/MatematicaDiscretaIII;
        actually, accretions and improvements are more than welcome!
    Disclaimer:
        use it on your own risk! No liabilities or warrants granted!
"""

from tkinter import *
import Graph


class GraphCanvas:

    node_radius = 15

    def __init__(self, frame):

        self.graph = Graph.Graph()
        self.prev_sel = None

        self.canvas = Canvas(frame)
        self.canvas.grid(row=0, column=0, sticky=NSEW)

        self.canvas.bind('<Button-1>', self.__handle_click)

    def __handle_click(self, event):
        # create new node if user clicked on blank
        node = self._in_node(event.x, event.y)
        if node is None:
            self._create_node(event.x, event.y)
            return
        # select node otherwise
        print(node)
        if self.prev_sel is None:
            self.prev_sel = node
            print("1st node selected: %s" % node)
            return
        elif self.prev_sel == node:
            # clicked on same node, cancel selection
            self.prev_sel = None
            return
        # draw edge
        print("edge from %s to %s" % (self.prev_sel, node))
        self._draw_edge(node)
        self.prev_sel = None

    def _draw_edge(self, node):
        print(self.prev_sel.edge_border(node))
        print(node.edge_border(self.prev_sel))
        self.canvas.create_line(self.prev_sel.edge_border(node),
                                node.edge_border(self.prev_sel),
                                width=3)

    def _create_node(self, x, y):
        node = CanvasNode(x, y)
        self.graph.append(node)
        self.canvas.create_oval(x - GraphCanvas.node_radius,
                                y - GraphCanvas.node_radius,
                                x + GraphCanvas.node_radius,
                                y + GraphCanvas.node_radius,
                                fill="yellow")
        self.canvas.create_text(x, y, text=node.node_id)

    def _in_node(self, x, y):
        for node in self.graph:
            if node.in_node(x, y):
                return node
        return None


class CanvasNode(Graph.Node):

    node_id = 0

    def __init__(self, x, y):
        CanvasNode.node_id += 1
        super(CanvasNode, self).__init__(CanvasNode.node_id)
        self.x = x
        self.y = y

    def in_node(self, x, y):
        return ((self.x - x)**2 + (self.y - y)**2)**.5 <= 2*GraphCanvas.node_radius

    def edge_border(self, other):
        d = ((other.x - self.x)**2 + (other.y - self.y)**2)**.5
        # watch out! possible division by zero here!!
        xp = self.x + GraphCanvas.node_radius*abs(other.x - self.x)/d
        yp = self.y + GraphCanvas.node_radius*abs(other.y - self.y)/d
        if other.x < self.x:
            xp = self.x - (xp - self.x)
        if other.y < self.y:
            yp = self.y - (yp - self.y)
        return xp, yp





