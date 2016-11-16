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
        self.mode = 'std'  # iso
        self.circumference = circumference
        self.mag_rigidity = 0.0
        self.acceptance = 0.0
        self.gamma_t = 1

    def get_alpha_p(self):
        return 1 / (self.gamma_t ** 2)

    @staticmethod
    def get_ring_dict():
        ring_dic = {}

        esr = Ring('ESR', 108.36)
        esr.acceptance = 0.024
        esr.gamma_t = 2.30  # STD Mode: 2.30 or 2.44 theoretical value, ISO: 1.4
        esr.mag_rigidity = 18
        ring_dic['ESR'] = esr

        cr = Ring('CR', 221.45)
        cr.mag_rigidity = 13
        ring_dic['CR'] = cr

        csre = Ring('CSRe', 108.36)
        csre.mag_rigidity = 18
        ring_dic['CSRe'] = csre

        ring_dic['CRYRING'] = Ring('CRYRING', 54.17)

        ring_dic['CSR'] = Ring('CSR', 35)

        ring_dic['HESR'] = Ring('HESR', 442.5)

        ring_dic['TSR'] = Ring('TSR', 55.4)

        ring_dic['RI-RING'] = Ring('RI-RING', 60.0)

        return ring_dic
