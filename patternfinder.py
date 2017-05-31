"""
Pattern finder in frequencies

Xaratustrah 2016

"""
import numpy as np
import logging as log


class PatternFinder():
    """
    Data and Sample should be sorted arrays containing frequencies values.
    """

    def __init__(self, data, sample):
        self.data = data
        self.sample = sample

    def get_self_distance_matrix(self):
        out = np.zeros((len(self.data), len(self.data)))
        for i in range(len(self.data)):
            for j in range(len(self.data)):
                out[i, j] = (abs(self.data[i] - self.data[j]))
        return out

    def get_first_match_index(self):
        # find the first matching point index
        tmp = np.zeros(len(self.data))
        for i in range(len(self.data)):
            tmp[i] = abs(self.sample[0] - self.data[i])
        return tmp.argmin()

    def do_patter_matching(self):
        """
        Returns the corresponding indexes in data matching elements in sample
        """
        delta_samp = PatternFinder.get_self_difference_array(self.sample)
        distance_mtx = self.get_self_distance_matrix()

        indexes = np.zeros(len(self.sample), dtype=int)
        jump = self.get_first_match_index()
        indexes[0] = int(jump)

        dist = np.zeros(len(distance_mtx))

        idx = 0
        for j in range(len(delta_samp)):
            for i in range(len(distance_mtx[jump, :])):
                dist[i] = abs(delta_samp[idx] - distance_mtx[jump, i])
            log.info('Array of original data: ', self.data)
            log.info('Array of samples', self.sample)
            log.info('Array of distances from samples: ', delta_samp)
            log.info('Next expected distance: ', delta_samp[idx])
            log.info('compare with row from data:', distance_mtx[jump, :])
            log.info('Result of comparison: ', dist)
            log.info('Only regarding this part: ', dist[jump + 1:])
            try:
                jump += dist[jump + 1:].argmin() + 1  # returns the first occurance of minimum as new jump
            except ValueError:
                log.error('Data does not contain sample.')
                return np.array([]), np.array([])
            log.info('minimum found at index of original data:', jump)
            log.info('Corresponding value in original data: ', self.data[jump])
            idx += 1
            indexes[j + 1] = int(jump)
        values = np.take(self.data, indexes)
        return indexes, values

    @staticmethod
    def get_self_difference_array(array):
        out = np.zeros(len(array) - 1)
        for i in range(len(out)):
            out[i] = abs(array[i] - array[i + 1])
        return out
