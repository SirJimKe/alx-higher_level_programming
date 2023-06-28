#!/usr/bin/python3
""" defines a node of a singly linked list """


class Node:
    """
    Represents a node of a singly linked list.

    The Node class provides a basic representation of a node, \
    which contains data and a reference to the next node.

    Attributes:
        __data (int): The data stored in the node.
        __next_node (Node): The reference to the next node.

    Methods:
        data(): Retrieves the data stored in the node.
        data(value): Sets the data stored in the node.
        next_node(): Retrieves the reference to the next node.
        next_node(value): Sets the reference to the next node.
    """
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """
    Represents a singly linked list.

    The SinglyLinkedList class provides a basic representation of a singly \
    linked list, which consists of nodes.

    Attributes:
        head (Node): The head node of the linked list.

    Methods:
        sorted_insert(value): Inserts a new Node into the correct sorted \
        position in the list (increasing order).
    """
    def __init__(self):
        self.head = None

    def sorted_insert(self, value):
        """
        Inserts a new Node into the correct sorted position in the list.

        Args:
            value (int): The value to be inserted.
        """
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
        elif value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next_node is not None and value >= \
                  current.next_node.data:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """
        Returns a string representation of the linked list.

        Returns:
            str: The string representation of the linked list.
        """
        result = ""
        current = self.head
        while current is not None:
            result += str(current.data) + "\n"
            current = current.next_node
        return result.strip()
