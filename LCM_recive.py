from PyQt5.QtCore import QThread, pyqtSignal
import lcm, os
from Pod_data_class import pod_data

Nirman = pod_data()


class Recived_pod_data(QThread):
    update_acceleration = pyqtSignal(int)
    update_velocity = pyqtSignal(int)
    update_height = pyqtSignal(int)
    update_h_vol = pyqtSignal(int)
    update_l_vol = pyqtSignal(int)


    def run(self):
        lc = lcm.LCM()
        subscription = lc.subscribe("Pod", self.my_handler)
        try:
            while True:
                lc.handle()
        except KeyboardInterrupt:
            pass

    def my_handler(self, channel, data):
        Nirman.decode(data)
        self.update_acceleration.emit(int(Nirman.acceleration))
        self.update_velocity.emit(int(Nirman.velocity))
        self.update_height.emit(int(Nirman.height))
        self.update_h_vol.emit(int(Nirman.High_battery_voltage))
        self.update_l_vol.emit(int(Nirman.Low_battery_voltage))
        os.system("clear")
        Nirman.print()
