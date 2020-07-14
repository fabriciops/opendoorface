import config
import requests
import json
import logging
import cv2

class APIDeteccao:
    """Classe de integração com a API de Deteccao
    """
    routes = {
        "rosto": config.API_DETECCAO + 'rosto'        
    }
    
    def getRosto(self, frame):
        """Obtém o usuários com faces cadastradas
        """

        print("teste getRosto")   
        img_encoded = cv2.imencode('.jpg', frame)[1]

        #Monta o objeto imagem com o nome da foto
        file_img = {'imagem': ('image.jpg', img_encoded.tostring(), 'image/jpeg', {'Expires': '0'})}

        dataUser = { 
            "imagem": file_img,
            
        }

        response = None
        try:
            response = requests.post(self.routes['rosto'], 
            
            # headers=self._getHeadersBinary(), 
            verify=False,
            data=dataUser,
            files=file_img) 

            print(response)
            
            # logging.info('Response: {}'.format(response))
            # print('response', response)
        except:
            print('Não foi possível obter comunicação com a API de detecção')
            logging.info('Não foi possível obter comunicação com a API de detecção') 
            return None       

        if(response and response.status_code == 200):
            resultObject = json.loads(response.content.decode())

            if(resultObject):
                logging.debug('resultObject: {:}'.format(resultObject))
                return resultObject

        return None

   
