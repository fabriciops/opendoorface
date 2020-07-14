# USAGE
# python opendoor.py --ip 0.0.0.0 --port 8000
import argparse
import json, time, logging
import logging
import time
import cv2
import config
from apis.api_deteccao import APIDeteccao
from apis.api_reconhecimento import APIReconhecimento
from apis.api_abertura import APIAbertura
from handlers.hardware_handler import HardwareHandler
from concurrent.futures import process

def main():
	led.turn_ALL_LEDS(True)
	time.sleep(2.0)
	led.turn_ALL_LEDS(False)
	led.buzzy()
	print("Módulo abertura porta \n " + args["mode"])
	gerarImagem()

def pause():
	time.sleep(2.0)


def openDoor():
    
	led.turn_LED('red', False)
	led.turn_LED('yellow', False)
	led.turn_LED('green', True)
	led.unlock_door()
	led.buzzy()
	time.sleep(1.5)

def dontOpenDoor(self):
    
	person = "desconhecido"

	led.turn_LED('green', False)
	led.turn_LED('red', True)
	led.buzzy_false()
	led.turn_LED('yellow', True)

def openDoorOut():
    
	led.turn_LED('yellow', False)
	led.turn_LED('green', True)
	led.buzzy_false()
	
	#Abre porta
	led.unlock_door()
	
	time.sleep(2.0)
	led.turn_LED('green', False)
	led.turn_LED('red', False)
	pause_deteccao = time.time()
	
	logging.info('Pessoa desconhecida tentou acessar a zona' (args["zoneID"]))
	time.sleep(2.0)
	pause_deteccao = time.time()

def gerarImagem():
    	
	looping = 0
	tempo_inicial = time.time()
	pause_deteccao =  3

	while(True):
    	
		led.turn_LED('green', False)
		led.turn_LED('red', False)
		# logging.info("flag, encodedImage: Start:WHILE.")

		tempo_inicio_loop = time.time()
		looping += 1

		if(looping == 8):

			looping = looping - looping

		# Capture frame-by-frame
		try:
			ret, frame = vs.read()
			led.turn_LED('yellow', True)
		
			#teste loop
			if frame is None:

				continue

			if(config.HABILITAR_DETECCAO == True):

				# logging.info('Detecção habilitada')
				tempo_inicio_loop = time.time()
				start_api_detect = time.time()
				rostos = APIDeteccao().getRosto(frame)
				
				logging.debug('tempo APIDeteccao().getRosto = {: }' .format(time.time() - start_api_detect))

				if rostos is not None:
					logging.debug('rostos {:}'.format(rostos['rostos']))

					for rosto in rostos['rostos']:
						(x, y, w, h) = rosto['coordenadas']
						frame_cropped = frame[y:y+h, x:x+w]

					if(config.HABILITAR_RECONHECIMENTO == True):
    					
						# TODO log tempo inicio de reconhecimento
						resultadoReconhecimento = APIReconhecimento().reconhecer(frame_cropped)

						if resultadoReconhecimento is not None :
							
							rosto['reconhecido']= True
						else:
    						
							rosto['reconhecido']= False

					if(rosto['reconhecido'] == True):

						if(looping == 1):
    						
							openDoor()
						else:
    						#Aguardando acesso
							led.turn_LED('red', True)

					else:
    					
						if(args["mode"] == "in"):
							
							led.turn_LED('red', True)
						
						else:
    						
							if(looping == 1):
    							
								openDoor()
							else:
								#Aguardando acesso
								led.turn_LED('red', True)
    						
							

    								

			# Our operations on the frame come here
			color = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)

			# encode the frame in JPEG format
			(flag, encodedImage) = cv2.imencode(".jpg", frame)
			cv2.imwrite
			# ensure the frame was successfully encoded
			if not flag:
				continue

		except Exception as e:
			logging.debug('Except on Camera Frame read. Error = ' + str(e))
			logging.debug('Time per loop = {: }' .format(time.time() - tempo_inicio_loop))

# check to see if this is the main thread of execution
if __name__ == '__main__':
	ap = argparse.ArgumentParser()
	ap.add_argument("-l", "--log", type=str, default="INFO", help="Type log level (DEBUG, INFO, WARNING, ERROR, CRITICAL)")
	ap.add_argument("-m", "--mode", type=str, default="in", help="Type mode (in | out)")
	ap.add_argument("-d", "--detect", type=str, default=config.API_DETECCAO, help="Type IP or name for the Face Detection API")
	ap.add_argument("-r", "--recognize", type=str, default=config.API_RECONHECIMENTO, help="Type IP or name for the Face Recognition API")
	ap.add_argument("-t", "--tolerance", type=float, default=config.TOLERANCE, help="Type the tolerance used to recognize faces")
	ap.add_argument("-z", "--zoneID", type=str, default=config.ID_ZONE, help="Type the zone ID number/name where this device will operate")
	ap.add_argument("-i", "--ip", type=str, default="0.0.0.0", help="Type IP for the API")
	ap.add_argument("-p", "--port", type=int, default=5007, help="Type port where API is listening from")

	args = vars(ap.parse_args())

	LEVELS = {'debug': logging.DEBUG,
				'info': logging.INFO,
				'warning': logging.WARNING,
				'error': logging.ERROR,
				'critical': logging.CRITICAL}
	level = LEVELS.get(args["log"], logging.INFO)

	#config logging
	logging.basicConfig(filename='log/teste.log', format='[%(asctime)s] {%(pathname)s:%(lineno)d} [%(levelname)s] %(message)s', level=logging.INFO)

	logging.info("Opendoor started")
	logging.info("logging level = {}".format(args["log"]))
	logging.info("mode = {}".format(args["mode"]))
	logging.info("API Face Detection = {}".format(args["detect"]))
	logging.info("API Face Recognition = {}".format(args["recognize"]))
	logging.info("Tolerance = {}".format(args["tolerance"]))
	

	vs = None

	#zona = None
	led = HardwareHandler()
	faceEncontrada = False

	vs = cv2.VideoCapture(0)
	
	ip = args["ip"]
	port = args["port"]

	main()


