from psutil import sensors_battery
from notify2 import init, Notification
from time import sleep

if __name__ == '__main__':
    init('battery notification')
    notification = Notification('Battery low', "Your battery is almost empty. Plug in your computer now or save your work.")
    shown = False
    while True:
        battery = sensors_battery()
        if battery.percent < 80 and not battery.power_plugged and not shown:
            notification.update('Battery low', f'Your battery is almost empty. Plug in your computer now or save your work\n'
                                               f'You have {battery.secsleft // 60} minutes left.')
            notification.show()
            shown = True
            sleep(300)
        sleep(10)
