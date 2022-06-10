from flask import Flask
import socket
import os
import time

app= Flask("Clustering Algorithms")


@app.route("/")
def hello():
    return "ApiRest attiva: /ALGORITMO/ID per richiedere il servizio"


@app.route("/DBSCAN/<int:db_id>")
def dbscanMethod(db_id):
    print("Richiesta Ricevuta!")
    try:
        s = socket.socket()
        print("Socket successfully created...\n")

    except socket.error as err:
        print("socket creation failed with error %s" % (err))
    s.connect((socket.gethostbyname(os.environ["CLUSTER-SERVER-IP"]), os.environ["CLUSTER-SERVER-PORT"]))
    s.sendall(("DBSCAN:"+str(db_id)).encode());
    time.sleep(2)
    s.close()
    return "Sending request for DBSCAN algorithm on "+str(db_id)+" DB...\nWait few minutes and check your email!"

@app.route("/KMEANS/<int:db_id>")
def kmeansMethod(db_id):
    try:
        s = socket.socket()
        print("Socket successfully created")
    except socket.error as err:
        print("socket creation failed with error %s" % (err))
    s.connect((socket.gethostbyname(os.environ["CLUSTER-SERVER-IP"]), os.environ["CLUSTER-SERVER-PORT"]))
    s.sendall(("KMEANS:" + str(db_id)).encode());
    time.sleep(2)
    s.close()
    return "Sending request for KMEANS algorithm on "+str(db_id)+" DB...\nWait few minutes and check your email!"
