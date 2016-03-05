"""
Barion

-- GUI Application --

Jul 2015 Xaratustrah
Mar 2016 Xaratustrah


"""

from abc import ABCMeta, abstractmethod


class UI_Interface(object):
    """
    Abstract class definition as an interface between Model and View in the MVC scheme
    """
    __metaclass__ = ABCMeta

    @abstractmethod
    def show_message(self, text):
        """
        A method for showing a line of text
        :param text:
        :return:
        """
        pass

    @abstractmethod
    def show_message_box(self, text):
        """
        A method for showing a message box with a text inside
        :param text:
        :return:
        """
        pass
