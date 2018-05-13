import ccxt
import idexExchange
import pandas as pd
import datetime
import os
import numpy as np

def getSymbols():
    symbols = []
    if os.path.exists("Tikers.txt"):
        f = open("Tikers.txt", "r")
        fileData = f.readlines()
        for i in range(0, len(fileData)):
            symbols = symbols + fileData[i].split(",")
        symbols = [x.strip() for x in symbols]
        symbols= list(set(symbols))
    return symbols

def hitbtcAgg(symbols):
    result = []
    try:
        hitbtc = ccxt.hitbtc({
            'apiKey': 'apiKey',
            'secret': 'secret',
            'options': {'adjustForTimeDifference': True}
        })
        totalBalance = hitbtc.fetch_balance()["free"]
        exchangeSymbols= hitbtc.symbols
        checkSymbols = list(np.intersect1d(exchangeSymbols, symbols))
        allData = hitbtc.fetch_tickers(checkSymbols)
        ethPrice = hitbtc.fetch_ticker("ETH/USDT")["last"]
        btcPrice = hitbtc.fetch_ticker("BTC/USDT")["last"]
        for s in checkSymbols:
            try:
                quote = s.split("/")[-1]
                dataSymbols= allData[s]
                coinBalance = totalBalance.get(s.split("/")[0], 0)
                volume = int(float(dataSymbols["baseVolume"]))
                ask = dataSymbols["ask"]
                bid = dataSymbols["bid"]
                last= float(dataSymbols["last"])
                if quote=="BTC":
                    volume = int(volume*btcPrice*last)
                elif quote=="ETH":
                    volume = int(volume*ethPrice*last)
                else:
                    volume = int(volume*dataSymbols["last"])
                volume= volume/ethPrice
                result.append(["hitbtc", s, coinBalance, ask, bid, volume])
            except:
                print("Hitbtc couldn`t get "+ s)
                continue
    except Exception as e:
        print(str(e)[:150])
    return(result)


def okexAgg(symbols):
    result = []
    try:
        okex = ccxt.okex({
            'apiKey': 'apiKey',
            'secret': 'secret',
            'options': {'adjustForTimeDifference': True}
        })
        totalBalance = okex.fetch_balance()["free"]
        exchangeSymbols= okex.symbols
        checkSymbols = list(np.intersect1d(exchangeSymbols, symbols))
        allData = okex.fetch_tickers(checkSymbols)
        ethPrice = okex.fetch_ticker("ETH/USDT")["last"]
        btcPrice = okex.fetch_ticker("BTC/USDT")["last"]
        for s in checkSymbols:
            try:
                quote = s.split("/")[-1]
                dataSymbols = allData[s]
                coinBalance = totalBalance.get(s.split("/")[0], 0)
                volume = int(float(dataSymbols["baseVolume"]))
                ask = dataSymbols["ask"]
                bid = dataSymbols["bid"]
                last = float(dataSymbols["last"])
                if quote == "BTC":
                    volume = int(volume * btcPrice * last)
                elif quote == "ETH":
                    volume = int(volume * ethPrice * last)
                else:
                    volume = int(volume * dataSymbols["last"])
                volume= volume/ethPrice
                result.append(["okex", s, coinBalance, ask, bid, volume])
            except:
                print("Okex couldn`t get " + s)
                continue
    except Exception as e:
        print(str(e)[:150])
    return (result)



def liquiAgg(symbols):
    result = []
    try:
        liqui = ccxt.liqui({
            'apiKey': 'apiKey',
            'secret': 'secret',
            'options': {'adjustForTimeDifference': True}
        })
        totalBalance = liqui.fetch_balance()["free"]
        exchangeSymbols= liqui.symbols
        checkSymbols = list(np.intersect1d(exchangeSymbols, symbols))
        allData = liqui.fetch_tickers(checkSymbols)
        ethPrice = liqui.fetch_ticker("ETH/USDT")["last"]
        btcPrice = liqui.fetch_ticker("BTC/USDT")["last"]
        for s in checkSymbols:
            try:
                quote = s.split("/")[-1]
                dataSymbols = allData[s]
                coinBalance = totalBalance.get(s.split("/")[0], 0)
                volume = int(float(dataSymbols["baseVolume"]))
                ask = dataSymbols["ask"]
                bid = dataSymbols["bid"]
                last = float(dataSymbols["last"])
                if quote == "BTC":
                    volume = int(volume * btcPrice * last)
                elif quote == "ETH":
                    volume = int(volume * ethPrice * last)
                else:
                    volume = int(volume * dataSymbols["last"])
                volume= volume/ethPrice
                result.append(["liqui", s, coinBalance, ask, bid, volume])
            except:
                print("Liqui couldn`t get " + s)
                continue
    except Exception as e:
        print(str(e)[:150])
    return (result)



