from pyfirmata import Arduino, SERVO
from time import sleep

board = Arduino('COM3')
board.digital[10].mode = SERVO

def rotateServo(pin, angle):
    board.digital[10].write(angle)
    sleep(0.015)

while True:
    for i in range(0,180):
        rotateServo(10, i)
    for i in range(180,1,-1):
        rotateServo(10, i)