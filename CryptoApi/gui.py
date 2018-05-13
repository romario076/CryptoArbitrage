
try:
    from Tkinter import *
    import tkMessageBox  as messagebox
except ImportError:
    from tkinter import *
    from tkinter import messagebox

try:
    import ttk
    py3 = 0
except ImportError:
    import tkinter.ttk as ttk
    py3 = 1
import time
from ExConnTest import *
from AutoScroll import *
import threading
import sys

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    top = Gui (root)
    root.mainloop()

w = None
def create_New_Toplevel_1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    top = Gui (w)
    return (w, top)

def destroy_New_Toplevel_1():
    global w
    w.destroy()
    w = None


def clear_all():
    gl = globals().copy()
    for var in gl:
        if var[0] == '_': continue
        if 'func' in str(globals()[var]): continue
        if 'module' in str(globals()[var]): continue

        del globals()[var]


class Gui:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#d9d9d9' # X11 color: 'gray85'
        self.root = root
        self.style = ttk.Style()
        self.style.theme_use("vista")
        #self.root.iconbitmap('cut.ico')
        #self.photo = PhotoImage(file='cut.ico')
        #if sys.platform == "win32":
        #    self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=[('selected', _compcolor), ('active',_ana2color)])
        self.stopRunning = False

        top.geometry("1180x585+30+15")
        top.title("Arbitrage")
        top.configure(background="#d9d9d9")

        self.root.iconbitmap('ico.ico')
        #self.root.wm_iconphoto(True, 'ico.ico')

        self.TFrame1 = ttk.Frame(top)
        self.TFrame1.place(relx=0.12, rely=0.03, relheight=0.93, relwidth=0.785)
        self.TFrame1.configure(relief=RAISED)
        self.TFrame1.configure(borderwidth="2")
        self.TFrame1.configure(relief=RAISED)
        self.TFrame1.configure(width=875)

        self.progress = ttk.Progressbar(top, orient="horizontal",  length=200, mode="determinate")
        self.progress.place(relx=0.01, rely=0.97, relheight=0.03, relwidth=0.3)
        self.status= Label(top, text= "Prepearing...", bd=1, relief=SUNKEN, anchor=W)
        self.status.place(relx=0.31, rely=0.97, relheight=0.03, relwidth=0.679)

        self.style.configure('Treeview.Heading',  font="TkDefaultFont")
        self.Scrolledtreeview1 = ScrolledTreeView(self.TFrame1)
        self.Scrolledtreeview1.place(relx=0.009, rely=0.02, relheight=0.95, relwidth=0.98)
        self.Scrolledtreeview1.configure(columns="Col1 Col2 Col3 Col4 Col5 Col6 Col7 Col8 Col9 Col10 Col11 Col12 Col13")
        self.Scrolledtreeview1.heading("#0",text="Id")
        self.Scrolledtreeview1.heading("#0",anchor="center")
        self.Scrolledtreeview1.column("#0",width="35", stretch=YES)
        self.Scrolledtreeview1.column("#0",minwidth="20")
        self.Scrolledtreeview1.column("#0",stretch="1")
        self.Scrolledtreeview1.column("#0",anchor="w")
        self.Scrolledtreeview1.heading("Col1",text="Update") #Update
        self.Scrolledtreeview1.heading("Col1",anchor="center")
        self.Scrolledtreeview1.column("Col1",width="50", stretch=YES)
        self.Scrolledtreeview1.column("Col1",minwidth="20")
        self.Scrolledtreeview1.column("Col1",stretch="1")
        self.Scrolledtreeview1.column("Col1",anchor="w")
        self.Scrolledtreeview1.heading("Col2",text="Symbol") #Symbol
        self.Scrolledtreeview1.heading("Col2",anchor="center")
        self.Scrolledtreeview1.column("Col2",width="65", stretch=YES)
        self.Scrolledtreeview1.column("Col2",minwidth="20")
        self.Scrolledtreeview1.column("Col2",stretch="1")
        self.Scrolledtreeview1.column("Col2",anchor="w")
        self.Scrolledtreeview1.heading("Col3",text="Ex1") # Ex1
        self.Scrolledtreeview1.heading("Col3",anchor="center")
        self.Scrolledtreeview1.column("Col3",width="50", stretch=YES)
        self.Scrolledtreeview1.column("Col3",minwidth="20")
        self.Scrolledtreeview1.column("Col3",stretch="1")
        self.Scrolledtreeview1.column("Col3",anchor="w")
        self.Scrolledtreeview1.heading("Col4",text="Ex2") #Ex2
        self.Scrolledtreeview1.heading("Col4",anchor="center")
        self.Scrolledtreeview1.column("Col4",width="50", stretch=YES)
        self.Scrolledtreeview1.column("Col4",minwidth="20")
        self.Scrolledtreeview1.column("Col4",stretch="1")
        self.Scrolledtreeview1.column("Col4",anchor="w")
        self.Scrolledtreeview1.heading("Col5",text="CoinBalEx1") #Balance1
        self.Scrolledtreeview1.heading("Col5",anchor="center")
        self.Scrolledtreeview1.column("Col5",width="70", stretch=YES)
        self.Scrolledtreeview1.column("Col5",minwidth="20")
        self.Scrolledtreeview1.column("Col5",stretch="1")
        self.Scrolledtreeview1.column("Col5",anchor="w")
        self.Scrolledtreeview1.heading("Col6",text="CoinBalEx2") #Balance2
        self.Scrolledtreeview1.heading("Col6",anchor="center")
        self.Scrolledtreeview1.column("Col6",width="70", stretch=YES)
        self.Scrolledtreeview1.column("Col6",minwidth="20")
        self.Scrolledtreeview1.column("Col6",stretch="1")
        self.Scrolledtreeview1.column("Col6",anchor="w")
        self.Scrolledtreeview1.heading("Col7",text="Bid1") #Bid1
        self.Scrolledtreeview1.heading("Col7",anchor="center")
        self.Scrolledtreeview1.column("Col7",width="65", stretch=YES)
        self.Scrolledtreeview1.column("Col7",minwidth="20")
        self.Scrolledtreeview1.column("Col7",stretch="1")
        self.Scrolledtreeview1.column("Col7",anchor="w")
        self.Scrolledtreeview1.heading("Col8",text="Ask1") #Ask1
        self.Scrolledtreeview1.heading("Col8",anchor="center")
        self.Scrolledtreeview1.column("Col8",width="65", stretch=YES)
        self.Scrolledtreeview1.column("Col8",minwidth="20")
        self.Scrolledtreeview1.column("Col8",stretch="1")
        self.Scrolledtreeview1.column("Col8",anchor="w")
        self.Scrolledtreeview1.heading("Col9",text="Bid2") #Bid2
        self.Scrolledtreeview1.heading("Col9",anchor="center")
        self.Scrolledtreeview1.column("Col9",width="65", stretch=YES)
        self.Scrolledtreeview1.column("Col9",minwidth="20")
        self.Scrolledtreeview1.column("Col9",stretch="1")
        self.Scrolledtreeview1.column("Col9",anchor="w")
        self.Scrolledtreeview1.heading("Col10",text="Ask2") #Ask2
        self.Scrolledtreeview1.heading("Col10",anchor="center")
        self.Scrolledtreeview1.column("Col10",width="65", stretch=YES)
        self.Scrolledtreeview1.column("Col10",minwidth="20")
        self.Scrolledtreeview1.column("Col10",stretch="1")
        self.Scrolledtreeview1.column("Col10",anchor="w")
        self.Scrolledtreeview1.heading("Col11",text="V1") #V1
        self.Scrolledtreeview1.heading("Col11",anchor="center")
        self.Scrolledtreeview1.column("Col11",width="60", stretch=YES)
        self.Scrolledtreeview1.column("Col11",minwidth="20")
        self.Scrolledtreeview1.column("Col11",stretch="1")
        self.Scrolledtreeview1.column("Col12",anchor="w")
        self.Scrolledtreeview1.heading("Col12", text="V2")   #V2
        self.Scrolledtreeview1.heading("Col12",anchor="center")
        self.Scrolledtreeview1.column("Col12",width="60", stretch=YES)
        self.Scrolledtreeview1.column("Col12",minwidth="20")
        self.Scrolledtreeview1.column("Col12",stretch="1")
        self.Scrolledtreeview1.column("Col12",anchor="w")
        self.Scrolledtreeview1.heading("Col13",text="Delta") #Delta
        self.Scrolledtreeview1.heading("Col13",anchor="center")
        self.Scrolledtreeview1.column("Col13",width="50", stretch=YES)
        self.Scrolledtreeview1.column("Col13",minwidth="20")
        self.Scrolledtreeview1.column("Col13",stretch="1")
        self.Scrolledtreeview1.column("Col13",anchor="w")

        self.TFrame2 = ttk.Frame(top)
        self.TFrame2.place(relx=0.01, rely=0.03, relheight=0.93, relwidth=0.1)
        self.TFrame2.configure(relief=RAISED)
        self.TFrame2.configure(borderwidth="2")
        self.TFrame2.configure(relief=RAISED)
        self.TFrame2.configure(width=105)

        self.TFrame3 = ttk.Frame(top)
        self.TFrame3.place(relx=0.91, rely=0.03, relheight=0.93, relwidth=0.08)
        self.TFrame3.configure(relief=RAISED)
        self.TFrame3.configure(borderwidth="2")
        self.TFrame3.configure(relief=RAISED)
        self.TFrame3.configure(width=105)

        self.hitbtcCheckVar = IntVar(value=1)
        self.hitbtcCheck= Checkbutton(self.TFrame3, text="Hitbtc", variable=self.hitbtcCheckVar, bg=_bgcolor, anchor=W)
        self.hitbtcCheck.place(relx=0.07, rely=0.07, height=10, width=70)
        self.okexCheckVar = IntVar(value=1)
        self.okexCheck= Checkbutton(self.TFrame3, text="Okex",  variable=self.okexCheckVar, bg=_bgcolor, anchor=W)
        self.okexCheck.place(relx=0.07, rely=0.12, height=10, width=70)
        self.liquiCheckVar = IntVar(value=1)
        self.liquiCheck= Checkbutton(self.TFrame3, text="Liqui",  variable=self.liquiCheckVar, bg=_bgcolor, anchor=W)
        self.liquiCheck.place(relx=0.07, rely=0.17, height=10, width=70)
        self.krakenCheckVar = IntVar(value=1)
        self.krakenCheck= Checkbutton(self.TFrame3, text="Kraken",  variable=self.krakenCheckVar, bg=_bgcolor, anchor=W)
        self.krakenCheck.place(relx=0.07, rely=0.22, height=10, width=70)
        self.binanceCheckVar = IntVar(value=1)
        self.binanceCheck= Checkbutton(self.TFrame3, text="Binance",  variable=self.binanceCheckVar, bg=_bgcolor, anchor=W)
        self.binanceCheck.place(relx=0.07, rely=0.27, height=10, width=70)
        self.kucoinCheckVar = IntVar(value=1)
        self.kucoinCheck= Checkbutton(self.TFrame3, text="Kucoin",  variable=self.kucoinCheckVar, bg=_bgcolor, anchor=W)
        self.kucoinCheck.place(relx=0.07, rely=0.32, height=10, width=70)
        self.yobitCheckVar = IntVar(value=1)
        self.yobitCheck= Checkbutton(self.TFrame3, text="Yobit",  variable=self.yobitCheckVar, bg=_bgcolor, anchor=W)
        self.yobitCheck.place(relx=0.07, rely=0.37, height=10, width=70)
        self.bitfinexCheckVar = IntVar(value=1)
        self.bitfinexCheck= Checkbutton(self.TFrame3, text="Bitfinex",  variable=self.bitfinexCheckVar , bg=_bgcolor, anchor=W)
        self.bitfinexCheck.place(relx=0.07, rely=0.42, height=10, width=70)
        self.bittrrexCheckVar = IntVar(value=1)
        self.bittrrexCheck= Checkbutton(self.TFrame3, text="Bittrex",  variable=self.bitfinexCheckVar , bg=_bgcolor, anchor=W)
        self.bittrrexCheck.place(relx=0.07, rely=0.47, height=10, width=70)
        self.poloniexCheckVar = IntVar(value=0)
        self.poloniexCheck= Checkbutton(self.TFrame3, text="Poloniex",  variable=self.poloniexCheckVar , bg=_bgcolor, anchor=W)
        self.poloniexCheck.place(relx=0.07, rely=0.52, height=10, width=70)
        self.gateCheckVar = IntVar(value=1)
        self.gateCheck= Checkbutton(self.TFrame3, text="Gate",  variable=self.gateCheckVar , bg=_bgcolor, anchor=W)
        self.gateCheck.place(relx=0.07, rely=0.57, height=10, width=70)
        self.idexCheckVar = IntVar(value=1)
        self.idexCheck= Checkbutton(self.TFrame3, text="Idex",  variable=self.idexCheckVar , bg=_bgcolor, anchor=W)
        self.idexCheck.place(relx=0.07, rely=0.62, height=10, width=70)

        self.Button1 = Button(self.TFrame2, command=self.main)
        self.Button1.place(relx=0.19, rely=0.07, height=34, width=67)
        self.Button1.configure(activebackground="#d9d9d9")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Go''')
        self.Button1.configure(width=67)

        self.Button2 = Button(self.TFrame2, command= self.CloseWindow)
        self.Button2.place(relx=0.19, rely=0.88, height=34, width=67)
        self.Button2.configure(activebackground="#d9d9d9")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''Exit''')

        self.Button3 = Button(self.TFrame2, command= self.stopRun)
        self.Button3.place(relx=0.19, rely=0.19, height=34, width=67)
        self.Button3.configure(activebackground="#d9d9d9")
        self.Button3.configure(activeforeground="#000000")
        self.Button3.configure(background="#d9d9d9")
        self.Button3.configure(disabledforeground="#a3a3a3")
        self.Button3.configure(foreground="#000000")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(pady="0")
        self.Button3.configure(text='''Stop''')

        self.Spinbox1 = Spinbox(self.TFrame2, from_=1.0, to=100.0)
        self.Spinbox1.place(relx=0.19, rely=0.35, relheight=0.03, relwidth=0.71)
        self.Spinbox1.configure(activebackground="#f9f9f9")
        self.Spinbox1.configure(background="white")
        self.Spinbox1.configure(buttonbackground="#d9d9d9")
        self.Spinbox1.configure(disabledforeground="#a3a3a3")
        self.Spinbox1.configure(foreground="black")
        self.Spinbox1.configure(from_="5.0")
        self.Spinbox1.configure(highlightbackground="black")
        self.Spinbox1.configure(highlightcolor="black")
        self.Spinbox1.configure(insertbackground="black")
        self.Spinbox1.configure(selectbackground="#c4c4c4")
        self.Spinbox1.configure(selectforeground="black")
        self.Spinbox1.configure(to="60.0")
        self.Spinbox1.configure(width=75)

        self.TLabel1 = Label(self.TFrame2, justify=LEFT, anchor=W)
        self.TLabel1.place(relx=0.1, rely=0.29, height=29, width=86)
        self.TLabel1.configure(background="#d9d9d9")
        self.TLabel1.configure(foreground="#000000")
        self.TLabel1.configure(relief=FLAT)
        self.TLabel1.configure(text='''UpdateSec:''')
        self.TLabel1.configure(width=86)

        self.TLabel2 = Label(self.TFrame2, justify=LEFT, anchor=W)
        self.TLabel2.place(relx=0.1, rely=0.41, height=29, width=70)
        self.TLabel2.configure(background="#d9d9d9")
        self.TLabel2.configure(foreground="#000000")
        self.TLabel2.configure(relief=FLAT)
        self.TLabel2.configure(text='''NextUpdate:''')

        self.Text1= Label(self.TFrame2, text="", relief=SUNKEN)
        self.Text1.place(relx=0.19, rely=0.46, relheight=0.04, relwidth=0.7)
        self.Text1.configure(background="white")
        self.Text1.configure(text='''00:00:00''')

        self.TLabel3 = Label(self.TFrame2, justify=LEFT, anchor=W)
        self.TLabel3.place(relx=0.1, rely=0.51, height=29, width=70)
        self.TLabel3.configure(background="#d9d9d9")
        self.TLabel3.configure(foreground="#000000")
        self.TLabel3.configure(relief=FLAT)
        self.TLabel3.configure(text='''VolumeLimit:''')

        self.volumeLimit = Entry(self.TFrame2, text="", relief=SUNKEN)
        self.volumeLimit.place(relx=0.19, rely=0.56, relheight=0.04, relwidth=0.7)
        self.volumeLimit.configure(background="white")
        self.volumeLimit.insert(END, str(100))

        self.TLabel4 = Label(self.TFrame2, justify=LEFT, anchor=W)
        self.TLabel4.place(relx=0.1, rely=0.61, height=29, width=70)
        self.TLabel4.configure(background="#d9d9d9")
        self.TLabel4.configure(foreground="#000000")
        self.TLabel4.configure(relief=FLAT)
        self.TLabel4.configure(text='''DeltaLimit:''')

        self.deltaLimit = Entry(self.TFrame2, text="", relief=SUNKEN)
        self.deltaLimit.place(relx=0.19, rely=0.66, relheight=0.04, relwidth=0.7)
        self.deltaLimit.configure(background="white")
        self.deltaLimit.insert(END, str(0.5))



    def stopRun(self):
        self.root.update()
        self.stopRunning= True
        print("Stop running........")

    def CloseWindow(self) :
        self.root.destroy()

    def insertOpenData(self, table):
        self.Scrolledtreeview1.delete(*self.Scrolledtreeview1.get_children())
        for i,row in table.iterrows():
            self.Scrolledtreeview1.insert('', 'end', text=str(i),\
                    values=( str(row[0]).split(" ")[-1],  str(row[1]), str(row[2]), str(row[3]), row[4], row[5], \
                             row[6], row[7], row[8], row[9], row[10], row[11], row[12]))

    def updateTimer(self):
        t= int(self.Spinbox1.get())
        for i in range(0, t):
            time.sleep(1)
            self.Text1["text"]= str("00:00:0" + str(t - i))
            self.root.update()
        self.Text1["text"] = str("00:00:00")

    def updateTable(self):
        summaryTable = calcSummary(data=self.data, volumeLim=self.volumeLim, deltaLim=self.deltaLim)
        self.insertOpenData(table=summaryTable)

    def loadSymbols(self):
        self.symbols= getSymbols()
        print("Loaded " + str(len(self.symbols))+ " symbols")
        print("Symbols: " + str(self.symbols))

    def loop(self):
        print ("Start running........")
        while not self.stopRunning:
            hitbitcData=okexData=liquiData=krakenData=binanceData= \
                kucoinData=yobitData=bitfinexData=bittrexData=gateData=poloniexData = idexData=[]
            try:
                self.progress["value"] = 10
                if self.hitbtcCheckVar.get():
                    self.status["text"] = "Requesting data from Hitbtc..."
                    self.root.update()
                    hitbitcData = hitbtcAgg(symbols=self.symbols)
                    self.progress["value"] = 20
                if self.okexCheckVar.get():
                    self.status["text"] = "Requesting data from Okex..."
                    self.root.update()
                    okexData= okexAgg(symbols=self.symbols)
                    self.progress["value"] = 25
                if self.liquiCheckVar.get():
                    self.status["text"] = "Requesting data from Liqui..."
                    self.root.update()
                    liquiData = liquiAgg(symbols=self.symbols)
                    self.progress["value"] = 30
                if self.krakenCheckVar.get():
                    self.status["text"] = "Requesting data from Kraken..."
                    self.root.update()
                    krakenData= krakenAgg(symbols=self.symbols)
                    self.progress["value"] = 35
                if self.binanceCheckVar.get():
                    self.status["text"] = "Requesting data from Binance..."
                    self.root.update()
                    binanceData = binanceAgg(symbols=self.symbols)
                    self.progress["value"] = 40
                if self.kucoinCheckVar.get():
                    self.status["text"] = "Requesting data from Kucoin..."
                    self.root.update()
                    kucoinData= kucoinAgg(symbols=self.symbols)
                    self.progress["value"] = 50
                if self.yobitCheckVar.get():
                    self.status["text"] = "Requesting data from Yobit..."
                    self.root.update()
                    yobitData= yobitAgg(symbols=self.symbols)
                    self.progress["value"] = 55
                if self.bitfinexCheckVar.get():
                    self.status["text"] = "Requesting data from Bitfinex..."
                    self.root.update()
                    bitfinexData= bitfinexAgg(symbols=self.symbols)
                    self.progress["value"] = 60
                if self.bittrrexCheckVar.get():
                    self.status["text"] = "Requesting data from Bittrrex..."
                    self.root.update()
                    bittrexData= bittrexAgg(symbols=self.symbols)
                    self.progress["value"] = 65
                if self.gateCheckVar.get():
                    self.status["text"] = "Requesting data from Gate..."
                    self.root.update()
                    gateData= gateAgg(symbols=self.symbols)
                    self.progress["value"] = 70
                if self.poloniexCheckVar.get():
                    self.status["text"] = "Requesting data from Poloniex..."
                    self.root.update()
                    poloniexData = poloniexAgg(symbols=self.symbols)
                    self.progress["value"] = 75
                if self.idexCheckVar.get():
                    self.status["text"] = "Requesting data from Idex..."
                    self.root.update()
                    idexData = idexAgg(symbols=self.symbols)
                    self.progress["value"] = 80

                if self.stopRunning == False:
                    self.data = hitbitcData + okexData + liquiData + krakenData + \
                                binanceData + kucoinData + yobitData + bitfinexData + \
                                bittrexData + gateData + poloniexData + idexData
                    self.progress["value"] = 100
                    self.status["text"] = "Done!"
                    self.updateTable()
                    self.updateTimer()
            except Exception as e:
                print(e)
                break

    def checkInputs(self):
        error= False
        try:
            self.volumeLim= int(self.volumeLimit.get())
        except:
            error= True
            messagebox.showinfo("Warning", "Specified wrong volumeLim input!")
        try:
            self.deltaLim = float(self.deltaLimit.get())
        except:
            error= True
            messagebox.showinfo("Warning", "Specified wrong deltaLim input!")
        return (error)

    def main(self):
        error= self.checkInputs()
        if not error:
            self.thread= []
            try:
                self.stopRunning = False
                self.loadSymbols()
                self.thread = threading.Thread(target=self.loop)
                self.thread.daemon = True
                self.thread.start()
            except Exception as e:
                print(e)




if __name__ == '__main__':
    vp_start_gui()