def krakenAgg(symbols):
    result = []
    try:
        kraken = ccxt.kraken({
            'apiKey': 'apiKey',
            'secret': 'secret',
            'options': {'adjustForTimeDifference': True}
        })
        totalBalance = kraken.fetch_balance()["free"]
        exchangeSymbols= kraken.symbols
        checkSymbols = list(np.intersect1d(exchangeSymbols, symbols))
        allData = kraken.fetch_tickers(checkSymbols)
        ethPrice = kraken.fetch_ticker("ETH/USD")["last"]
        btcPrice = kraken.fetch_ticker("BTC/USD")["last"]
        for s in checkSymbols:
            try:
                quote = s.split("/")[-1]
                dataSymbols = allData[s]
                coinBalance = totalBalance.get(s.split("/")[0], 0)
                volume = int(float(dataSymbols["baseVolume"]))
                ask = dataSymbols["ask"]
                bid = dataSymbols["bid"]
                last = float(dataSymbols["last"])
                if quote == "BTC":
                    volume = int(volume * btcPrice * last)
                elif quote == "ETH":
                    volume = int(volume * ethPrice * last)
                else:
                    volume = int(volume * dataSymbols["last"])
                volume= volume/ethPrice
                result.append(["kraken", s, coinBalance, ask, bid, volume])
            except:
                print("Kraken couldn`t get " + s)
                continue
    except Exception as e:
        print(str(e)[:150])
    return (result)


def binanceAgg(symbols):
    result = []
    try:
        binance = ccxt.binance({
            'apiKey': 'apiKey',
            'secret': 'secret',
            'options': {'adjustForTimeDifference': True}
        })
        totalBalance = binance.fetch_balance()["free"]
        exchangeSymbols= binance.symbols
        checkSymbols = list(np.intersect1d(exchangeSymbols, symbols))
        allData = binance.fetch_tickers(checkSymbols)
        ethPrice = binance.fetch_ticker("ETH/USDT")["last"]
        btcPrice = binance.fetch_ticker("BTC/USDT")["last"]
        for s in checkSymbols:
            try:
                quote = s.split("/")[-1]
                dataSymbols = allData[s]
                coinBalance = totalBalance.get(s.split("/")[0], 0)
                volume = int(float(dataSymbols["baseVolume"]))
                ask = dataSymbols["ask"]
                bid = dataSymbols["bid"]
                last = float(dataSymbols["last"])
                if quote == "BTC":
                    volume = int(volume * btcPrice * last)
                elif quote == "ETH":
                    volume = int(volume * ethPrice * last)
                else:
                    volume = int(volume * dataSymbols["last"])
                volume= volume/ethPrice
                result.append(["binance", s, coinBalance, ask, bid, volume])
            except:
                print("Binance couldn`t get " + s)
                continue
    except Exception as e:
        print(str(e)[:150])
    return (result)



