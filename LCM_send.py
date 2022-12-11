import lcm, random, time, os
from Pod_data_class import pod_data

Nirman = pod_data()
lc = lcm.LCM()

def smooth_random(low,high,current):
    temp = low
    high = high - low
    current = current - low
    low = 0

    close_range = int((low+high)*0.3)
    if (current<=close_range): return (temp+random.randint(0,close_range))
    elif (current>=(high-close_range)): return (temp+random.randint((current-close_range),high))
    else : return (temp+random.randint((current-close_range),(current+close_range)))
    
    

def randon_pod_data():
    Nirman.acceleration = smooth_random(0,100,Nirman.acceleration)
    Nirman.velocity = smooth_random(0,100,Nirman.velocity)
    Nirman.height = smooth_random(0,10,Nirman.height)
    Nirman.High_battery_voltage = smooth_random(12,30,Nirman.High_battery_voltage)
    Nirman.Low_battery_voltage = smooth_random(5,12,Nirman.Low_battery_voltage)
    
    

def send_pod_data(delay_time):
    count = 0

    while 1:
        randon_pod_data()
        lc.publish("Pod", Nirman.encode())
        count += 1
        os.system("clear")
        print(count)

        time.sleep(delay_time)

def send_pod_data_once():
    randon_pod_data()
    lc.publish("Pod", Nirman.encode())


if __name__ == "__main__":
    send_pod_data(1)