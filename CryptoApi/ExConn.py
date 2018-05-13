from ExConnModules import *

def getSymbols():
    symbols = []
    if os.path.exists("Tikers.txt"):
        f = open("Tikers.txt", "r")
        fileData = f.readlines()
        for i in range(0, len(fileData)):
            symbols = symbols + fileData[i].split(",")
        symbols = [x.strip() for x in symbols]
    return symbols


def hitbtcAgg(symbols):
    data= []
    try:
        data= hitbtcRequest(symbols=symbols)
    except:
        pass
    return data


def okexAgg(symbols):
    data= []
    try:
        data= okexRequest(symbols=symbols)
    except:
        pass
    return data

def liquiAgg(symbols):
    data= []
    try:
        data= liquiRequest(symbols=symbols)
    except:
        pass
    return data

def krakenAgg(symbols):
    data= []
    try:
        data= krakenRequest(symbols=symbols)
    except:
        pass
    return data


def binanceAgg(symbols):
    data= []
    try:
        data= binanceRequest(symbols=symbols)
    except:
        pass
    return data


def kucoinAgg(symbols):
    data= []
    try:
        data= kucoinRequest(symbols=symbols)
    except:
        pass
    return data


def huobiAgg(symbols):
    data= []
    try:
        data= huobiRequest(symbols=symbols)
    except:
        pass
    return data


def yobitAgg(symbols):
    data= []
    try:
        data= huobiRequest(symbols=symbols)
    except:
        pass
    return data


def bitfinexAgg(symbols):
    data= []
    try:
        data= bitfinexRequest(symbols=symbols)
    except:
        pass
    return data

def bittrexAgg(symbols):
    data= []
    try:
        data= bittrexRequest(symbols=symbols)
    except:
        pass
    return data

def poloniexAgg(symbols):
    data= []
    try:
        data= poloniexRequest(symbols=symbols)
    except:
        pass
    return data

def gateAgg(symbols):
    data= []
    try:
        data= poloniexRequest(symbols=symbols)
    except:
        pass
    return data


