"""
Barion

-- GUI Application --

Jul 2015 Xaratustrah
Mar 2016 Xaratustrah


"""

from PyQt5.QtWidgets import QMainWindow, QMessageBox, QFileDialog, QDialog
from PyQt5.QtGui import QKeyEvent
from PyQt5.QtCore import Qt, QCoreApplication
from mainwindow_ui import Ui_MainWindow
from ui_interface import UI_Interface
from aboutdialog_ui import Ui_AbooutDialog
from particle import Particle
from amedata import AMEData
import os


class mainWindow(QMainWindow, Ui_MainWindow, UI_Interface):
    """
    The main class for the GUI window
    """

    def __init__(self):
        """
        The constructor and initiator.
        :return:
        """
        # initial setup
        super(mainWindow, self).__init__()
        self.setupUi(self)

        # set home folders
        self.home_folder = os.path.expanduser('~') + '/.barion/'
        self.make_folders()

        # create an instance of the table data and give yourself as UI Interface
        self.ame_data = AMEData(self)

        # fill combo box with names
        self.comboBox_name.addItems(self.ame_data.names_list)

        # UI related stuff
        self.connect_signals()

        # A particle to begin with
        self.particle = None
        self.comboBox_name.setCurrentIndex(6)
        self.reinit_particle()

    def connect_signals(self):
        """
        Connects signals.
        :return:
        """
        self.pushButton_clear.clicked.connect(self.textBrowser.clear)
        self.pushButton_isotopes.clicked.connect(self.show_isotopes)
        self.pushButton_isotones.clicked.connect(self.show_isotones)
        self.pushButton_isobars.clicked.connect(self.show_isobars)
        self.pushButton_save.clicked.connect(self.save_file_dialog)
        self.pushButton_calculate.clicked.connect(self.on_pushButton_calculate)
        self.pushButton_table_data.clicked.connect(self.on_pushButton_table_data)
        self.pushButton_identify.clicked.connect(self.on_pushButton_identify)

        self.actionClear_results.triggered.connect(self.textBrowser.clear)
        self.actionSave_results.triggered.connect(self.save_file_dialog)

        # Action about and Action quit will be shown differently in OSX

        self.actionAbout.triggered.connect(self.show_about_dialog)
        self.actionQuit.triggered.connect(QCoreApplication.instance().quit)
        # self.actionLoad_Freqlist.triggered.connect(self.save_file_dialog)

        self.pushButton_nav_n.clicked.connect(self.on_nav_n_pressed)
        self.pushButton_nav_ne.clicked.connect(self.on_nav_ne_pressed)
        self.pushButton_nav_e.clicked.connect(self.on_nav_e_pressed)
        self.pushButton_nav_se.clicked.connect(self.on_nav_se_pressed)
        self.pushButton_nav_s.clicked.connect(self.on_nav_s_pressed)
        self.pushButton_nav_sw.clicked.connect(self.on_nav_sw_pressed)
        self.pushButton_nav_w.clicked.connect(self.on_nav_w_pressed)
        self.pushButton_nav_nw.clicked.connect(self.on_nav_nw_pressed)

        self.spinBox_qq.valueChanged.connect(self.on_spinBox_qq_changed)
        self.spinBox_nn.valueChanged.connect(self.on_spinBox_nn_changed)
        self.spinBox_zz.valueChanged.connect(self.on_spinBox_zz_changed)

        self.comboBox_name.currentIndexChanged.connect(self.on_comboBox_name_changed)

    def show_about_dialog(self):
        about_dialog = QDialog()
        about_dialog.ui = Ui_AbooutDialog()
        about_dialog.ui.setupUi(about_dialog)
        about_dialog.exec_()
        about_dialog.show()

    def make_folders(self):
        """
        Checks and makes missing folders in the user's home directory
        :return:
        """
        if not os.path.exists(self.home_folder):
            os.mkdir(self.home_folder)

    def show_message(self, message):
        """
        Implementation of an abstract method:
        Show text in status bar
        :param message:
        :return:
        """
        self.statusbar.showMessage(message)

    def show_message_box(self, text):
        """
        Display a message box.
        :param text:
        :return:
        """
        reply = QMessageBox.question(self, 'Message',
                                     text, QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            return True
        else:
            return False

    def show_isotopes(self):
        """
        SLOT
        show isotopes
        :return:
        """
        self.reinit_particle()
        p_array = self.particle.get_isotopes()
        text = 'Isotopes of {} are:\n'.format(self.particle) + '\n'.join(map(str, p_array)) + '\n'
        self.textBrowser.append(text)

    def show_isotones(self):
        """
        SLOT
        show isotones
        :return:
        """
        self.reinit_particle()
        text = 'Isotones of {} are:\n'.format(self.particle) + '\n'.join(map(str, self.particle.get_isotones())) + '\n'
        self.textBrowser.append(text)

    def show_isobars(self):
        """
        SLOT
        show isobars
        :return:
        """
        self.reinit_particle()
        text = 'Isobars of {} are:\n'.format(self.particle) + '\n'.join(map(str, self.particle.get_isobars())) + '\n'
        self.textBrowser.append(text)

    def save_file_dialog(self):
        """
        Show a save file dialog
        :return:
        """
        file_name, _ = QFileDialog.getSaveFileName(self, "Save results", '',
                                                   "Text file (*.txt)")
        if not file_name:
            return
        self.save_results(file_name)

    def save_results(self, file_name):
        """
        Save results to fiven filename.
        :param file_name:
        :return:
        """
        if not self.textBrowser.toPlainText():
            self.show_message('No results to save.')
            return

        with open(file_name, 'w') as f:
            f.write(str(self.textBrowser.toPlainText()))
            self.show_message('Wrote to file {}.'.format(file_name))

    def check_nuclide_validity(self):
        """
        Check if the given nuclide exists in the table
        :return:
        """
        nuclide_validity = True
        if '{}_{}'.format(self.spinBox_zz.value(), self.spinBox_nn.value()) in self.ame_data.zz_nn_names_dic:
            aa = self.spinBox_zz.value() + self.spinBox_nn.value()
            self.label_name.setText(
                '{} {} {}+'.format(aa, self.ame_data.zz_nn_names_dic[
                    '{}_{}'.format(self.spinBox_zz.value(), self.spinBox_nn.value())], self.spinBox_qq.value()))
            self.show_message('Valid nuclide')
        else:
            self.label_name.setText('------')
            self.show_message('Not a valid nuclide')
            nuclide_validity = False
        return nuclide_validity

    def reinit_particle(self):
        """
        Re initialize the particle with new values
        :return:
        """
        if self.check_nuclide_validity():
            # Here make a particle
            zz = self.spinBox_zz.value()
            nn = self.spinBox_nn.value()
            self.particle = Particle(zz, nn, self.ame_data)
            self.particle.qq = self.spinBox_qq.value()
            self.particle.ke_u = self.doubleSpinBox_energy.value()
            self.particle.path_length_m = self.doubleSpinBox_path_length.value()
            self.particle.i_beam_uA = self.doubleSpinBox_beam_current.value()
            self.particle.f_analysis_mhz = self.doubleSpinBox_f_analysis.value()

    def keyPressEvent(self, event):
        """
        Keypress event handler
        :return:
        """
        if type(event) == QKeyEvent:
            # here accept the event and do something
            if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:  # code enter key
                # self.do_calculate()
                self.on_pushButton_calculate()
                event.accept()
            if event.key() == Qt.Key_Space:
                # self.on_pushButton_table_data()
                event.accept()
            if event.key() == Qt.Key_Up:
                print('up')
                event.accept()
        else:
            event.ignore()

    def on_spinBox_zz_changed(self):
        """
        SLOT
        :return:
        """
        self.spinBox_zz.setMinimum(1)
        self.spinBox_zz.setMaximum(self.ame_data.zz_max)
        self.comboBox_name.setCurrentIndex(self.spinBox_zz.value())
        if self.spinBox_qq.value() > self.spinBox_zz.value():
            self.spinBox_qq.setValue(self.spinBox_zz.value())
        self.check_nuclide_validity()

    def on_spinBox_nn_changed(self):
        """
        SLOT
        :return:
        """
        self.spinBox_nn.setMinimum(0)
        self.spinBox_nn.setMaximum(self.ame_data.nn_max)
        self.check_nuclide_validity()

    def on_spinBox_qq_changed(self):
        """
        SLOT
        :return:
        """
        self.spinBox_qq.setMinimum(1)
        self.spinBox_qq.setMaximum(self.ame_data.zz_max)
        if self.spinBox_qq.value() > self.spinBox_zz.value():
            self.spinBox_qq.setValue(self.spinBox_zz.value())
        self.check_nuclide_validity()

    def on_comboBox_name_changed(self, idx):
        """
        SLOT
        :return:
        """
        self.spinBox_zz.setValue(idx)
        # self.spinBox_nn.setValue(idx)
        # self.spinBox_qq.setValue(idx)

    def on_pushButton_calculate(self):
        """
        SLOT
        :return:
        """
        self.do_calculate()

    def do_calculate(self):
        """
        SLOT
        Do the actual calculation
        :return:
        """
        if self.check_nuclide_validity():
            self.show_message('Valid nuclide.')
            # self.textBrowser.append('Calculation not implemented yet.\n')
            self.reinit_particle()
            self.textBrowser.append(self.particle.calculate_from_energy())
        else:
            self.show_message('Not a valid nuclide.')

    def on_pushButton_table_data(self):
        """
        SLOT
        :return:
        """
        self.reinit_particle()
        self.textBrowser.append(self.particle.get_table_data())

    def on_pushButton_identify(self):
        f_actual = self.doubleSpinBox_f_actual.value()
        f_unknown = self.doubleSpinBox_f_unknown.value()
        self.particle.identify(f_actual, f_unknown)

    def on_nav_n_pressed(self):
        """
        SLOT
        :return:
        """
        zz = self.spinBox_zz.value()
        self.spinBox_zz.setValue(zz + 1)

    def on_nav_ne_pressed(self):
        """
        SLOT
        :return:
        """
        zz = self.spinBox_zz.value()
        nn = self.spinBox_nn.value()
        self.spinBox_zz.setValue(zz + 1)
        self.spinBox_nn.setValue(nn + 1)

    def on_nav_e_pressed(self):
        """
        SLOT
        :return:
        """
        nn = self.spinBox_nn.value()
        self.spinBox_nn.setValue(nn + 1)

    def on_nav_se_pressed(self):
        """
        SLOT
        :return:
        """
        zz = self.spinBox_zz.value()
        nn = self.spinBox_nn.value()
        self.spinBox_zz.setValue(zz - 1)
        self.spinBox_nn.setValue(nn + 1)

    def on_nav_s_pressed(self):
        """
        SLOT
        :return:
        """
        zz = self.spinBox_zz.value()
        self.spinBox_zz.setValue(zz - 1)

    def on_nav_sw_pressed(self):
        """
        SLOT
        :return:
        """
        zz = self.spinBox_zz.value()
        nn = self.spinBox_nn.value()
        self.spinBox_zz.setValue(zz - 1)
        self.spinBox_nn.setValue(nn - 1)

    def on_nav_w_pressed(self):
        """
        SLOT
        :return:
        """
        nn = self.spinBox_nn.value()
        self.spinBox_nn.setValue(nn - 1)

    def on_nav_nw_pressed(self):
        """
        SLOT
        :return:
        """
        zz = self.spinBox_zz.value()
        nn = self.spinBox_nn.value()
        self.spinBox_zz.setValue(zz + 1)
        self.spinBox_nn.setValue(nn - 1)
