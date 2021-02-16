# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 17:51:54 2021

@author: DEMİR
"""

import sys 
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from bs4 import BeautifulSoup
import threading
from selenium import webdriver
import time

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument("disable-gpu")

browser = webdriver.Chrome() #options=options


sayi = 5


class mainPage(QWidget):
    
    def __init__(self , parent = None):
        super(mainPage , self).__init__(parent)
        
        self.setWindowTitle("Coin Exchange")
        self.setFixedSize(600,400)
        
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        tabs = QTabWidget()
        tabs.addTab(self.scrapingUI(), "Scraping")
        tabs.addTab(self.addCoinUI(), "Add new Coin")
        layout.addWidget(tabs)
        
    def addNewCoin(self): # maximum 3 tane ekleme yapılabilsin
        global sayi
        coinName = self.coinName.text()
        coinUrl  = self.coinUrl.text()
        
        if coinName == "" or coinUrl == "":
            QMessageBox.about(self,"ALERT","Boş bırakılamaz")
        else:
            if sayi == 5:
                self.newCoin = QCheckBox(coinName); self.newCoin.setFont(QFont("Helvetica",12))
                self.newCoin.toggled.connect(self.newCoinOne)
                self.grid.addWidget(self.newCoin , sayi , 0)
                self.newCoinUrl = self.coinUrl.text()
                sayi += 1
            elif sayi == 6:
                self.newCoin1 = QCheckBox(coinName); self.newCoin1.setFont(QFont("Helvetica",12))
                self.newCoin1.toggled.connect(self.newCoinOne1)
                self.grid.addWidget(self.newCoin1 , sayi , 0)
                self.newCoinUrl1 = self.coinUrl.text()
                sayi += 1
            elif sayi == 7: 
                self.newCoin2 = QCheckBox(coinName); self.newCoin2.setFont(QFont("Helvetica",12))
                self.newCoin2.toggled.connect(self.newCoinOne2)
                self.grid.addWidget(self.newCoin2 , sayi , 0)
                self.newCoinUrl2 = self.coinUrl.text()
                sayi += 1
            
            else:
                QMessageBox.about(self,"Are u VIP ?","Sadece 3 tane coin ekleyebilirsin !")
            
   
        
    def scrapingUI(self):
        
        scrapingUI = QWidget()
        
        self.grid = QGridLayout()
        
        self.btc = QCheckBox("Bitcoin  BTC"); self.btc.setFont(QFont("Helvetica",12))
        self.btc.toggled.connect(self.btcCheck)
        self.btcurl = "https://coinmarketcap.com/tr/currencies/bitcoin/"
        
        self.ltc = QCheckBox("Litecoin LTC"); self.ltc.setFont(QFont("Helvetica",12))
        self.ltc.toggled.connect(self.ltcCheck)
        self.ltcurl = "https://coinmarketcap.com/tr/currencies/litecoin/"
        
        trx = QCheckBox("Tron     TRX"); trx.setFont(QFont("Helvetica",12))
        
        
        eos = QCheckBox("Eos      EOS"); eos.setFont(QFont("Helvetica",12))
        xrp = QCheckBox("Ripple   XRP"); xrp.setFont(QFont("Helvetica",12))
        
        self.lbl = QLabel("   ");  self.lbl.setFont(QFont( "Helvetica",12))
        self.lbl1 = QLabel("   "); self.lbl1.setFont(QFont("Helvetica",12))
        self.lbl2 = QLabel("   "); self.lbl2.setFont(QFont("Helvetica",12))
        self.lbl3 = QLabel("   "); self.lbl3.setFont(QFont("Helvetica",12))
        self.lbl4 = QLabel("   "); self.lbl4.setFont(QFont("Helvetica",12))
        self.lbl5 = QLabel("   "); self.lbl5.setFont(QFont("Helvetica",12))
        self.lbl6 = QLabel("   "); self.lbl6.setFont(QFont("Helvetica",12))
        self.lbl7 = QLabel("   "); self.lbl7.setFont(QFont("Helvetica",12))
        
        
        
        
        
        
        self.grid.addWidget(self.btc , 0 , 0)
        self.grid.addWidget(self.ltc , 1 , 0)
        self.grid.addWidget(trx , 2 , 0)
        self.grid.addWidget(eos , 3 , 0)
        self.grid.addWidget(xrp , 4 , 0)
        self.grid.addWidget(self.lbl ,  0 , 1)
        self.grid.addWidget(self.lbl1 , 1 , 1)
        self.grid.addWidget(self.lbl2 , 2 , 1)
        self.grid.addWidget(self.lbl3 , 3 , 1)
        self.grid.addWidget(self.lbl4 , 4 , 1)
        self.grid.addWidget(self.lbl5 , 5 , 1)
        self.grid.addWidget(self.lbl6 , 6 , 1)
        self.grid.addWidget(self.lbl7 , 7 , 1)
        
        
        
        scrapingUI.setLayout(self.grid)
        return scrapingUI
        
    def addCoinUI(self):
        
        generalTab = QWidget()
        
        izgaraCoinAdd = QGridLayout()
        
        lblCoinName = QLabel("Coin Name :")
        lblCoinName.setFont(QFont("Helvetica",12))
        
        self.coinName = QLineEdit()
        self.coinName.setFont(QFont("Helvetica",12))
        
        lblCoinUrl = QLabel("Coin URL :")
        lblCoinUrl.setFont(QFont("Helvetica",12))
        
        self.coinUrl = QLineEdit()
        self.coinUrl.setFont(QFont("Helvetica",12))
        
        addButton = QPushButton("Add")
        addButton.clicked.connect(self.addNewCoin)
        addButton.setFont(QFont("Helvetica",12))
        
        izgaraCoinAdd.addWidget(lblCoinName , 0 , 0)
        izgaraCoinAdd.addWidget(self.coinName , 0 , 1)
        izgaraCoinAdd.addWidget(lblCoinUrl , 1 , 0)
        izgaraCoinAdd.addWidget(self.coinUrl , 1 , 1)
        izgaraCoinAdd.addWidget(addButton, 2 , 3)
        
        generalTab.setLayout(izgaraCoinAdd)
        return generalTab
        
    def btcCheck(self):
        
        
        if self.btc.isChecked() == True:
            deger , ok = QInputDialog.getText(self, self.btc.text() , 'Coin limit')
            if ok == False:
                self.btc.setChecked(False)
            else:
                if deger == "":
                    QMessageBox.about(self , "Error" , "lütfen bir değer giriniz .")
                    self.btc.setChecked(False)
                else: # web scraping kısmı 
                   t1 = threading.Thread(target=self.coinFiyat , args=( self.btcurl , self.btc ,))
                   t1.start()
                    
        
    def ltcCheck(self):
        print("sa")
                
    def trxCheck(self):
        print("sa")
        
    def newCoinOne(self):
        
        
        if self.newCoin.isChecked() == True:
            
            t1 = threading.Thread(target=self.coinFiyat , args=( self.newCoinUrl , self.newCoin ,))
            t1.start()
            
        
    def newCoinOne1(self):
        print("merhaba")
        
    def newCoinOne2(self):
        print("si")
        
        
    def coinFiyat(self , url , sendCoin):
        global browser
        
        browser.get(url)
        
        
        while True:
            
            content = browser.page_source
            soup = BeautifulSoup(content , "html.parser")
            coin = soup.find("div" , attrs={"class" : "priceValue___11gHJ"})
            
            self.lbl.setText(coin.text)
            print(coin.text)
            
            if sendCoin.isChecked() == False:
                break
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
def main():
    app = QApplication(sys.argv)
    ex = mainPage()
    ex.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()