def kucoinAgg(symbols):
    result = []
    try:
        kucoin = ccxt.kucoin({
            'apiKey': 'apiKey',
            'secret': 'secret',
            'options': {'adjustForTimeDifference': True}
        })
        totalBalance = kucoin.fetch_balance()["free"]
        exchangeSymbols= kucoin.symbols
        checkSymbols = list(np.intersect1d(exchangeSymbols, symbols))
        allData = kucoin.fetch_tickers(checkSymbols)
        ethPrice = kucoin.fetch_ticker("ETH/USDT")["last"]
        btcPrice = kucoin.fetch_ticker("BTC/USDT")["last"]
        for s in checkSymbols:
            try:
                quote = s.split("/")[-1]
                dataSymbols = allData[s]
                coinBalance = totalBalance.get(s.split("/")[0], 0)
                volume = int(float(dataSymbols["baseVolume"]))
                ask = dataSymbols["ask"]
                bid = dataSymbols["bid"]
                last = float(dataSymbols["last"])
                if quote == "BTC":
                    volume = int(volume * btcPrice * last)
                elif quote == "ETH":
                    volume = int(volume * ethPrice * last)
                else:
                    volume = int(volume * dataSymbols["last"])
                volume= volume/ethPrice
                result.append(["kucoin", s, coinBalance, ask, bid, volume])
            except:
                print("Kucoin couldn`t get " + s)
                continue
    except Exception as e:
        print(str(e)[:150])
    return (result)



def huobiAgg(symbols):
    ##3Problem fetch ticker
    result = []
    try:
        huobi = ccxt.huobi({
            'apiKey': 'apiKey',
            'secret': 'secret',
            'options': {'adjustForTimeDifference': True}
        })

        totalBalance = huobi.fetch_balance()["free"]
        # totalBalance= [x+"/CNY" for x in totalBalance if x!="CNY"]
        totalExBalance = sum(list(totalBalance.values()))
        checkSymbols = huobi.symbols
        for s in symbols:
            if s in checkSymbols:
                try:
                    dataSymbols = huobi.fetch_ticker(s)
                    coinBalance = totalBalance[s.split("/")[0]]
                    result.append(["huobi", s, coinBalance, dataSymbols["ask"], dataSymbols["bid"], dataSymbols["baseVolume"]])
                except:
                    print("Huobi couldn`t get "+ s)
                    continue
    except Exception as e:
        print(str(e)[:150])
    return (result)


def yobitAgg(symbols):
    result = []
    try:
        yobit = ccxt.yobit({
            'apiKey': 'apiKey',
            'secret': 'secret',
            'options': {'adjustForTimeDifference': True}
        })
        totalBalance = yobit.fetch_balance()["free"]
        exchangeSymbols= yobit.symbols
        checkSymbols = list(np.intersect1d(exchangeSymbols, symbols))
        allData = yobit.fetch_tickers(checkSymbols)
        ethPrice = yobit.fetch_ticker("ETH/USD")["last"]
        btcPrice = yobit.fetch_ticker("BTC/USD")["last"]
        for s in checkSymbols:
            try:
                quote = s.split("/")[-1]
                dataSymbols = allData[s]
                coinBalance = totalBalance.get(s.split("/")[0], 0)
                volume = int(float(dataSymbols["baseVolume"]))
                ask = dataSymbols["ask"]
                bid = dataSymbols["bid"]
                last = float(dataSymbols["last"])
                if quote == "BTC":
                    volume = int(volume * btcPrice * last)
                elif quote == "ETH":
                    volume = int(volume * ethPrice * last)
                else:
                    volume = int(volume * dataSymbols["last"])
                volume= volume/ethPrice
                result.append(["yobit", s, coinBalance, ask, bid, volume])
            except:
                print("Yobit couldn`t get " + s)
                continue
    except Exception as e:
        print(str(e)[:150])
    return (result)


def bitfinexAgg(symbols):
    result = []
    try:
        bitfinex = ccxt.bitfinex({
            'apiKey': 'apiKey',
            'secret': 'secret',
            'options': {'adjustForTimeDifference': True}
        })
        totalBalance = bitfinex.fetch_balance()["free"]
        exchangeSymbols= bitfinex.symbols
        checkSymbols = list(np.intersect1d(exchangeSymbols, symbols))
        allData = bitfinex.fetch_tickers(checkSymbols)
        ethPrice = bitfinex.fetch_ticker("ETH/USD")["last"]
        btcPrice = bitfinex.fetch_ticker("BTC/USD")["last"]
        for s in checkSymbols:
            try:
                quote = s.split("/")[-1]
                dataSymbols = allData[s]
                coinBalance = totalBalance.get(s.split("/")[0], 0)
                volume = int(float(dataSymbols["baseVolume"]))
                ask = dataSymbols["ask"]
                bid = dataSymbols["bid"]
                last = float(dataSymbols["last"])
                if quote == "BTC":
                    volume = int(volume * btcPrice * last)
                elif quote == "ETH":
                    volume = int(volume * ethPrice * last)
                else:
                    volume = int(volume * dataSymbols["last"])
                volume= volume/ethPrice
                result.append(["bitfinex", s, coinBalance, ask, bid, volume])
            except:
                print("Bitfinex couldn`t get " + s)
                continue
    except Exception as e:
        print(str(e)[:150])
    return (result)



