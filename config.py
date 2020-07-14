#Pinos de utilização pelo hardware
UNLOCK_DOOR_PIN = 15
LED_RED_PIN = 16
LED_YELLOW_PIN  = 18
LED_GREEN_PIN   = 22
BUZZY_PIN = 24
BUTTON_PRESSED = 0 #TODO: Configurar pino

#Nível de tolerância
TOLERANCE = 0.4

#Nome da zona utilizada
ID_ZONE = 1

# Maquina Producao
API_CADASTRO_RECEPCIONISTA = 'http://api-cadastro-villaaymore.marlin.com.br/'
API_CADASTRO_RECEPCIONISTA_LOGIN = 'recepcionista@villaymore.com.br'
API_CADASTRO_RECEPCIONISTA_SENHA = '123456'


#Endereço da API RODANDO LOCAL RASPBERRY /  VERIFICAR O IP QUE A API ESTARÁ RODANDO
API_DETECCAO = 'http://192.168.0.107:5001/'
API_RECONHECIMENTO = 'http://192.168.0.107:5003/'

#Mokc
# SIMULAR_RASPBERRY = False #Marcar como False em produção / Utilização fora do Raspberry EX: Maquina virtual

HABILITAR_DETECCAO = True
HABILITAR_RECONHECIMENTO = True

#Tempo de Pausa

TEMPO_PAUSE = 5
