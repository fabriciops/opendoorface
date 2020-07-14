import config
import logging
import time
import RPi.GPIO as GPIO
from apis.api_deteccao import APIDeteccao

class HardwareHandler:

    '''
        Gerenciador de estruturas de hardware
    '''
    def __init__(self):
        logging.info('HardwareManagementHandler is initialized')
        # if config.SIMULAR_RASPBERRY: #Adicionado para simular não acesso da camera
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)

        GPIO.setup(config.LED_GREEN_PIN, GPIO.OUT)
        GPIO.setup(config.LED_YELLOW_PIN, GPIO.OUT)
        GPIO.setup(config.LED_RED_PIN, GPIO.OUT)
        GPIO.setup(config.UNLOCK_DOOR_PIN, GPIO.OUT)
        GPIO.setup(config.BUZZY_PIN, GPIO.OUT)

        logging.debug('GPIO %d, %d, %d and %d are configured as Output', config.LED_GREEN_PIN, config.LED_YELLOW_PIN,
                    config.LED_RED_PIN, config.UNLOCK_DOOR_PIN)

        logging.debug('LED green connected to GPIO %d', config.LED_GREEN_PIN)
        logging.debug('LED yellow connected to GPIO %d', config.LED_YELLOW_PIN)
        logging.debug('LED red connected to GPIO %d', config.LED_RED_PIN)
        logging.debug('Unlock Door connected to GPIO %d', config.UNLOCK_DOOR_PIN)
        logging.debug('Buzzy connected to GPIO %d', config.BUZZY_PIN)

        GPIO.output(config.LED_GREEN_PIN, False)
        GPIO.output(config.LED_YELLOW_PIN, False)
        GPIO.output(config.LED_RED_PIN, False)
        GPIO.output(config.UNLOCK_DOOR_PIN, False)
        GPIO.output(config.BUZZY_PIN, False)

        logging.debug('LEDs are set to zero')
        logging.debug('Unlock Door is set to zero')
        logging.debug('Hardware setup is done')
        self.portaaberta = False
    
        
    def turn_LED(self, color, state):
    #     logging.info("LED {color} is {state}")
    #     print("LED {} is {}".format(color, state))
        if color == "red":
            GPIO.output(config.LED_RED_PIN, state)
        elif color == "yellow":
            GPIO.output(config.LED_YELLOW_PIN, state)
        else:
            GPIO.output(config.LED_GREEN_PIN, state)

    def turn_ALL_LEDS(self, state):
        logging.info('LEDS are turned {}'.format("ON" if state else "OFF"))
        GPIO.output(config.LED_RED_PIN, state)
        GPIO.output(config.LED_GREEN_PIN, state)
        GPIO.output(config.LED_YELLOW_PIN, state) 

    def unlock_door(self):
        logging.info('Unlock door')
        GPIO.output(config.UNLOCK_DOOR_PIN, True)
        time.sleep(3.0)
        GPIO.output(config.UNLOCK_DOOR_PIN, False)

        

    def lock_door(self):
        logging.info('lock door')
        GPIO.output(config.UNLOCK_DOOR_PIN, False)
       
    def buzzy(self):
        logging.info('Buzzy')
        GPIO.output(config.BUZZY_PIN, True)
        time.sleep(0.1)
        GPIO.output(config.BUZZY_PIN, False)
        time.sleep(0.1)
        GPIO.output(config.BUZZY_PIN, True)
        time.sleep(0.1)
        GPIO.output(config.BUZZY_PIN, False)
        time.sleep(0.1)
        GPIO.output(config.BUZZY_PIN, True)
        time.sleep(0.1)
        GPIO.output(config.BUZZY_PIN, False)
        time.sleep(0.2)
        GPIO.output(config.BUZZY_PIN, False)
        time.sleep(0.2)
        GPIO.output(config.BUZZY_PIN, True)
        time.sleep(0.1)
        GPIO.output(config.BUZZY_PIN, False)
        time.sleep(0.1)
        GPIO.output(config.BUZZY_PIN, True)
        time.sleep(0.1)
        GPIO.output(config.BUZZY_PIN, False)
        time.sleep(0.1)
        GPIO.output(config.BUZZY_PIN, True)
        time.sleep(0.1)
        GPIO.output(config.BUZZY_PIN, False)

    def buzzy_false(self):
        logging.info('Buzzy')
        GPIO.output(config.BUZZY_PIN, True)
        time.sleep(1.0)
        GPIO.output(config.BUZZY_PIN, False)
        
    
    
