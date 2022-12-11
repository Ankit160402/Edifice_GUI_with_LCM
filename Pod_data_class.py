class pod_data():
    def __init__(self):
        self.acceleration = 0
        self.velocity = 0
        self.height = 0
        self.High_battery_voltage = 0
        self.Low_battery_voltage = 0

        self.encodeing_var = '#'
    def encode(self):
        return ((str(self.acceleration)+self.encodeing_var+
                str(self.velocity)+self.encodeing_var+
                str(self.height)+self.encodeing_var+
                str(self.High_battery_voltage)+self.encodeing_var+
                str(self.Low_battery_voltage)).encode())

    def decode(self,decode_bin):
        decode = decode_bin.decode()
        decode = decode.split(self.encodeing_var)
        self.acceleration = decode[0]
        self.velocity = decode[1]
        self.height = decode[2]
        self.High_battery_voltage = decode[3]
        self.Low_battery_voltage = decode[4]

    def print(self):
        new_line = "\n"
        data_str = (f'Acceleration : {self.acceleration} m/s\u00b2'
                    + new_line +f'Velocity : {self.velocity} m/s'
                    + new_line +f'Pod Height : {self.height} cm'
                    + new_line +f'High Battery Voltage : {self.High_battery_voltage} V'
                    + new_line +f'Low Battery Voltage : {self.Low_battery_voltage} V')

        print(data_str)

    def update(self,acc,vel,hgt,hv,lv):
        self.acceleration = acc
        self.velocity = vel
        self.height = hgt
        self.High_battery_voltage = hv
        self.Low_battery_voltage = lv


if __name__ == "__main__":
    Nirman = pod_data()
    Nirman.update(1,2,3,4,5)
    Nirman.print()

    Nirman.decode(Nirman.encode())
    Nirman.print()