def bittrexAgg(symbols):
    result = []
    try:
        bittrex = ccxt.bittrex({
            'apiKey': 'apiKey',
            'secret': 'secret',
            'options': {'adjustForTimeDifference': True}
        })
        totalBalance = bittrex.fetch_balance()["free"]
        exchangeSymbols= bittrex.symbols
        checkSymbols = list(np.intersect1d(exchangeSymbols, symbols))
        allData = bittrex.fetch_tickers(checkSymbols)
        ethPrice = bittrex.fetch_ticker("ETH/USDT")["last"]
        btcPrice = bittrex.fetch_ticker("BTC/USDT")["last"]
        for s in checkSymbols:
            try:
                quote = s.split("/")[-1]
                dataSymbols = allData[s]
                coinBalance = totalBalance.get(s.split("/")[0], 0)
                volume = int(float(dataSymbols["baseVolume"]))
                ask = dataSymbols["ask"]
                bid = dataSymbols["bid"]
                last = float(dataSymbols["last"])
                if quote == "BTC":
                    volume = int(volume * btcPrice * last)
                elif quote == "ETH":
                    volume = int(volume * ethPrice * last)
                else:
                    volume = int(volume * dataSymbols["last"])
                volume= volume/ethPrice
                result.append(["bittrex", s, coinBalance, ask, bid, volume])
            except:
                print("Bittrex couldn`t get " + s)
                continue
    except Exception as e:
        print(str(e)[:150])
    return (result)



def poloniexAgg(symbols):
    result = []
    try:
        poloniex = ccxt.poloniex({
            'apiKey': 'apiKey',
            'secret': 'secret',
            'options': {'adjustForTimeDifference': True}
        })
        allData= poloniex.load_markets()
        totalBalance = poloniex.fetch_balance()["free"]
        ethPrice = allData["ETH/USDT"]["info"]["last"]
        btcPrice = allData["BTC/USDT"]["info"]["last"]
        checkSymbols = poloniex.symbols
        for s in symbols:
            if s in checkSymbols:
                try:
                    quote = s.split("/")[-1]
                    #dataSymbols = poloniex.fetch_ticker(s)
                    dataSymbols= allData[s]
                    coinBalance = totalBalance.get(s.split("/")[0], 0)
                    volume = int(float(dataSymbols["info"]["baseVolume"]))
                    ask = dataSymbols["info"]["lowestAsk"]
                    bid = dataSymbols["info"]["highestBid"]
                    last= float(dataSymbols["info"]["last"])
                    if quote=="BTC":
                        volume = int(volume*btcPrice*last)
                    elif quote=="ETH":
                        volume = int(volume*ethPrice*last)
                    else:
                        volume = int(volume*dataSymbols["last"])
                    volume = volume / ethPrice
                    result.append(["poloniex", s, coinBalance, ask, bid, volume])
                except:
                    print("Poloniex couldn`t get "+ s)
                    continue
    except Exception as e:
        print(str(e)[:150])
    return (result)


