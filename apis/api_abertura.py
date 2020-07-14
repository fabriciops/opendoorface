import config
import requests
import json
import logging

class APIAbertura:
    """Classe de integração com a API de monitoramento
    """
    dataLogin = {"email": config.API_CADASTRO_RECEPCIONISTA_LOGIN, "senha": config.API_CADASTRO_RECEPCIONISTA_SENHA }

    routes = {
        "login": config.API_CADASTRO_RECEPCIONISTA + 'login',
        "pessoa/comfaceid": config.API_CADASTRO_RECEPCIONISTA + 'pessoa/comfaceid',
        "zona/id": config.API_CADASTRO_RECEPCIONISTA + 'zona/'+ str(config.ID_ZONE),
        "dispositivo/id": config.API_CADASTRO_RECEPCIONISTA + 'config.ID_DISPOSITIVO',
        "log": config.API_CADASTRO_RECEPCIONISTA + 'log',
    
    }

    def _getHeaderLogin(self):
        headers = {"Content-Type": "application/json"}
        return headers
    
    def _getHeadersAuthorization(self):
        headers = { "Authorization": self._getToken(), "Content-Type": "application/json"}
        return headers

    def _getToken(self):
        responseLogin = requests.post(self.routes['login'], 
            headers=self._getHeaderLogin(), 
            verify=False,
            json=self.dataLogin)
        
        if(responseLogin and responseLogin.status_code == 200):
            tokenObject = json.loads(responseLogin.content.decode('ASCII'))
            token = 'Bearer ' + tokenObject['token']
            logging.debug('token: ', token)
        
            return token
    
    def getUsuariosComFacesCadastradas(self):
        """Obtém o usuários com faces cadastradas
        """
        print("url: " ,self.routes['pessoa/comfaceid'])
        responseRequest = requests.get(self.routes['pessoa/comfaceid'], 
            headers=self._getHeadersAuthorization(),
            verify=False)

        if(responseRequest and responseRequest.status_code == 200):
            resultObject = json.loads(responseRequest.content.decode())

            if(resultObject):
                logging.debug('resultObject: ', resultObject)
                return resultObject

        return None

    def getZona(self):
        """Obtém o Zonas cadastradas
        """
        print("url: " ,self.routes['zona/id'])
        responseRequest = requests.get(self.routes['zona/id'], 
            headers=self._getHeadersAuthorization(),
            verify=False)

        if(responseRequest and responseRequest.status_code == 200):
            resultObject = json.loads(responseRequest.content.decode())

            if(resultObject):
                logging.debug('resultObject: ', resultObject)
                return resultObject

        return None

    def getDispositivo(self):
        """Obtém o Dispositivo cadastradas
        """
        print("url: " ,self.routes['dispositivo/id'])
        responseRequest = requests.get(self.routes['dispositivo/id'], 
            headers=self._getHeadersAuthorization(),
            verify=False)

        if(responseRequest and responseRequest.status_code == 200):
            resultObject = json.loads(responseRequest.content.decode())

            if(resultObject):
                logging.debug('resultObject: ', resultObject)
                return resultObject

        return None

    def insertLog(self):
        """Obtém o Log 'QUEM ESTEVE AONDE E QUANDO?'
        """
        print("url: " ,self.routes['log'])
        responseRequest = requests.post(self.routes['dispositivo/id'], 
            headers=self._getHeadersAuthorization(),
            verify=False)

        if(responseRequest and responseRequest.status_code == 200):
            resultObject = json.loads(responseRequest.content.decode())

            if(resultObject):
                logging.debug('resultObject: ', resultObject)
                return resultObject

        return None