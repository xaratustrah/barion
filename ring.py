"""
Barion

-- GUI Application --

Jul 2015 Xaratustrah
Mar 2016 Xaratustrah


"""


class Ring(object):
    """
    Class representing a storage ring
    """

    def __init__(self, name, circumference):
        self.name = name
        self.circumference = circumference
        self.mag_rigidity = 0.0
        self.acceptance = 0.0
        self.gamma_t = 0

    def get_alpha_p(self):
        return 1 / (self.gamma_t ** 2)
