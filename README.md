Sistema de Controle de Acesso por Reconhecimento Facial
📋 Visão Geral

Sistema de controle de acesso inteligente que utiliza reconhecimento facial para autorizar ou negar a abertura de portas. O sistema combina visão computacional com hardware físico para criar uma solução completa de segurança.

🚀 Funcionalidades

    Detecção de rostos em tempo real

    Reconhecimento facial com tolerância configurável

    Controle de hardware: LEDs, buzzer e tranca elétrica

    Modos de operação: entrada ("in") e saída ("out")

    Logging completo de eventos do sistema

    Interface por linha de comando configurável

🏗️ Arquitetura

Camera → Detecção → Reconhecimento → Decisão → Hardware
   │         │           │             │         │
   └─OpenCV──┴──API──────┴──API────────┴──GPIO──┘

Componentes Principais

    Módulo de Captura (cv2.VideoCapture) - Captura vídeo da câmera

    API de Detecção (APIDeteccao) - Detecta rostos nos frames

    API de Reconhecimento (APIReconhecimento) - Identifica pessoas conhecidas

    API de Abertura (APIAbertura) - Gerencia abertura da porta

    Handler de Hardware (HardwareHandler) - Controla dispositivos físicos

📦 Pré-requisitos
Dependências

pip install opencv-python
# APIs customizadas (apis/, handlers/, config/)

Hardware Requerido

    Câmera USB compatível com OpenCV

    LEDs (vermelho, amarelo, verde)

    Buzzer ativo/passivo

    Tranca elétrica 12V

    Placa de controle GPIO (Raspberry Pi/Arduino)

    Fonte de alimentação adequada

⚙️ Instalação
    Clone o repositório

git clone <repositorio>
cd opendoor-system

    Configure o hardware

    Conecte os LEDs nos pinos GPIO correspondentes

    Conecte o buzzer no pino configurado

    Conecte a tranca elétrica no relé

    Configure a câmera USB

    Configure as APIs
    Edite o arquivo config/__init__.py:

API_DETECCAO = "http://endereco-api-deteccao:5000"
API_RECONHECIMENTO = "http://endereco-api-reconhecimento:5001"
TOLERANCE = 0.6  # Tolerância para reconhecimento
ID_ZONE = "zona-1"

🎯 Uso
Execução Básica

# Modo entrada (padrão)
python opendoor.py --mode in

# Modo saída
python opendoor.py --mode out

Parâmetros da CLI
python opendoor.py [OPÇÕES]

Opções:
  -h, --help            Mostra esta mensagem de ajuda
  -l, --log LOG         Nível de log (DEBUG, INFO, WARNING, ERROR, CRITICAL)
  -m, --mode MODE       Modo de operação (in | out)
  -d, --detect DETECT   Endereço da API de Detecção Facial
  -r, --recognize RECOGNIZE
                        Endereço da API de Reconhecimento Facial
  -t, --tolerance TOLERANCE
                        Tolerância para reconhecimento (0.0-1.0)
  -z, --zoneID ZONEID   ID da zona de controle
  -i, --ip IP           IP para bind da API interna
  -p, --port PORT       Porta da API interna

Exemplos de Uso

# Modo debug com tolerância baixa
python opendoor.py --log DEBUG --mode in --tolerance 0.4

# Zona específica com APIs customizadas
python opendoor.py --zoneID "sala-server" --detect "192.168.1.100:5000"

# Produção com logging mínimo
python opendoor.py --log ERROR --mode out

🔧 Configuração do Hardware
Pinagem (GPIO - Exemplo Raspberry Pi)

# Configuração em HardwareHandler
LED_VERMELHO = 17    # GPIO 17 - Acesso negado
LED_AMARELO = 27     # GPIO 27 - Aguardando/Processando
LED_VERDE = 22       # GPIO 22 - Acesso permitido
BUZZER = 23          # GPIO 23 - Feedback sonoro
RELE_TRANCA = 24     # GPIO 24 - Controle da tranca

Diagrama de Conexões

+------------+          +-----------------+
|   Câmera   |----USB---|   Raspberry Pi  |
+------------+          +-------+---------+
                                |
                      +---------+---------+
                      |   Controle GPIO   |
                      +---------+---------+
                                |
                 +--------------+--------------+
                 |       |       |      |      |
                LED     LED     LED   Buzzer  Relé
               Verm.   Amar.   Verde           |
                                                |
                                         +------+------+
                                         |  Tranca 12V |
                                         +-------------+

