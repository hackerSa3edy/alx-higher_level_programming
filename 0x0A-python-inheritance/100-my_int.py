#!/usr/bin/python3
"""
100-my_int module

Initiates a MyInt class that inherits from int class.
"""



class MyInt(int):
    """MyInt

    Arguments:
        int -- parent class
    """
    def __eq__(self, __value: object) -> bool:
        """__eq__

        Arguments:
            __value -- The other object

        Returns:
            True if self object != __value, False otherwise
        """
        return super().__ne__(__value)


    def __ne__(self, __value: object) -> bool:
        """__ne__

        Arguments:
            __value -- The other object

        Returns:
            True if self object == __value, False otherwise
        """
        return super().__eq__(__value)
