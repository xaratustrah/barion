"""
Barion

-- GUI Application --

Jul 2015 Xaratustrah
Mar 2016 Xaratustrah


"""


class Particle(object):
    """
    Class Particle describes a valid nuclide
    """
    CC = 299792458  # m/s
    UU = 931.4940023  # MeV/C^2
    EE = 1.602176565e-19  # Coulombs
    ME = 0.510998928  # MeV/C^2

    def __init__(self, zz, nn, ame_data):
        """
        Constructor of the class
        :param zz: proton number
        :param nn: neutron number
        :param ame_data: an existing pointer to a table object
        :return:
        """
        self.ame_data = ame_data

        # variables with tbl in the name are direct readouts form the data file

        for i in self.ame_data.ame_table:
            if i[4] == zz and i[3] == nn:
                self.tbl_zz = i[4]
                self.tbl_nn = i[3]
                self.tbl_aa = i[5]
                self.tbl_name = i[6]
                self.tbl_massexcess_kev = i[8]
                self.tbl_massexcess_err_kev = i[9]
                self.tbl_binen_kev = i[10]
                self.tbl_bien_err_kev = i[11]
                self.tbl_betaen_kev = i[13]
                self.tbl_betaen_err_kev = i[14]
                self.tbl_am_microu = i[15] * 1e6 + i[16]
                self.tbl_am_err_microu = i[17]
                if i[0] == 'exp':
                    self.exp = True
                else:
                    self.exp = False

    def __str__(self):
        """
        Converts the particle to string
        :return:
        """
        return \
            str(self.tbl_aa) + '-' + \
            self.tbl_name + ', ' + \
            'Z: ' + str(self.tbl_zz) + ', ' + \
            'N:' + str(self.tbl_nn)

    def get_isotopes(self):
        """
        Retrieves the isotopes of the current nuclide
        :return:
        """
        p_array = []
        for i in self.ame_data.ame_table:
            if i[4] == self.tbl_zz:
                p = Particle(i[4], i[3], self.ame_data)
                p_array.append(p)
        return p_array

    def get_isotones(self):
        """
        Retrieves the isotones of the current nuclide
        :return:
        """
        p_array = []
        for i in self.ame_data.ame_table:
            if i[3] == self.tbl_nn:
                p = Particle(i[4], i[3], self.ame_data)
                p_array.append(p)
        return p_array

    def get_isobars(self):
        """
        Retrieves the isobars of the current nuclide
        :return:
        """
        p_array = []
        for i in self.ame_data.ame_table:
            if i[5] == self.tbl_aa:
                p = Particle(i[4], i[3], self.ame_data)
                p_array.append(p)
        return p_array

    def get_table_data(self):
        """
        Retrieves the data only from table, without calculations
        :return:
        """
        return \
            'Table Data: \n' + \
            str(self.tbl_aa) + '-' + self.tbl_name + ', ' + \
            'Z: ' + str(self.tbl_zz) + ', ' + \
            'N:' + str(self.tbl_nn) + ', ' + \
            '{source} \n'.format(source='** EXP **' if self.exp else '** SYS **') + \
            'Mass Excess [keV]: ' + str(self.tbl_massexcess_kev) + ' ± ' + str(self.tbl_massexcess_err_kev) + '\n' + \
            'Binding Energy [keV]: ' + str(self.tbl_binen_kev) + ' ± ' + str(self.tbl_bien_err_kev) + '\n' + \
            'Beta Decay Energy [keV]: ' + str(self.tbl_betaen_kev) + ' ± ' + str(self.tbl_betaen_err_kev) + '\n' + \
            'Atomic Mass [uU]: ' + str(self.tbl_am_microu) + ' ± ' + str(self.tbl_am_err_microu) + '\n'

    @staticmethod
    def to_mev(m_u):
        return m_u * Particle.UU

    @staticmethod
    def to_kg(m_u):
        return m_u * Particle.UU * 1.0e6 * Particle.EE / (Particle.CC ** Particle.CC)

    @staticmethod
    def to_u(m_mev):
        return m_mev / Particle.UU

    @staticmethod
    def get_total_charge(qq):
        return qq * Particle.EE

    @staticmethod
    def get_total_energy_mev():

         pass
    #
    # def get_gamma():
    #     pass
    #
    # def get_beta():
    #     pass
    #
    # def get_relativistic_mass():
    #     pass
    #
    # def get_relativistic_momentum():
    #     pass
    #
    # def get_magnetic_rigidity():
    #     pass
    #
    # def get_electric_rigidity():
    #     pass
    #
    # def get_velocity():
    #     pass
    #
    # def get_revolution_frequency():
    #     pass
    #
    # def get_revolution_harmonic():
    #     pass
    #
    # def get_number_of_ions():
    #     pass
    #
    # def get_atomic_mass_in_u():
    #     pass
    #
    # def get_ionic_mass_in_u():
    #     pass
    #
    # def get_elbien():
    #     pass
