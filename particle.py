"""
Barion


Jul 2015 Xaratustrah
Mar 2016 Xaratustrah


"""

from amedata import AMEData
import math
import numpy as np


class Particle(object):
    """
    Class Particle describes a valid nuclide
    """
    FILL_COLOR_STABLE = '#F5A9A9'

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

        # calculated and given values (secondary)
        self.ke_amev = 0.0
        self.path_length_m = 0.0
        self.f_analysis_mhz = 0.0
        self.i_beam_uA = 0.0
        self.lifetime = 0.0
        self.lifetime_flag = 'unknown'  # stable, less, more, sys, exp
        self.chart_fill_color = None

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

        # start with a bare ion
        self.qq = self.tbl_zz

    def __str__(self):
        """
        Converts the particle to string
        :return:
        """
        return \
            str(self.tbl_aa) + '-' + \
            self.tbl_name + ' ' + \
            str(self.qq) + '+, ' + \
            'Z: ' + str(self.tbl_zz) + ', ' + \
            'N: ' + str(self.tbl_nn)

    def get_short_name(self):
        return '{}{}{}+'.format(self.tbl_aa, self.tbl_name, self.qq)

    def get_all_in_all(self):
        """
        Get all nuclei in all charge states!
        """
        p_array = []
        for entry in self.ame_data.ame_table:
            for eee in range(entry[4]):
                p = Particle(entry[4], entry[3], self.ame_data, self.ring)
                p.qq = entry[4] - eee
                # give properties of the reference particle
                p.ke_amev = self.ke_amev
                # todo: nicht path length, mass formel hier!
                p.path_length_m = self.path_length_m
                p.f_analysis_mhz = self.f_analysis_mhz
                p.i_beam_uA = self.i_beam_uA
                # add to array
                p_array.append(p)
            # if entry[4] > 20:
            #     break
        return p_array

    def get_nuclides(self, zz_min, zz_max, nn_min, nn_max, ee_max):
        """
        Parameters
        ----------
        zz_min
        zz_max
        nn_min
        nn_max
        qq_max: number of charge states. i.e. 2 means bare and H-like

        Returns: array of particle object
        -------

        """
        p_array = []
        for i in self.ame_data.ame_table:
            if zz_min <= i[4] <= zz_max:
                if nn_min <= i[3] <= nn_max:
                    for eee in range(ee_max):
                        # create particle
                        p = Particle(i[4], i[3], self.ame_data, self.ring)
                        p.qq = i[4] - eee
                        # give properties of the reference particle
                        p.ke_amev = self.ke_amev
                        # todo: nicht path length, mass formel hier!
                        p.path_length_m = self.path_length_m
                        p.f_analysis_mhz = self.f_analysis_mhz
                        p.i_beam_uA = self.i_beam_uA
                        # add to array
                        p_array.append(p)
        return p_array

    def get_isotopes(self):
        """
        Retrieves the isotopes of the current nuclide
        :return:
        """
        p_array = []
        for i in self.ame_data.ame_table:
            if i[4] == self.tbl_zz:
                p = Particle(i[4], i[3], self.ame_data, self.ring)
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
                p = Particle(i[4], i[3], self.ame_data, self.ring)
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
                p = Particle(i[4], i[3], self.ame_data, self.ring)
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
            'Atomic Mass [uU]: ' + str(self.tbl_am_microu) + ' ± ' + str(self.tbl_am_err_microu) + '\n' + \
            'Lifetime [s]: ' + str(self.get_lifetime()) + '\n'

    # --------------------------------

    def get_lifetime(self):
        lt = ''
        mp = ''
        result = ''
        for entry in self.ame_data.nubase_table:
            if entry[0] == '{}{}'.format(self.tbl_aa, self.tbl_name):
                lt = entry[1]
                mp = entry[2]
            try:
                result = float(lt) * float(mp)
            except(ValueError):
                # deal with unwanted characters in the NUBASE
                if '<' in lt:
                    self.lifetime_flag = 'less_than'
                    result = float(lt.replace('<', '')) * float(mp)
                elif '>' in lt:
                    self.lifetime_flag = 'more_than'
                    result = float(lt.replace('>', '')) * float(mp)
                elif 'unst' in lt:
                    self.lifetime_flag = 'p-unst'
                elif '#' in lt:
                    self.lifetime_flag = 'sys'
                    result = float(lt.replace('#', '.')) * float(mp)
                else:
                    result = lt
        return result

    # --------------------------------
    def get_total_charge_in_coulomb(self):
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

    def get_ionic_moq_in_u(self):
        return self.get_ionic_mass_in_u() / self.qq

    # --------------------------------

    def get_total_kinetic_energy_in_mev(self):
        return self.ke_amev * self.tbl_aa

    def get_gamma(self):
        return self.get_total_kinetic_energy_in_mev() / AMEData.to_mev(self.get_ionic_mass_in_u()) + 1.0

    def get_eta(self):
        return (1 / self.get_gamma() ** 2) - (1 / self.ring.gamma_t ** 2)

    def get_beta(self):
        return math.sqrt(1.0 - 1.0 / math.pow(self.get_gamma(), 2))

    def get_beta_gamma(self):
        return self.get_beta() * self.get_gamma()

    def get_velocity(self):
        # return Velocity in m/s
        return self.get_beta() * AMEData.CC

    def get_relativistic_mass(self):
        # return relativistic mass in MeV/c^2
        return AMEData.to_mev(self.get_ionic_mass_in_u()) * self.get_gamma()

    def get_relativistic_momentum(self):
        # return relativistic momentum in MeV/c
        return AMEData.to_mev(self.get_ionic_mass_in_u()) * self.get_gamma() * self.get_beta()

    def get_relativistic_momentum_per_u(self):
        # return relativistic momentum in MeV/c/u
        return self.get_relativistic_momentum() / self.tbl_aa

    def get_pc(self):
        # return pc in MeV
        return self.get_relativistic_momentum() * AMEData.CC

    def get_magnetic_rigidity(self):
        # unit Tm
        return self.get_relativistic_momentum() * 1.0e6 / self.qq / AMEData.CC

    def get_electric_rigidity(self):
        # unit MJ/Q
        return self.get_magnetic_rigidity() * self.get_velocity() / 1.0e6

    def get_neutron_excess_parameter(self):
        return (self.tbl_nn - self.tbl_zz) / (self.get_atomic_mass_in_u())

    # --------------------------------

    def get_revolution_frequency(self):
        return self.get_velocity() / self.path_length_m / 1.0e6

    @staticmethod
    def get_revolution_frequency_from_harmonic(harmonic, measured_freq):
        return measured_freq / harmonic

    @staticmethod
    def get_harmonic_frequency_from_f_rev(harmonic, f_rev):
        return f_rev * harmonic

    def get_number_of_ions(self, f_rev):
        return int(self.i_beam_uA / 1.0e6 / f_rev / 1.0e6 / self.get_total_charge_in_coulomb())

    def get_prev_revolution_harmonic(self, f_rev):
        return int(self.f_analysis_mhz / f_rev)

    def get_next_revolution_harmonic(self, f_rev):
        return int(self.f_analysis_mhz / f_rev) + 1

    def get_prev_peak_frequency(self, f_rev):
        return self.get_prev_revolution_harmonic(f_rev) * f_rev

    def get_next_peak_frequency(self, f_rev):
        return self.get_next_revolution_harmonic(f_rev) * f_rev

    @staticmethod
    def get_frequency_at_harmnic_in_mhz(f_rev, harmonic):
        assert int(harmonic) == harmonic
        return f_rev * harmonic

    @staticmethod
    def get_frequency_at_harmnic_in_mhz_list(f_rev, harm_min, harm_max):
        assert int(harm_min) == harm_min
        assert int(harm_max) == harm_max
        assert harm_max > harm_min
        lst = []
        for i in range(harm_min, harm_max):
            lst.append([i, Particle.get_frequency_at_harmnic_in_mhz(f_rev, i)])
        return lst
    # --------------------------------

    @staticmethod
    def convert_table_to_str(tbl):
        s = ''
        for line in tbl:
            for element in line:
                s += str(element)
                s += ' '
            s += '\n'
        return s

    def calculate_from_energy_list(self):

        s = [['Nuclide:', "{} {} {}+".format(self.tbl_aa, self.tbl_name, self.qq), ''],
             ["Z:", str(self.tbl_zz), ''],
             ['N:', str(self.tbl_nn), ''],
             ['Source:', '{source}'.format(
                 source='** EXP **' if self.exp else '** SYS **'), ''],
             ['Kinetic energy:', str(self.ke_amev), '[MeV/u]'],
             ['Beam current:', str(self.i_beam_uA), '[µA]'],
             ['Path length:', str(self.path_length_m), '[m]'],
             ['Analysis freq.:', str(self.f_analysis_mhz), '[MHz]'],
             ['Total charge per ion:', str(
                 self.get_total_charge_in_coulomb()), '[C]'],
             ['Atomic mass:', str(self.get_atomic_mass_in_u()), '[u]'],
             ['Ionic mass:', str(self.get_ionic_mass_in_u()), '[u]'],
             ['Ionic mass:', str(AMEData.to_kg(
                 self.get_ionic_mass_in_u())), '[kg]'],
             ['Ionic m/Q:', str(self.get_ionic_moq_in_u()), '[u]'],
             ['Neutron Excess Parameter:', str(
                 self.get_neutron_excess_parameter()), '[1/u]'],
             ['Tot. kin. Energy:', str(
                 self.get_total_kinetic_energy_in_mev()), '[MeV]'],
             ['gamma:', str(self.get_gamma()), ''],
             ['beta:', str(self.get_beta()), ''],
             ['beta * gamma:', str(self.get_beta_gamma()), ''],
             ['Velocity:', str(self.get_velocity()), '[m/s]'],
             ['eta:', str(self.get_eta()), ''],
             ['', str(AMEData.get_kmh(self.get_velocity())), '[km/h]'],
             ['Rel. mass:', str(self.get_relativistic_mass()), '[MeV/c^2]'],
             ['', str(AMEData.to_u(self.get_relativistic_mass())), '[u]'],
             ['', str(AMEData.to_kg(self.get_relativistic_mass())), '[kg]'],
             ['Rel. Momentum:', str(
                 self.get_relativistic_momentum()), '[MeV/c]'],
             ['Rel. Mom. per Nucl.:', str(
                 self.get_relativistic_momentum_per_u()), '[MeV/c/u]'],
             ['pc:', str(self.get_pc()), '[MeV]'],
             ['Brho:', str(self.get_magnetic_rigidity()), '[T/m]'],
             ['Erho:', str(self.get_electric_rigidity()), '[MJ/C]'],
             ['f_rev:', str(self.get_revolution_frequency()), '[MHz]'],
             ['No. of ions:', str(self.get_number_of_ions(
                 self.get_revolution_frequency())), ''],
             ['Prev. harmonic:', str(self.get_prev_revolution_harmonic(
                 self.get_revolution_frequency())), ''],
             ['Expected peak:', str(self.get_prev_peak_frequency(
                 self.get_revolution_frequency())), '[MHz]'],
             ['Next harmonic:', str(self.get_next_revolution_harmonic(
                 self.get_revolution_frequency())), ''],
             ['Expected peak:', str(self.get_next_peak_frequency(self.get_revolution_frequency())), '[MHz]']]

        return s

    def get_moq_unknown_from_freq(self, frev_p_ref, frev_p_unknown):
        alpha_p = self.ring.get_alpha_p()
        delta_f = frev_p_ref - frev_p_unknown
        delta_moq = - delta_f / frev_p_ref * self.get_ionic_moq_in_u() / alpha_p
        moq_unknown = self.get_ionic_moq_in_u() - delta_moq
        return moq_unknown

    def get_unknown_rev_freq_from_moq(self, frev_p_ref, moq_unknown):
        alpha_p = self.ring.get_alpha_p()
        delta_moq = self.get_ionic_moq_in_u() - moq_unknown
        delta_f = -alpha_p * delta_moq / self.get_ionic_moq_in_u() * frev_p_ref
        return frev_p_ref - delta_f

    def identify(self, f_p_ref, f_p_unknown, zz_range, nn_range, ee_max, accuracy):
        moq_unknown = self.get_moq_unknown_from_freq(f_p_ref, f_p_unknown)
        moq_dict = {}
        for i in self.ame_data.ame_table:
            if i[4] in range(self.tbl_zz - zz_range, self.tbl_zz + zz_range):
                if i[3] in range(self.tbl_nn - nn_range, self.tbl_nn + nn_range):
                    p = Particle(i[4], i[3], self.ame_data, self.ring)
                    for eee in range(ee_max):
                        p.qq = i[4] - eee
                        moq_dict[str(p)] = p.get_ionic_moq_in_u()
        candidates = [k for (k, v) in moq_dict.items()
                      if abs(v - moq_unknown) <= accuracy]
        if str(self) in candidates:
            candidates.remove(str(self))
        return candidates

    def identify_search(self, f_p_ref, f_p_unknown, zz_range, nn_range, ee_max):
        accuracy = 1e-6
        while True:
            s = self.identify(
                f_p_ref, f_p_unknown, zz_range, nn_range, ee_max, accuracy)
            if s:
                break
            accuracy += 1e-6
        return s[0]

    # --------------------------------

    def get_nuclides_freqs(self, p_ref_f_rev_measured, harmonic, region_set):
        freqs_sim = np.array([])
        freqs_sim_dic = {}

        for pp in region_set:
            pp.ke_amev = self.ke_amev
            pp.path_length_m = self.path_length_m

            # following command assumes gamma_t set in the p_ref.ring.gamma_t
            ff = self.get_unknown_rev_freq_from_moq(
                p_ref_f_rev_measured, pp.get_ionic_moq_in_u())

            ff_at_harm = Particle.get_harmonic_frequency_from_f_rev(
                harmonic, ff)
            freqs_sim = np.append(freqs_sim, ff_at_harm)
            freqs_sim_dic[ff_at_harm] = pp

        freqs_sim.sort()
        freqs_sim = np.flip(freqs_sim)
        return freqs_sim, freqs_sim_dic

    @staticmethod
    def get_xisqaure_array(muster, probe):
        xisqu_array = np.array([])
        for i in range(len(muster)):
            xisqu = 0
            for j in range(len(probe)):
                xisqu += (muster[j] - probe[j])**2
            xisqu_array = np.append(xisqu_array, xisqu)
            muster = np.roll(muster, -1)
            muster[-1] = 0
        return xisqu_array
