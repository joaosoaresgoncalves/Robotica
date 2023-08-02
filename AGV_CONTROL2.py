from time import sleep
from signal import pause
from time import sleep
from gpiozero import Motor, InputDevice

FORWARD = 1
BACKWARD = 2
LEFT = 3
RIGHT = 4
STOP = 5

class AGV_CONTROL:

    def __init__(self):
        # Motor forward, backward, enable (pwm)
        self.motor_right = Motor(16, 26, 13)
        #___________________________________pins (15,14,18)

        # IR Sensors
        self.sensor_left = InputDevice(6)
        self.sensor_right = InputDevice(5)


    def schedule(self, event_name, event_value, speed, intensity):

        if event_name == 'INIT':
            print("AGV: Init")
            self.last = 0
            return [event_value, None, None]

        #______________________ procurar o event name na function block que dá ordem para avançar
        #do mesmo formato das condicoes de cima e de baixo
            self.move_forward(speed)
            sleep(0.5)
            while self.follow_line(speed, intensity):
                pass

            return [None, event_value, None]

        elif event_name == "STOP":
            self.stop()

            return [None, None, event_value]

    def move_forward(self, speed=1):
        #_____________
        #______________ teste de erro (teste if) que retorna nada se speed nao tiver nas condicoes [0,1]

        if self.last != FORWARD:
            print("AGV: Moving forward")
            self.last = FORWARD

        self.motor_right.forward(speed)
        self.motor_left.forward(speed)

    def move_backward(self, speed=1):
        #_____________
        #______________ teste de erro (teste if) que retorna nada se speed nao tiver nas condicoes [0,1]

        if self.last != BACKWARD:
            print("AGV: Moving backward")
            self.last = BACKWARD

        self.motor_right.backward(speed)
        self.motor_left.backward(speed)

    def turn_left(self, speed=1, intensity=1):
        if intensity <= 0 or intensity > 1 or speed > 1 or speed < 0:
            return

        if self.last != LEFT:
            print("AGV: Turning left")
            self.last = LEFT

        
        #ordem para o motor da direita andar (intesity * speed) e o da esquerda ((1-intesity)*speed)


    def turn_right(self, speed=1, intensity=1):
        if intensity <= 0 or intensity > 1 or speed > 1 or speed < 0:
            return

        if self.last != RIGHT:
            print("AGV: Turning right")
            self.last = RIGHT

        self.motor_right.forward((1 - intensity) * speed)
        self.motor_left.forward(intensity * speed)

    def stop(self):
        if self.last != STOP:
            print("AGV: Stoping")
            self.last = STOP
        self.motor_right.stop()
        self.motor_left.stop()

    def follow_line(self, speed=1, intensity=1):
        if self.sensor_left.is_active and self.sensor_right.is_active:
            print("Stop condition detected")
            #_____ condicao para parar 
            #_____e, se estiver parado, dar return falso, se não estiver, return verdadeiro
        elif self.sensor_left.is_active:
            self.turn_right(speed, intensity)
            sleep(0.02)
        elif self.sensor_right.is_active:
            self.turn_left(speed, intensity)
            sleep(0.02)
        else:
            self.move_forward(speed)
            sleep(0.02)
        #_____

    def __del__(self):
    	self.motor_right.close()
    	self.motor_left.close()
    	self.sensor_right.close()
    	self.sensor_left.close()
