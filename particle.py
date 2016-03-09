"""
Barion

-- GUI Application --

Jul 2015 Xaratustrah
Mar 2016 Xaratustrah


"""

from amedata import AMEData
import math


class Particle(object):
    """
    Class Particle describes a valid nuclide
    """

    def __init__(self, zz, nn, ame_data):
        """
        Constructor of the class
        :param zz: proton number
        :param nn: neutron number
        :param ame_data: an existing pointer to a table object
        :return:
        """

        # given only values (primary)
        self.ame_data = ame_data
        self.qq = 0

        # calculated and given values (secondary)
        self.ke_u = 0.0
        self.path_length = 0.0
        self.f_peak = 0.0
        self.i_beam = 0.0

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

    # --------------------------------

    def get_total_charge(self):
        return self.qq * AMEData.EE

    def get_atomic_mass_in_u(self):
        return self.tbl_am_microu / 1e6

    def get_ionic_mass_in_u(self):
        # note elbien is in eV must convert to MeV
        if self.tbl_zz <= 100:
            return self.get_atomic_mass_in_u() + AMEData.to_u(
                (AMEData.get_elbien(self.tbl_zz, 0) - AMEData.get_elbien(self.tbl_zz,
                                                                         self.qq)) / 1.0e6 - self.qq * AMEData.ME)
        else:
            return self.get_atomic_mass_in_u()
        pass

    # --------------------------------

    def get_total_energy_mev(self):
        return self.ke_u ** self.tbl_aa

    def get_gamma(self):
        return self.get_total_energy_mev() / AMEData.to_mev(self.get_ionic_mass_in_u()) + 1.0

    # --------------------------------

    def get_beta(self):
        return math.sqrt(1.0 - 1.0 / math.pow(self.get_gamma(), 2))

    def get_velocity(self):
        return self.get_beta() * AMEData.CC

    def get_relativistic_mass(self):
        return AMEData.to_mev(self.get_ionic_mass_in_u()) * self.get_gamma()

    def get_relativistic_momentum(self):
        return AMEData.to_mev(self.get_ionic_mass_in_u()) * self.get_gamma() * self.get_beta()

    def get_magnetic_rigidity(self):
        return self.get_relativistic_momentum() * 1.0e6 / self.qq / AMEData.CC

    def get_electric_rigidity(self):
        return self.get_magnetic_rigidity() * self.get_velocity() / 1.0e3

    # --------------------------------

    def get_revolution_frequency(self):
        return self.get_velocity() / self.path_length / 1.0e6

    def get_prev_revolution_harmonic(self):
        return int(self.f_peak / self.get_revolution_frequency())

    def get_nect_revolution_harmonic(self):
        return int(self.f_peak / self.get_revolution_frequency()) + 1

    def get_number_of_ions(self):
        return self.i_beam / (self.get_revolution_frequency() * 1.0e6 * self.get_total_charge())

    # --------------------------------

    def calculate_from_energy(self):
        s = "Given:\n"
        s += "{} {} {}+\n".format(self.tbl_aa, self.tbl_name, self.qq)
        s += "z: {}\n".format(self.tbl_zz)
        s += "n: {}\n\n".format(self.tbl_nn)
        s += "beta:\t{}\n".format(self.get_beta())
        s += "gamma:\t{}\n".format(self.get_gamma())
        #s += "Brho:\t{} [Tm]\n".format(self.get_magnetic_rigidity())

        return s
