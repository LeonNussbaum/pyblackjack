#Cards Used https://code.google.com/archive/p/vector-playing-cards/downloads Playing Cards Version 1.3  
import os
from sre_parse import State
from tkinter import *
import tkinter as tk
import tkinter.ttk as ttk
import numpy as np
from PIL import Image, ImageTk

class deck:
    def __init__(self):
        self.symbols = ['A', '2', '3','4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K' ]
        self.colors = ['C', 'H', 'S', 'D']
        self.deck = []

    def createdeck(self):
        for x in range(3):
            for color in self.colors:
                for symbol in self.symbols:                   
                    if(symbol == 'A'):
                        value = 11
                        self.deck.append(Card(symbol, color, value))
                    elif(symbol == 'J'):
                        value = 10
                        self.deck.append(Card(symbol, color, value))
                    elif(symbol == 'Q'):
                        value = 10
                        self.deck.append(Card(symbol, color, value))
                    elif(symbol == 'K'):
                        value = 10
                        self.deck.append(Card(symbol, color, value))
                    else:
                        value = int(symbol)
                        self.deck.append(Card(symbol, color, value))                   
        np.random.shuffle(self.deck)

class player:
    def __init__(self):
        self.monney = 1000
        self.bet = 0

class carddata:
    def __init__(self) -> None:
        self.cards = []
        self.points = 0
        self.cardcount = 0
        self.hasbj = False

    def reset(self):
        self.cards = []
        self.points = 0
        self.cardcount = 0
        self.hasbj = False

class gamedata:
    def __init__(self) -> None:
        self.player = carddata()
        self.dealer = carddata()
    
    def cleanup(self):
        self.player.reset()
        self.dealer.reset()

class Card:
    def __init__(self, color, symbol, value):
        self.value = value
        self.color = color
        self.symbol = symbol

