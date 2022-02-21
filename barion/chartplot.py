"""
Barion

-- GUI Application --

Jul 2015 Xaratustrah
Mar 2016 Xaratustrah
Feb 2022 Xaratustrah

"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches


class ChartPlot:
    def __init__(self):
        self.arrow_to = False
        self.arrow_from = False
        self.plot_filename = 'nuclidic_chart.pdf'
        self.chart_cell_height = 0.8
        self.chart_cell_width = 0.8
        self.chart_title = 'Chart of the nuclides'
        self.chart_ylabel = 'Z'
        self.chart_xlabel = 'N'
        self.font_size = 6

    def bulk_plot(self, particle_array):
        fig1 = plt.figure(num=None, figsize=(8, 6), dpi=150,
                          facecolor='w', edgecolor='k')
        ax1 = plt.subplot(111, aspect='equal')

        # set to dummy large number for later adjustment
        ylim_min = xlim_min = 1000
        ylim_max = xlim_max = 0

        for pp in particle_array:
            ax1.add_patch(self.create_plotcell(pp))
            ax1.text(pp.tbl_nn, pp.tbl_zz, '{}{}'.format(pp.tbl_aa, pp.tbl_name), fontsize=self.font_size,
                     horizontalalignment='center',
                     verticalalignment='center')
            if xlim_min >= pp.tbl_nn:
                xlim_min = pp.tbl_nn - 1
            if ylim_min >= pp.tbl_zz:
                ylim_min = pp.tbl_zz - 1

            if pp.tbl_nn > xlim_max:
                xlim_max = pp.tbl_nn + 2
            if pp.tbl_zz > ylim_max:
                ylim_max = pp.tbl_zz + 1
        ax1.set_xlim([xlim_min, xlim_max])
        ax1.set_ylim([ylim_min, ylim_max])

        plt.grid(False)
        plt.title(self.chart_title)
        plt.ylabel(self.chart_ylabel)
        plt.xlabel(self.chart_xlabel)
        fig1.tight_layout()
        fig1.savefig(self.plot_filename)

    def create_plotcell(self, pp):
        fill = False
        if pp.chart_fill_color:
            fill = True
        return patches.Rectangle(
            (pp.tbl_nn - 0.4, pp.tbl_zz - 0.4),  # (x,y)
            self.chart_cell_width,  # width
            self.chart_cell_height,  # height
            fill=fill,
            facecolor=pp.chart_fill_color
        )
