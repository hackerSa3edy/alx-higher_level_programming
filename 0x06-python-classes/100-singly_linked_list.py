#!/usr/bin/python3
"""100-singly_linked_list.py module

Raises:
    TypeError: data must be an integer

Returns:
    Create a single linked list
"""

class Node():
    """Linked list node
    """
    def __init__(self, data, next_node=None):
        """Initialize variables

        Arguments:
            data -- data to be assigned to the node

        Keyword Arguments:
            next_node -- pointer to the next node (default: {None})
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """data attr getter

        Returns:
            returns the data attribute
        """
        return self.__data

    @data.setter
    def data(self, value):
        """data attr setter

        Arguments:
            value -- value to be assigned to the data attribute

        Raises:
            TypeError: data must be an integer
        """
        if type(value) is not int:
            raise TypeError('data must be an integer')
        self.__data = value

    @property
    def next_node(self):
        """next_node attr getter

        Returns:
            pointer to the next node
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """next_node attr setter

        Arguments:
            value -- value to be assigned to the next_node attribute

        Raises:
            TypeError: next_node must be a Node object
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError('next_node must be a Node object')
        self.__next_node = value


class SinglyLinkedList():
    """Create a single linked list
    """
    def __init__(self):
        """Initialize variables
        """
        self.__head = None

    def __str__(self):
        """Readable string representation for the class

        Returns:
            All the list
        """
        self.__list = []
        self.__tempNode = self.__head
        while self.__tempNode != None:
            self.__list.append(self.__tempNode.data)
            print("print list: {}".format(self.__tempNode.data))
            self.__list.append("\n")
            self.__tempNode = self.__tempNode.next_node
        return "".join(self.__list)

    def sorted_insert(self, value):
        """insert value in its sorted place

        Arguments:
            value -- the value to be assigned to the new node
        """
        pass