class blackjack:
    def __init__(self, master=None):
        root = tk.Tk() if master is None else tk.Toplevel(master)
        root.configure(background="#194d33",height=1280,takefocus=True,width=720)
        root.geometry("1280x720")
        root.resizable(False, False)
        root.title("BLACKJACK")
        iconpng = PhotoImage(file = 'img/icon.png')   
        root.iconphoto(False, iconpng) 

        self.cardsframe = tk.Frame(root)
        self.cardsframe.configure(background="#194d33",height=200,padx=5,pady=0,width=200)
        
        self.dealerpoints = ttk.Label(self.cardsframe)
        self.dealerpoint = tk.StringVar(value="0")
        self.dealerpoints.configure(background="#194d33",text='0',textvariable=self.dealerpoint,font="{Arial} 24 {}",foreground="#5d605e")
        self.dealerpoints.grid(column=0, row=0)

        self.playerpoints = ttk.Label(self.cardsframe)
        self.playerpoint = tk.StringVar(value=0)
        self.playerpoints.configure(background="#194d33",text='0',textvariable=self.playerpoint,font="{Arial} 24 {}",foreground="#5d605e")
        self.playerpoints.grid(column=0, row=3)

        self.bg = Image.open('img/BG.png')
        self.bg = ImageTk.PhotoImage(self.bg)

        self.dealercards = tk.Frame(self.cardsframe)
        self.dealercards.configure(background="#194d33",height=200,padx=5,pady=5,width=200)
        self.dealercard1 = tk.Label(self.dealercards, image=self.bg)
        self.dealercard1.grid(column=0, padx=10, pady=10, row=0)
        self.dealercard2 = tk.Label(self.dealercards,background="#194d33")
        self.dealercard2.grid(column=1, padx=10, pady=10, row=0)
        self.dealercard3 = tk.Label(self.dealercards,background="#194d33")
        self.dealercard3.grid(column=2, padx=10, pady=10, row=0)
        self.dealercard4 = tk.Label(self.dealercards,background="#194d33")
        self.dealercard4.grid(column=3, padx=10, pady=10, row=0)
        self.dealercard5 = tk.Label(self.dealercards,background="#194d33")
        self.dealercard5.grid(column=4, padx=10, pady=10, row=0)
        self.dealercard6 = tk.Label(self.dealercards,background="#194d33")
        self.dealercard6.grid(column=5, padx=10, pady=10, row=0)
        self.dealercards.grid(column=0, row=1)

        self.playercards = tk.Frame(self.cardsframe)
        self.playercards.configure(background="#194d33",height=200,padx=5,pady=5,width=200)
        self.playercard1 = tk.Label(self.playercards,image=self.bg)
        self.playercard1.grid(column=0, padx=10, pady=10, row=0)
        self.playercard2 = tk.Label(self.playercards,background="#194d33")
        self.playercard2.grid(column=1, padx=10, pady=10, row=0)        
        self.playercard3 = tk.Label(self.playercards,background="#194d33")
        self.playercard3.grid(column=2, padx=10, pady=10, row=0)
        self.playercard4 = tk.Label(self.playercards,background="#194d33")
        self.playercard4.grid(column=3, padx=10, pady=10, row=0)
        self.playercard5 = tk.Label(self.playercards,background="#194d33")
        self.playercard5.grid(column=4, padx=10, pady=10, row=0)
        self.playercard6 = tk.Label(self.playercards,background="#194d33")
        self.playercard6.grid(column=5, padx=10, pady=10, row=0)
        self.playercards.grid(column=0, row=2)

        self.cardsframe.pack(padx=10, pady=10, side="top")
        self.cardsframe.grid_anchor("center")

        self.guiitems = tk.Frame(root)
        self.guiitems.configure(background="#292929", height=200, width=200)

        self.Game_BTNS = tk.Frame(self.guiitems, container="false")
        self.Game_BTNS.configure(background="#292929", height=0, width=0)

        self.staybtn = ttk.Button(self.Game_BTNS)
        self.staybtn.configure(text='STAY',command=self.staycmd, state=DISABLED)
        self.staybtn.grid(column=0, ipady=10, padx=10, pady=10, row=1)

        self.hitbtn = ttk.Button(self.Game_BTNS)
        self.hitbtn.configure(text='HIT', command=self.hitbtnconf , state=DISABLED)
        self.hitbtn.grid(column=1, ipady=10, padx=10, row=1)

        self.doublebtn = ttk.Button(self.Game_BTNS)
        self.doublebtn.configure(text='DOUBLE',command=self.doublecmd ,state=DISABLED,)
        self.doublebtn.grid(column=3, ipady=10, padx=10, row=1)

        label1 = ttk.Label(self.Game_BTNS)
        self.monney = tk.IntVar(value=player1.monney)
        label1.configure(background="#292929",font="{Arial} 24 {}",foreground="#00f2aa",justify="center",text='800',textvariable=self.monney)
        label1.grid(column=2, row=1)

        self.Game_BTNS.grid(column=0, row=0)
        
        self.bet_value = tk.Frame(self.guiitems)
        self.bet_value.configure(background="#292929", height=400, width=400)

        self.betaddbtn = ttk.Button(self.bet_value)
        self.betaddbtn.configure( text='+', command=self.addbtncmd)
        self.betaddbtn.grid(column=1, padx=10, row=0)
        
        self.betminusbtn = ttk.Button(self.bet_value)
        self.betminusbtn.configure(text='-',command=self.minusbtncmd)
        self.betminusbtn.grid(column=0, padx=10, row=0)

        self.betbtn = tk.Button(self.bet_value)
        self.betbtn.configure(background="#ff4242",font="{Arial} 14 {}",state="active",text='BET',command=self.bethit)
        self.betbtn.grid(column=5, row=0)
        self.betint = tk.IntVar(value=player1.bet)
        
        self.betvallabel = ttk.Label(self.bet_value)
        self.betvallabel.configure(background="#292929",font="{Arial} 14 {}",text='5',foreground="#f4fffc",textvariable=self.betint)
        self.betvallabel.grid(column=2, padx=10, pady=10, row=0)

        self.bet_value.grid(column=0, row=6, sticky="w")
        self.bet_value.grid_anchor("n")

        self.guiitems.pack(side="top")

        self.mainwindow = root

    def addbtncmd(self):
        self.betint.set(self.betint.get()+10)
        if(self.betint.get() > player1.monney):
            self.betint.set(player1.monney)

    def minusbtncmd(self):
        self.betint.set(self.betint.get()-10)
        if(self.betint.get() < 0):
            self.betint.set(0)

    def gentext(self, cards):
        text =  cards.color +cards.symbol
        text = 'img/' + text +'.png'       
        return text

    def countpoints(self, cards):
        i = 0
        ascount = 0
        for card in cards:
            if(card.value == 11):
                ascount = ascount +1
            i = i + card.value
            if(i>21 and ascount > 0):
                i = i -10
                ascount = ascount-1           
        return i

    def bethit(self):
        global gamedata1
        gamedata1 = gamedata()
        self.gamereset()

        player1.bet = self.betint

        if(self.betint.get() == 0):
            return
        elif(self.betint.get() > player1.monney):
            return

        if(len(deck1.deck) < 78):
            deck1.createdeck()

        self.staybtn["state"] = "enable"
        self.hitbtn["state"] = "enable"

        if(player1.bet.get() < player1.monney):
            self.doublebtn["state"] = "enable"

        player1.monney = player1.monney - player1.bet.get()
        self.monney.set(player1.monney)
        self.betbtn["state"] = DISABLED
        self.betaddbtn["state"] = DISABLED
        self.betminusbtn["state"] = DISABLED
        
        gamedata1.player.cards.append(deck1.deck[0])
        deck1.deck.pop(0)

        player_image = self.gentext(gamedata1.player.cards[gamedata1.player.cardcount])
        self.img1 = Image.open(player_image)
        self.img1 = ImageTk.PhotoImage(self.img1)
        self.playercard1.configure(image=self.img1)

        gamedata1.player.cardcount = gamedata1.player.cardcount + 1

        gamedata1.dealer.cards.append(deck1.deck[0])
        deck1.deck.pop(0)
        player_image = self.gentext(gamedata1.dealer.cards[gamedata1.dealer.cardcount])
        self.img = Image.open(player_image)
        self.img = ImageTk.PhotoImage(self.img)

        self.dealercard1.configure(image=self.img)

        self.dealerpoint.set(self.countpoints(gamedata1.dealer.cards))
        gamedata1.dealer.cardcount= gamedata1.dealer.cardcount + 1

        gamedata1.player.cards.append(deck1.deck[0])
        deck1.deck.pop(0)

        player_image = self.gentext(gamedata1.player.cards[gamedata1.player.cardcount])
        self.img11 = Image.open(player_image)
        self.img11 = ImageTk.PhotoImage(self.img11)
        self.playercard2.configure(image=self.img11)

        gamedata1.player.cardcount = gamedata1.player.cardcount + 1

        gamedata1.dealer.cards.append(deck1.deck[0])
        deck1.deck.pop(0)
        
        self.bg2 = Image.open('img/BG.png')
        self.bg2 = ImageTk.PhotoImage(self.bg2)

        self.dealercard2.configure(image=self.bg2)

        gamedata1.dealer.cardcount= gamedata1.dealer.cardcount + 1

        self.playerpoint.set(self.countpoints(gamedata1.player.cards))
        gamedata1.player.points = self.countpoints(gamedata1.player.cards)
        
        if(gamedata1.player.points == 21):
            self.staycmd()

    def doublecmd(self):
        player1.monney = player1.monney - player1.bet.get()
        self.monney.set(player1.monney)
        player1.bet.set(player1.bet.get()*2)
        self.betint.set(player1.bet.get())
        self.hitbtnconf()
        
        if(gamedata1.player.points > 21):
            self.playerbust()
        else:
            self.staycmd()
        self.betint.set(player1.bet.get()/2)

    def staycmd(self):
        self.staybtn["state"] = DISABLED
        self.hitbtn["state"] = DISABLED
        self.doublebtn["state"] = DISABLED
        player_image = self.gentext(gamedata1.dealer.cards[1])
        self.img213 = Image.open(player_image)
        self.img213 = ImageTk.PhotoImage(self.img213)
        self.dealercard2.configure(image=self.img213)
        self.dealerpoint.set(self.countpoints(gamedata1.dealer.cards))
        gamedata1.dealer.points = self.countpoints(gamedata1.dealer.cards)

        self.dealerpoint.set(self.countpoints(gamedata1.dealer.cards))
        gamedata1.dealer.points = self.countpoints(gamedata1.dealer.cards)

        while gamedata1.dealer.points < 17:
            gamedata1.dealer.cards.append(deck1.deck[0])
            deck1.deck.pop(0)
            self.dealerpoint.set(self.countpoints(gamedata1.dealer.cards))
            gamedata1.dealer.points = self.countpoints(gamedata1.dealer.cards)
            self.dealerpoint.set(self.countpoints(gamedata1.dealer.cards))
            gamedata1.dealer.points = self.countpoints(gamedata1.dealer.cards)
            
            dealer_img = self.gentext(gamedata1.dealer.cards[gamedata1.dealer.cardcount])
            self.dimg12 = Image.open(dealer_img)

            if(gamedata1.dealer.cardcount == 2):
                self.dimg1235 = Image.open(dealer_img)
                self.dimg1235 = ImageTk.PhotoImage(self.dimg1235)
                self.dealercard3.configure(image=self.dimg1235)
            if(gamedata1.dealer.cardcount == 3):
                self.dimg123 = Image.open(dealer_img)
                self.dimg123 = ImageTk.PhotoImage(self.dimg123)
                self.dealercard4.configure(image=self.dimg123)
            elif(gamedata1.dealer.cardcount == 4): 
                self.dimg1234 = Image.open(dealer_img)
                self.dimg1234 = ImageTk.PhotoImage(self.dimg1234)
                self.dealercard5.configure(image=self.dimg1234)
            elif(gamedata1.dealer.cardcount == 5):
                self.dimg12345 = Image.open(dealer_img)
                self.dimg12345 = ImageTk.PhotoImage(self.dimg12345)
                self.dealercard6.configure(image=self.dimg12345)
            gamedata1.dealer.cardcount = gamedata1.dealer.cardcount + 1
        self.compervalue()    
            
    def playerbust(self):
        self.staybtn["state"] = DISABLED
        self.hitbtn["state"] = DISABLED
        self.doublebtn["state"] = DISABLED
        self.playerpoint.set(">21 :( " + str(gamedata1.player.points)+" +0")
        self.dealerpoint.set(">21 :( " + str(gamedata1.dealer.points)+" +0")

        self.betaddbtn["state"] = "active"
        self.betminusbtn["state"] = "active"
        self.betbtn["state"] = "active"

    def checkbj(self,carddata):
        if(carddata.cardcount == 2 and carddata.points == 21):
            return True
        else:
            return False

    def compervalue(self):
        gamedata1.player.hasbj = self.checkbj(gamedata1.player)
        gamedata1.dealer.hasbj = self.checkbj(gamedata1.dealer)

        if(gamedata1.dealer.hasbj and gamedata1.player.hasbj):
            self.playerpoint.set("DEALER AND PLAYER BLACKJACK!!!!! "+ str(gamedata1.player.points)+ " +" + str(player1.bet.get()))
            self.dealerpoint.set("DEALER AND PLAYER BLACKJACK!!!!! "+ str(gamedata1.dealer.points))
            player1.monney = player1.monney + player1.bet.get()
        
        elif(gamedata1.player.hasbj):
            self.playerpoint.set("BLACKJACK!!!!! "+ str(gamedata1.player.points) + " +" + str(player1.bet.get()*2.5))
            self.dealerpoint.set("BLACKJACK!!!!! "+ str(gamedata1.dealer.points) + " +" + str(player1.bet.get()*2.5))
            player1.monney = player1.monney + player1.bet.get()*2.5
        elif(gamedata1.dealer.hasbj):
            self.playerpoint.set("DEALER BLACKJACK!!!!! "+ str(gamedata1.player.points) +" +0")
            self.dealerpoint.set("DEALER BLACKJACK!!!!! "+ str(gamedata1.dealer.points) +" +0")

        elif(gamedata1.dealer.points > 21):
            self.playerpoint.set("Dealer bust " + str(gamedata1.player.points) + " +" + str(player1.bet.get()*2))
            self.dealerpoint.set("Dealer bust "+ str(gamedata1.dealer.points)+ " +" + str(player1.bet.get()*2))
            player1.monney = player1.monney + player1.bet.get()*2

        elif(gamedata1.dealer.points > gamedata1.player.points):
            self.playerpoint.set("Dealer points > Player points " + str(gamedata1.player.points)+" +0")
            self.dealerpoint.set("Dealer points > Player points "+ str(gamedata1.dealer.points)+" +0")
        elif(gamedata1.player.points > gamedata1.dealer.points):
            self.playerpoint.set("Dealer points < Player points "+ str(gamedata1.player.points)+" +"+ str(player1.bet.get()*2))
            self.dealerpoint.set("Dealer points < Player points "+ str(gamedata1.dealer.points)+ " +" + str(player1.bet.get()*2))
            player1.monney = player1.monney + player1.bet.get()*2
        elif(gamedata1.player.points == gamedata1.dealer.points):
            self.playerpoint.set("Dealer points = Player points "+ str(gamedata1.player.points) + " +" + str(player1.bet.get()))
            self.dealerpoint.set("Dealer points = Player points "+ str(gamedata1.dealer.points)+ " +" + str(player1.bet.get()))
            player1.monney = player1.monney + player1.bet.get()

        self.monney.set(player1.monney)

        self.betbtn["state"] = "active"
        self.betaddbtn["state"] = "active"
        self.betminusbtn["state"] = "active"

    def hitbtnconf(self):
        self.doublebtn["state"] = DISABLED
        if(gamedata1.player.points < 21):
            gamedata1.player.cards.append(deck1.deck[0])
            deck1.deck.pop(0)
            player_image = self.gentext(gamedata1.player.cards[gamedata1.player.cardcount])
            gamedata1.player.cardcount = gamedata1.player.cardcount + 1

            if(gamedata1.player.cardcount == 3):
                self.img12 = Image.open(player_image)
                self.img12 = ImageTk.PhotoImage(self.img12)
                self.playercard3.configure(image=self.img12)
            elif(gamedata1.player.cardcount == 4):
                self.img123 = Image.open(player_image)
                self.img123 = ImageTk.PhotoImage(self.img123)
                self.playercard4.configure(image=self.img123)
            elif(gamedata1.player.cardcount == 5): 
                self.img1234 = Image.open(player_image)
                self.img1234 = ImageTk.PhotoImage(self.img1234)
                self.playercard5.configure(image=self.img1234)                
            elif(gamedata1.player.cardcount == 6):
                self.img12345 = Image.open(player_image)
                self.img12345 = ImageTk.PhotoImage(self.img12345)
                self.playercard6.configure(image=self.img12345)

            self.playerpoint.set(self.countpoints(gamedata1.player.cards))
            gamedata1.player.points = self.countpoints(gamedata1.player.cards)

        if(gamedata1.player.points > 21):
            self.playerbust()
        elif(gamedata1.player.points == 21):
            self.staycmd()        

    def gamereset(self):
        gamedata1.cleanup()

        self.bg = Image.open('img/BG.png')
        self.bg = ImageTk.PhotoImage(self.bg)

        self.dealercard1.configure(image=self.bg)
        self.dealercard2.configure(image="")
        self.dealercard3.configure(image="")
        self.dealercard4.configure(image="")
        self.dealercard5.configure(image="")
        self.dealercard6.configure(image="")

        self.playercard1.configure(image=self.bg)
        self.playercard2.configure(image="")
        self.playercard3.configure(image="")
        self.playercard4.configure(image="")
        self.playercard5.configure(image="")
        self.playercard6.configure(image="")

        self.staybtn["state"] = DISABLED
        self.hitbtn["state"] = DISABLED
        self.doublebtn["state"] = DISABLED
        self.betaddbtn["state"] = "active"
        self.betminusbtn["state"] = "active"       
        self.betbtn["state"] = "active"   

    def run(self):
        self.mainwindow.mainloop()
player1 = player()
deck1 = deck()
app = blackjack()
app.run()
