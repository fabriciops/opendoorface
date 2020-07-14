import config
import requests
import json
import logging
import cv2


class APIReconhecimento:
    """Classe de integração com a API de monitoramento
    """
    """Classe de integração com a API de Deteccao
    """
    routes = {
        "reconhecer": config.API_RECONHECIMENTO + 'reconhecer',
             
    }

    logging.info(routes) 
    print(routes)
    
    def reconhecer(self, frame):
        """Obtém o usuários com faces cadastradas
        """        
        img_encoded = cv2.imencode('.jpg', frame)[1]

        print("img_encoded " + img_encoded)

        #Monta o objeto imagem com o nome da foto
        file_img = {'imagem': ('image.jpg', img_encoded.tostring(), 'image/jpeg', {'Expires': '0'})}

        print("file_img " + file_img)

        dataUser = { 
            "imagem": file_img,
            #"numero_face": numero_face,
        }

        print("dataUser: " + dataUser)

        response = None
        try:
            response = requests.post(self.routes['reconhecer'], 
            # headers=self._getHeadersBinary(), 
            verify=False,
            data=dataUser,
            files=file_img)
            
            logging.info('Response: {}'.format(response))
            print('response', response)
        except:
            print('Não foi possível obter comunicação com a API de reconhecimento')
            logging.info('Não foi possível obter comunicação com a API de reconhecimento') 
            return None       

        if(response and response.status_code == 200):
            resultObject = json.loads(response.content.decode())

            if(resultObject):
                logging.debug('resultObject: {:}'.format(resultObject))
                return resultObject

        return None 
    
    def getCadastrados(self):
        """Obtém o usuários com faces cadastradas
        """
        print("url: " ,self.routes['pessoa/comfaceid'])
        response = requests.get(self.routes['pessoa/comfaceid'], 
            headers=self._getHeadersAuthorization(),
            verify=False)

        if(responseRequest and responseRequest.status_code == 200):
            resultObject = json.loads(responseRequest.content.decode())

            if(resultObject):
                logging.debug('resultObject: ', resultObject)
                return resultObject

        return None
    
    def reconhecendoFace(frame, x, y, w, h, rService):

        global cv2

        #Recortando frame
        frame_cropped = frame[y:y+h, x:x+w]
        
        #Reconhecendo face
        response = rService.recognizeFileFull(frame_cropped)
        print('response', response)

        (flag, encodedImage) = cv2.imencode(".jpg", frame_cropped)

        if response is not None:
            print('response', response)

            data = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            
            zonaId = zona[0]['id']
            print('zonaId', zonaId)

            print('response', response)
            if float(response[0][1]['distance']) <= config.TOLERANCE:
                print('response', response)
                pessoaId = response[0][0]
                print('pessoaId', pessoaId)
                #logService.logPortaAbertaUsuarioCadastrado(pessoaId, zonaId, config.ID_DISPOSITIVO, encodedImage)

                print('{} passou pela zona {} em {}. tolerance = {}'
                    .format(response[0][1]['name'], zona[0]['id'], data, config.TOLERANCE))

                cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
                cv2.putText(frame, '{}'.format(response[0][1]['name'] + ' autorizado. Porta aberta'), (10, 400), cv2.FONT_HERSHEY_DUPLEX, 0.7, (0, 255, 0))
            else:
                # logService.logPortaFechadaUsuarioDesconhecido(zonaId, config.ID_DISPOSITIVO, encodedImage)
                
                print('Pessoa desconhecida passou pela zona {} em {}. tolerance = {}'
                    .format(zona[0]['id'], data, config.TOLERANCE))

                cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
                cv2.putText(frame, '{}'.format('Desconhecido'), (10, 400), cv2.FONT_HERSHEY_DUPLEX, 0.7, (0, 0, 255))
            # time.sleep(5.0)