🚦 Fluxo de Operação
Modo "in" (Entrada)

    Detecta rosto na câmera

    Reconhece pessoa (se habilitado)

    Se reconhecida → Abre porta

    Se desconhecida → Nega acesso

Modo "out" (Saída)

    Detecta movimento/rosto

    Abre porta automaticamente (sem reconhecimento)

Sinalização Visual/Sonora

    LED Vermelho: Acesso negado

    LED Amarelo: Processando/Aguardando

    LED Verde: Acesso permitido

    Buzzer curto: Sucesso

    Buzzer longo: Falha

📊 Logging e Monitoramento
Arquivos de Log

    Local: log/teste.log

    Formato: [timestamp] {arquivo:linha} [nível] mensagem

Níveis de Log

    DEBUG: Detalhes de processamento

    INFO: Eventos do sistema

    WARNING: Problemas não críticos

    ERROR: Falhas operacionais

    CRITICAL: Falhas do sistema

Exemplo de Log

[2024-01-15 10:30:15] {opendoor.py:150} [INFO] Opendoor started
[2024-01-15 10:30:20] {opendoor.py:200} [DEBUG] tempo APIDeteccao().getRosto = 0.245s
[2024-01-15 10:30:21] {opendoor.py:210} [INFO] Acesso permitido para usuário conhecido

🛠️ Desenvolvimento
Estrutura do Projeto

opendoor-system/
├── apis/                    # APIs de serviço
│   ├── api_deteccao.py     # Detecção facial
│   ├── api_reconhecimento.py # Reconhecimento
│   └── api_abertura.py     # Controle de porta
├── handlers/               # Controladores de hardware
│   └── hardware_handler.py # GPIO/LEDs/Buzzer
├── config/                 # Configurações
│   └── __init__.py        # Variáveis globais
├── log/                    # Logs do sistema
├── opendoor.py            # Ponto de entrada
└── README.md              # Esta documentação

Extendendo o Sistema

Para adicionar novas funcionalidades:

    Nova API de serviço:

# apis/api_nova.py
class APINova:
    def processar(self, dados):
        # Implementação
        return resultado

    Novo hardware:

# handlers/hardware_handler.py
class HardwareHandler:
    def novo_dispositivo(self, estado):
        # Controle GPIO
        GPIO.output(PINO_NOVO, estado)

🔒 Segurança
Considerações

    Dados biométricos: Armazene com criptografia

    Comunicação: Use HTTPS para APIs externas

    Autenticação: Implemente nas APIs

    Logs sensíveis: Evite registrar dados pessoais

Melhorias Recomendadas

    Autenticação por token nas APIs

    Criptografia de frames transmitidos

    Rate limiting para prevenção de ataques

    Backup de banco de dados de rostos

🐛 Solução de Problemas
Problemas Comuns

    Câmera não detectada

# Verifique dispositivos USB
ls /dev/video*
# Teste com outro software
sudo apt install guvcview
guvcview

    GPIO não funciona

# Verifique permissões
groups $USER
# Adicione ao grupo gpio
sudo usermod -a -G gpio $USER

    APIs não respondem

# Teste conectividade
curl http://endereco-api:porta/health
# Verifique logs
tail -f log/teste.log

Debug Avançado

# Executar com máximo de logs
python opendoor.py --log DEBUG --mode in 2>&1 | tee debug.log

# Monitorar processos
sudo lsof -i :5007
top -p $(pgrep -f opendoor.py)

📈 Performance
Requisitos do Sistema

    CPU: Mínimo 2 cores

    RAM: 2GB+ (depende da resolução)

    Storage: 100MB para logs

    OS: Linux (testado em Raspberry Pi OS)

Otimizações

    Reduza resolução da câmera para 720p

    Ajuste FPS no loop principal

    Use processamento assíncrono para APIs

    Cache de resultados de reconhecimento

🤝 Contribuição

    Fork o repositório

    Crie uma branch (git checkout -b feature/nova-funcionalidade)

    Commit suas mudanças (git commit -am 'Add nova funcionalidade')

    Push para a branch (git push origin feature/nova-funcionalidade)

    Crie um Pull Request

📄 Licença

[Inserir informação de licença aqui]
📞 Suporte
Canais

    Issues: [Link para issue tracker]

    Email: suporte@empresa.com

    Documentação: [Link para docs completos]

Informações para Suporte Técnico

Ao reportar problemas, inclua:

python opendoor.py --version  # Se implementado
python --version
uname -a
cat /etc/os-release
