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

    def __init__(self, zz, nn, ame_data, ring):
        """
        Constructor of the class
        :param zz: proton number
        :param nn: neutron number
        :param ame_data: an existing pointer to a table object
        :return:
        """

        # given only values (primary)
        self.ame_data = ame_data
        self.ring = ring
        self.qq = 0

        # calculated and given values (secondary)
        self.ke_u = 0.0
        self.path_length_m = 0.0
        self.f_analysis_mhz = 0.0
        self.i_beam_uA = 0.0

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

    def get_ionic_moq(self):
        return self.get_ionic_mass_in_u() / self.qq

    # --------------------------------

    def get_total_energy_mev(self):
        return self.ke_u * self.tbl_aa

    def get_gamma(self):
        return self.get_total_energy_mev() / AMEData.to_mev(self.get_ionic_mass_in_u()) + 1.0

    # --------------------------------

    def get_beta(self):
        return math.sqrt(1.0 - 1.0 / math.pow(self.get_gamma(), 2))

    def get_beta_gamma(self):
        return self.get_beta() * self.get_gamma()

    def get_velocity(self):
        return self.get_beta() * AMEData.CC

    def get_relativistic_mass(self):
        return AMEData.to_mev(self.get_ionic_mass_in_u()) * self.get_gamma()

    def get_relativistic_momentum(self):
        return AMEData.to_mev(self.get_ionic_mass_in_u()) * self.get_gamma() * self.get_beta()

    def get_relativistic_momentum_per_u(self):
        return self.get_relativistic_momentum() / self.tbl_aa

    def get_pc(self):
        return self.get_relativistic_momentum() * AMEData.CC

    def get_magnetic_rigidity(self):
        return self.get_relativistic_momentum() * 1.0e6 / self.qq / AMEData.CC

    def get_electric_rigidity(self):
        return self.get_magnetic_rigidity() * self.get_velocity() / 1.0e3

    # --------------------------------

    def get_revolution_frequency(self):
        return self.get_velocity() / self.path_length_m / 1.0e6

    def get_number_of_ions(self):
        return int(self.i_beam_uA / 1.0e6 / self.get_revolution_frequency() / 1.0e6 / self.get_total_charge())

    def get_prev_revolution_harmonic(self):
        return int(self.f_analysis_mhz / self.get_revolution_frequency())

    def get_next_revolution_harmonic(self):
        return int(self.f_analysis_mhz / self.get_revolution_frequency()) + 1

    def get_prev_peak_frequency(self):
        return self.get_prev_revolution_harmonic() * self.get_revolution_frequency()

    def get_next_peak_frequency(self):
        return self.get_next_revolution_harmonic() * self.get_revolution_frequency()

    # --------------------------------

    def calculate_from_energy(self):
        s = "Given:\n------\n"
        s += "{} {} {}+\n".format(self.tbl_aa, self.tbl_name, self.qq)
        s += "z= {}, ".format(self.tbl_zz)
        s += "n= {}\n".format(self.tbl_nn)
        s += "Kin. Energy:\t\t{}\t\t[MeV/u]\n".format(self.ke_u)
        s += "Beam current:\t{}\t\t[µA]\n".format(self.i_beam_uA)
        s += "Path length:\t\t{}\t\t[m]\n".format(self.path_length_m)
        s += "Analysis freq.:\t{}\t\t[MHz]\n".format(self.f_analysis_mhz)

        s += "\n"
        s += "Calculated:\n-----------\n"
        s += "Total charge:\t\t{}\t[C]\n".format(self.get_total_charge())

        # s += "Atom. Mass.:\t\t{}\t\t[u]\n".format(self.get_atomic_mass_in_u())

        s += "Ion. Mass.:\t\t{}\t[u]\n".format(self.get_ionic_mass_in_u())

        s += "m/Q (ionic):\t\t{}\n".format(self.get_ionic_moq())

        s += "Tot. Kin. Energy:\t{}\t\t[MeV]\n".format(self.get_total_energy_mev())
        s += "gamma:\t\t{}\n".format(self.get_gamma())
        s += "beta:\t\t{}\n".format(self.get_beta())
        s += "beta * gamma:\t{}\n".format(self.get_beta_gamma())
        s += "Velocity:\t\t{}\t[m/s]\n".format(self.get_velocity())
        s += "\t\t{}\t[km/h]\n".format(AMEData.get_kmh(self.get_velocity()))

        s += "Relativistic mass:\t{}\t[MeV/c^2]\n".format(self.get_relativistic_mass())
        s += "\t\t{}\t[u]\n".format(AMEData.to_u(self.get_relativistic_mass()))

        s += "Rel. momentum:\t{}\t[MeV/c]\n".format(self.get_relativistic_momentum())
        s += "Rel. mom. per Nuc.:\t{}\t[MeV/c/u]\n".format(self.get_relativistic_momentum_per_u())

        s += "pc:\t\t{}\t[MeV]\n".format(self.get_pc())

        s += "Brho:\t\t{}\t[T/m]\n".format(self.get_magnetic_rigidity())
        s += "Erho:\t\t{}\t[kV]\n".format(self.get_electric_rigidity())

        s += "f_rev:\t\t{}\t[MHz]\n".format(self.get_revolution_frequency())
        s += "No. of ions:\t\t{}\n".format(self.get_number_of_ions())

        s += "Prev. Harmonic:\t{}\n".format(self.get_prev_revolution_harmonic())
        s += "Expected peak freq.:\t{}\t[MHz]\n".format(self.get_prev_peak_frequency())
        s += "Next Harmonic:\t{}\n".format(self.get_next_revolution_harmonic())
        s += "Expected peak freq.:\t{}\t[MHz]\n".format(self.get_next_peak_frequency())

        return s

    def calculate_from_energy_list(self):

        s = [['Nuclide:', "{} {} {}+".format(self.tbl_aa, self.tbl_name, self.qq), ''],
             ["Z:", str(self.tbl_zz), ''],
             ['N:', str(self.tbl_nn), ''],
             ['Kinetic energy:', str(self.ke_u), '[MeV/u]'],
             ['Beam current:', str(self.i_beam_uA), '[µA]'],
             ['Path length:', str(self.path_length_m), '[m]'],
             ['Analysis freq.:', str(self.f_analysis_mhz), '[MHz]'],
             ['Total charge:', str(self.get_total_charge()), '[C]'],
             ['Atomic mass:', str(self.get_atomic_mass_in_u()), '[u]'],
             ['Ionic mass:', str(self.get_ionic_mass_in_u()), '[u]'],
             ['Ionic m/Q:', str(self.get_ionic_moq()), '[u]'],
             ['Tot. kin. Energy:', str(self.get_total_energy_mev()), '[MeV]'],
             ['gamma:', str(self.get_gamma()), ''],
             ['beta:', str(self.get_beta()), ''], ['beta * gamma:', str(self.get_beta_gamma()), ''],
             ['Velocity:', str(self.get_velocity()), '[m/s]'],
             ['', str(AMEData.get_kmh(self.get_velocity())), '[km/h]'],
             ['Rel. mass:', str(self.get_relativistic_mass()), '[MeV/c^2]'],
             ['', str(AMEData.to_u(self.get_relativistic_mass())), '[u]'],
             ['', str(AMEData.to_kg(self.get_relativistic_mass())), '[kg]'],
             ['Rel. Momentum:', str(self.get_relativistic_momentum()), '[MeV/c]'],
             ['Rel. Mom. per Nucl.:', str(self.get_relativistic_momentum_per_u()), '[MeV/c/u]'],
             ['pc:', str(self.get_pc()), '[MeV]'], ['Brho:', str(self.get_magnetic_rigidity()), '[T/m]'],
             ['Erho:', str(self.get_electric_rigidity()), '[kV]'],
             ['f_rev:', str(self.get_revolution_frequency()), '[MHz]'],
             ['No. of ions:', str(self.get_number_of_ions()), ''],
             ['Prev. harmonic:', str(self.get_prev_revolution_harmonic()), ''],
             ['Expected peak:', str(self.get_prev_peak_frequency()), '[MHz]'],
             ['Next harmonic:', str(self.get_next_revolution_harmonic()), ''],
             ['Expected peak:', str(self.get_next_peak_frequency()), '[MHz]']]

        return s

    def identify(self, f_actual, f_unknown):
        max_ee = 5
        max_aa = 142
        max_zz = 60
        # todo:here
        alpha_p = self.ring.get_alpha_p()
        delta_f = f_actual - f_unknown
        delta_moq = delta_f / alpha_p * self.get_ionic_moq()
        s = "Ring: ESR\n"
        s += "delta_moq: {}\n".format(delta_moq)
        s += 'moq of unknown particle:{}\n'.format(self.get_ionic_moq() + delta_moq)

        return s
