from broker import Broker

BROKER = Broker()
TOPIC  =  'scox/v1/retailer1/store2/terminal01/interventions/requests'
PAYLOAD = '{"event":"createIntervention","params":{"type":"dataNeeded", "operation":"HelloMessage", "time":"2022-02-16T14:52:32","sourceTopic":"scox/v1/retailer1/store2/terminal01/interventions/requests", "severity":"immediate","dataEntry":[{"inputs":[{"type":"buttonList","buttons":[{"data":"cOk","caption":{"id":"ScotApp_58","section":"Intervention"}}]}],"summary":{"text":"Welcome to NCR SelfServ� Checkout"},"caption":{"id":"ScotApp_809","section":"Intervention"}}],"loginRequired":false}}'
IP = "127.0.0.1"
PORT = 8000

def connection(ip,port):
    ip = ip
    port = port
    BROKER.connect(ip, port)
    if not BROKER.is_connected()  :
        print("Failed to connect to broker")
        exit
    else:
        print("Connection with broker successsfull.")

def pubsub():
    BROKER.subscribe(TOPIC)
    BROKER.publishFile(TOPIC, './file/request.json', )

def printmessage():
    msg = BROKER.get_message(120)
    if msg == "":
        print("received empty message")
    else:
        print("received message" + msg.get_payload() )

connection(IP, PORT)
pubsub()  
printmessage()