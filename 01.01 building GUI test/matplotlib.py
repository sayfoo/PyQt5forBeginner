import sys
from PySide6.QtWidgets import QApplication, QPushButton
import matplotlib.pyplot as plt


class AppDemo(QPushButton):
	def __init__(self):
		super().__init__()
		self.setText('Launch Chart')
		self.setStyleSheet('font-size: 40px;')
		self.resize(300, 150)
		self.clicked.connect(self.launch_graph)

	def launch_graph(self):
		fig, (ax1, ax2) = plt.subplots(nrows=2, sharex=True, figsize=(6, 6), dpi=200)
		plt.subplots_adjust(hspace=0)

		x = range(0, 10)
		y1 = range(0, 10)
		y2 = range(10, 0, -1)

		ax1.plot(x, y1)
		ax2.plot(x, y2)

		plt.show()

if __name__ == "__main__":
    if not QApplication.instance():
        app = QApplication(sys.argv)
    else:
        app = QApplication.instance()
    exe = AppDemo()
    exe.show()
    try:
        sys.exit(app.exec())
    except SystemExit as e:
        print(f"정상적으로 마쳐야 할텐뎅..[{e}]")