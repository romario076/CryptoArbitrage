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
            'apiKey': '1c08286612966c0cfde89951f8e25cfb',
            'secret': 'cf49923474a1eeb0cac3714a18836b0c',
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
            'apiKey': 'e661747e-5ffd-4ae4-9c73-81b02c479d46',
            'secret': 'EBCAE7AF874A99DDC51A26173CF85C0B',
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
            'apiKey': 'A9MN1E0R-RWUO52G6-VJQXZM1C-AZ4YR2A7-C67Z51UC',
            'secret': '0e7fc8851e071ac7ef4888a787cf945fff0c2474738ab1bef085e07d9591ddb9',
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
            'apiKey': 'nnMk0QyOMFfTqXSPN6Qorsz+6iqMLo7JwVdcoc2DI+vU+M+QKirTCV4j',
            'secret': 'wD3/BsdlgLUMh3E+zNSuFztMdcld86pVlTlzQgl4brcUzAWqoIoLe5NSxLpw1IfQGAgne5y7txCIs8pxQ84JWA==',
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
            'apiKey': 'HkUsqNGUm2k1sgEAWqKCMbb6r8eVjE655zwcGq6ET1vceaZysE7kvgOH1UKuhU1g',
            'secret': 'HQSr60HtlonWSFI1fszrAFjULmiMsd4ZPsq86CIEi0tE6RB0l3T9moEpSjPTKHP8',
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
            'apiKey': '5a8365a918da3477dcaea8f3',
            'secret': 'e53b33c4-dfe1-4a79-b5c4-70d2e78f6aea',
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
            'apiKey': '6e84c88a-727306e0-37633647-5ce7e',
            'secret': 'bd53ecee-1a6147e2-eefa218d-8bcbc',
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
            'apiKey': 'E1912175FA2891BF64D3FC605FDA6C8C',
            'secret': '399955509224b7b98ac5a9d2af115041',
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
            'apiKey': 'd8IztR3aHSOX3m7IpfxHNVz9sqtpZK1r0KOoOSTVIom',
            'secret': 'RfZVQIxamQwjw2bhGaWkMr3b3NLuOsZni3pXoYKY3Fm',
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
            'apiKey': '5b64b08e52554a8898a8130f44c1dd97',
            'secret': 'cec389794dac47ea8a78002799b55db4',
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
            'apiKey': 'HWJ8USAK-LIUIM3IN-WWUYY7WV-PQUB77GF',
            'secret': '62f50ccb0480dcf340305c2a46cb392f6ab46aaae4ce6bec92791cca5b20e014df98464cfe2e1d4bdc4955924780c0fe7af1a89696ecb6136aecb1243a11905f',
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
            'apiKey': '15408F71-19A2-4362-BDD6-C7A7C523D15A',
            'secret': '9f3fb71df4501528c068b79d795021e7134ff5c463148d56796b3ac7ee79cf22',
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
        idex = idexExchange.idex(address="984639855bf081116e0db26f5843a34384e58e7c", \
                                  private_key="0x8e9c7e96ad15be51ce4d28ddedc5fa2566528bbd2eb5f8acac58a8c2b7757b83")

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