def gateAgg(symbols):
    result = []
    try:
        gate = ccxt.gateio({
            'apiKey': 'apiKey',
            'secret': 'secret',
            'options': {'adjustForTimeDifference': True}
        })
        totalBalance = gate.fetch_balance()["free"]
        exchangeSymbols= gate.symbols
        checkSymbols = list(np.intersect1d(exchangeSymbols, symbols))
        allData = gate.fetch_tickers(checkSymbols)
        ethPrice = gate.fetch_ticker("ETH/USDT")["last"]
        btcPrice = gate.fetch_ticker("BTC/USDT")["last"]
        for s in checkSymbols:
            try:
                quote = s.split("/")[-1]
                dataSymbols = allData[s]
                coinBalance = totalBalance.get(s.split("/")[0], 0)
                volume = int(float(dataSymbols["baseVolume"]))
                ask = dataSymbols["ask"]
                bid = dataSymbols["bid"]
                last = float(dataSymbols["last"])
                if quote == "BTC":
                    volume = int(volume * btcPrice * last)
                elif quote == "ETH":
                    volume = int(volume * ethPrice * last)
                else:
                    volume = int(volume * dataSymbols["last"])
                volume= volume/ethPrice
                result.append(["gate", s, coinBalance, ask, bid, volume])
            except:
                print("Gate couldn`t get " + s)
                continue
    except Exception as e:
        print(str(e)[:150])
    return(result)


def idexAgg(symbols):
    result = []
    try:
        idex = idexExchange.idex(address="address", \
                                  private_key="privatKey")

        totalBalance = idex.get_my_balances()
        allData= idex.get_tickers()
        checkSymbols = list(allData.keys())
        symbolsUp= [x.split("/")[-1]+"_"+x.split("/")[0] for x in symbols]
        for i,s in enumerate(symbolsUp):
            if s in checkSymbols:
                try:
                    symb= symbols[i]
                    quote = symb.split("/")[-1]
                    dataSymbols= allData[s]
                    coinBalance = totalBalance.get(s.split("/")[0], 0)
                    volume = int(float(dataSymbols["baseVolume"]))
                    ask = float(dataSymbols["lowestAsk"])
                    bid = float(dataSymbols["highestBid"])
                    result.append(["idex", symb, coinBalance, ask, bid, volume])
                except:
                    print("Gate couldn`t get "+ s)
                    continue
    except Exception as e:
        print(str(e)[:150])
    return(result)



def calcSummary(data, volumeLim, deltaLim):
    roundn= 4
    summary = []
    for i in range(0, len(data)):
        updateTime = str(datetime.datetime.now()).split(" ")[-1][:8]
        ex = data[i][0]
        symb = data[i][1]
        for j in range(i, len(data)):
            ex2 = data[j][0]
            symb2 = data[j][1]
            if (ex != ex2) & (symb == symb2):
                balance1 = data[i][2]
                balance2 = data[j][2]
                ask1 = data[i][3]
                bid1 = data[i][4]
                ask2 = data[j][3]
                bid2 = data[j][4]
                v1 = int(data[i][5])
                v2 = int(data[j][5])
                if (v1 > volumeLim) & (v2 > volumeLim):
                    if (balance1 >= 0) & (balance2 >= 0):
                        deltaBid1= 100*(bid1-bid2)/bid1
                        deltaAsk1= 100*(ask1-ask2)/ask1
                        deltaBid2 = 100*(bid2 - bid1)/bid2
                        deltaAsk2 = 100*(ask2 - ask1)/ask2
                        if (deltaBid1>deltaLim) & (deltaAsk1>deltaLim):
                            temp = [updateTime, symb, str(data[i][0]),str(data[j][0]), round(balance1, roundn), round(balance2, roundn), \
                                    round(bid1, roundn), round(ask1, roundn), round(bid2, roundn), \
                                    round(ask2, roundn), v1, v2, round(min(deltaBid1, deltaAsk1), roundn)]
                            summary.append(temp)
                        if (deltaBid2>deltaLim) & (deltaAsk2>deltaLim):
                            temp = [updateTime, symb, str(data[j][0]), str(data[i][0]), round(balance2, roundn), round(balance1, roundn), \
                                    round(bid2, roundn), round(ask2, roundn), round(bid1, roundn), \
                                    round(ask1, roundn), v2, v1, round(min(deltaBid2, deltaAsk2), roundn)]
                            summary.append(temp)

    summaryTable = pd.DataFrame(summary, columns=["UpdateTime", "Symbol", "Exchange1", "Exchange2", \
                                                  "BalanceEx1", "BalanceEx2", "Bid1", "Ask1", "Bid2", "Ask2", "V1", "V2", "Delta"])
    summaryTable= summaryTable.sort_values("Delta", ascending=False).reset_index(drop=True)
    return (summaryTable)

