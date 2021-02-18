from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import pyqtSlot
from Dif_Test import Ui_MainWindow
from numpy import pi, linspace, meshgrid
import numpy as np
import matplotlib.cm as cm
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

# a: distancia entre rendijas


class Dif_App(QMainWindow, Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.fig1()
        self.fig2()

    def fig1(self):
        lamda1 = self.slider_lambda.value() * 1e-9
        k1 = np.divide(2 * pi, lamda1)

        a1 = self.slider_a.value() * 1e-4
        b1 = self.slider_b.value() * 1e-5
        n1 = self.slider_n.value()
        f1 = self.slider_f.value()

        N = 400

        X_Mmax1 = a1
        X_Mmin1 = -a1
        Y_Mmax1 = X_Mmax1
        Y_Mmin1 = X_Mmin1

        X1 = linspace(X_Mmin1, X_Mmax1, N)
        Y1 = X1

        def funcDif1(x):
            p = np.divide(k1 * a1, 2) * x  # alfa
            q = np.divide(k1 * b1, 2) * x  # beta
            return np.square(np.divide(np.sin(q), q)) * np.square(np.divide(np.sin(n1 * p), np.sin(p)))

        XX, YY = meshgrid(X1, Y1)

        Is = funcDif1(XX)

        # 2D figure

        mpl1 = self.widget_2.canvas
        mpl1.ax.clear()
        mpl1.ax.imshow(Is, cmap=cm.gray, aspect='auto', interpolation='bilinear', origin='lower', vmin=0, vmax=1.5)

        plt.style.use('bmh')
        mpl1.ax.grid(False)
        font = {'fontname': 'Times New Roman'}
        mpl1.ax.set_xlabel(r'$X\,\,$(m)', **font)
        mpl1.ax.set_ylabel(r'$Y\,\,$(m)', **font)

        mpl1.ax.set_xticks(linspace(0, N, 5))
        mpl1.ax.set_xticklabels(np.round(linspace(X_Mmin1, X_Mmax1, 5), 4))
        mpl1.ax.set_yticks(linspace(0, N, 5))
        mpl1.ax.set_yticklabels(np.round(linspace(Y_Mmin1, Y_Mmax1, 5), 4))
        # mpl.figure.suptitle()
        # mpl.ax.set_title()}
        mpl1.draw()

    def fig2(self):

        lamda = self.slider_lambda.value() * 1e-9
        k = np.divide(2 * pi, lamda)

        a = self.slider_a.value() * 1e-4
        b = self.slider_b.value() * 1e-5
        n = self.slider_n.value()
        f = self.slider_f.value()

        N = 5000

        X_Mmax = a
        X_Mmin = -a
        Y_Mmax = X_Mmax
        Y_Mmin = X_Mmin

        X = linspace(X_Mmin, X_Mmax, N)
        Y = X

        def funcDif2(x):
            p = np.divide(k * a, 2) * x  # alfa
            q = np.divide(k * b, 2) * x  # beta
            return np.square(np.divide(np.sin(q), q)) * np.square(np.divide(np.sin(n * p), np.sin(p)))

        def funcInt(x):
            r = np.divide(k * b, 2) * x  # beta
            return np.square(n) * np.square(np.divide(np.sin(r), r))

        # 2D figure

        Ix1 = X
        Ix2 = X
        Iy1 = funcDif2(X)
        Iy2 = funcInt(X)

        mpl = self.widget.canvas
        mpl.ax.clear()

        mpl.ax.plot(X, Iy1, color='black', linewidth=0.5)
        mpl.ax.plot(X, Iy2, linewidth=0.7, linestyle='dashed', color='black')
        mpl.ax.set_xlim(X_Mmin, X_Mmax)
        mpl.ax.set_ylim(bottom=0)

        verts = [(X_Mmin, 0), *zip(X, Iy1), (X_Mmax, 0)]
        poly = Polygon(verts, facecolor='0.9', edgecolor='0.5')
        mpl.ax.add_patch(poly)

        plt.style.use('bmh')
        font = {'fontname': 'Times New Roman'}
        mpl.ax.set_xlabel(r'$\sin{(\theta)}$', **font)
        mpl.ax.set_ylabel(r'$I(\theta)\,/\,I_0$', **font)
        # mpl.ax.set_xticks()
        # mpl.ax.set_xticklabels()
        # mpl.ax.set_yticks()
        # mpl.ax.set_yticklabels()
        # mpl.ax.set_title()
        mpl.draw()

    # DoubleSpinBox signals

    @pyqtSlot("double")
    def on_SpinBox_lambda_valueChanged(self, value):
        self.slider_lambda.setValue(int(value))

    @pyqtSlot("double")
    def on_SpinBox_b_valueChanged(self, value):
        self.slider_b.setValue(int(value))

    @pyqtSlot("double")
    def on_SpinBox_n_valueChanged(self, value):
        self.slider_n.setValue(int(value))

    @pyqtSlot("double")
    def on_SpinBox_a_valueChanged(self, value):
        self.slider_a.setValue(int(value))

    @pyqtSlot("double")
    def on_SpinBox_f_valueChanged(self, value):
        self.slider_f.setValue(int(value))

    # Sliders signals
    @pyqtSlot("int")
    def on_slider_lambda_valueChanged(self, value):
        self.SpinBox_lambda.setValue(value)
        self.fig1()
        self.fig2()

    @pyqtSlot("int")
    def on_slider_b_valueChanged(self, value):
        self.SpinBox_b.setValue(value)
        self.fig1()
        self.fig2()

    @pyqtSlot("int")
    def on_slider_n_valueChanged(self, value):
        self.SpinBox_n.setValue(value)
        self.fig1()
        self.fig2()

    @pyqtSlot("int")
    def on_slider_a_valueChanged(self, value):
        self.SpinBox_a.setValue(value)
        self.fig1()
        self.fig2()

    @pyqtSlot("int")
    def on_slider_f_valueChanged(self, value):
        self.SpinBox_f.setValue(value)
        self.fig1()
        self.fig2()


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    MyApplication = Dif_App()
    MyApplication.show()  # Show the form
    sys.exit(app.exec_())  # Execute the app
