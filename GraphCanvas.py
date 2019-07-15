
"""
    Description:
        Elementary classes to draw simple undirected graphs on a tkinter Canvas
    Author:
        Edson Kropniczki - (c) jul/2019 - all rights reserved
    License:
        just keep this header in your copy and feel free to mess up with this code as you wish;
        source code also publicly available at https://github.com/webargus/MatematicaDiscretaIII;
        actually, accretions and improvements are more than welcome! :)
    Disclaimer:
        No liabilities or warrants whatsoever granted, as usual. Use it on your own risk!
"""

from tkinter import *
import Graph
import EdgeDistanceDlg as EdgeDlg


class GraphCanvas:

    node_radius = 15                        # static integer for graphic vertex circle radius
    font = ("Arial", 10, "bold")            # static font for graph texts

    def __init__(self, frame, callback):

        self.callback = callback            # parent callback to work Dijkstra thing on graph
        self.graph = Graph.Graph()          # Graph obj to accumulate nodes created
        self.sel = None                     # pointer to selected nodes for edging
        self.sel_tags = []                  # array to track selection tags
        self.edit_flag = True               # flag to enable/disable graph editing
        self.arrow = PhotoImage(file='arrow16.png')  # img to highlight node selection

        self.canvas = Canvas(frame, background="white")
        self.canvas.grid(row=0, column=0, sticky=NSEW)

        self.canvas.bind('<Button-1>', self._handle_click)
        self.canvas.bind('<Control-1>', self._dijkstra)

    def _handle_click(self, event, ctrl=False):
        if not self.edit_flag:
            return
        # try to get node under mouse click
        node = self._in_node(event.x, event.y)
        # create fresh node if user clicked on blank canvas
        if node is None:
            self._create_node(event.x, event.y)
            self.remove_tags()                     # unselect node if any selected
            return
        # select 1st node otherwise
        if self.sel is None:
            self.sel = node
            self._draw_tag(node)
            return
        elif self.sel == node:
            # clicked on same node, cancel selection
            self.remove_tags()
            return
        # user clicked on 2nd node => selection complete
        self.sel = (self.sel, node)
        self._draw_tag(node)
        if ctrl:
            self.edit_flag = False
            self.callback(self.sel, self.graph)             # do Dijkstra stuff
        else:
            # edge drawing
            self._edge()

    def _dijkstra(self, event):
        self._handle_click(event, True)

    def _edge(self):
        n1, n2 = self.sel
        # abort if edge between nodes already exists
        if n1.get_edge(n2) is not None:
            self.remove_tags()
            return
        # prompt user to input distance
        EdgeDlg.EdgeDistanceDlg(self.canvas,
                                "Aresta %d - %d" % (n1.node_id, n2.node_id),
                                self._draw_edge)

    def _draw_edge(self, dist):

        if dist is None:                                # user cancelled
            self.remove_tags()                          # unselect node pair
            return

        n1, n2 = self.sel                               # retrieve selected node pair
        n1.add_edge(n2, dist)                           # add edge between them
        self.canvas.create_line(n1.edge_border(n2),
                                n2.edge_border(n1),
                                width=1)
        self.canvas.create_text(n2.middle_point(n1),
                                font=GraphCanvas.font,
                                fill="red",
                                text=dist)
        self.remove_tags()                             # unselect node pair

    def _create_node(self, x, y):
        node = CanvasNode(x, y)
        self.graph.append(node)
        self.canvas.create_oval(x - GraphCanvas.node_radius,
                                y - GraphCanvas.node_radius,
                                x + GraphCanvas.node_radius,
                                y + GraphCanvas.node_radius,
                                fill="yellow")
        self.canvas.create_text(x, y, text=node.node_id, font=GraphCanvas.font, fill="blue")

    def _draw_tag(self, node):
        self.sel_tags.append(self.canvas.create_image(node.x + GraphCanvas.node_radius,
                                                      node.y - GraphCanvas.node_radius,
                                                      image=self.arrow))

    def remove_tags(self):
        self.sel = None
        for tag in self.sel_tags:
            self.canvas.delete(tag)
        del self.sel_tags[:]
        self.edit_flag = True

    def clear(self):
        self.canvas.delete("all")
        del self.graph[:]
        CanvasNode.node_id = 0
        self.edit_flag = True

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
        d = self.get_distance(other)
        # watch out! possible division by zero here!!
        xp = self.x + GraphCanvas.node_radius*abs(other.x - self.x)/d
        yp = self.y + GraphCanvas.node_radius*abs(other.y - self.y)/d
        if other.x < self.x:
            xp = self.x - (xp - self.x)
        if other.y < self.y:
            yp = self.y - (yp - self.y)
        return xp, yp

    def middle_point(self, other):
        xp = (other.x + self.x)/2
        yp = (other.y + self.y)/2
        return xp+5, yp+5

    def get_distance(self, other):
        return ((other.x - self.x)**2 + (other.y - self.y)**2)**.5


