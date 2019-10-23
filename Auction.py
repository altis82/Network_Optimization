# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 10:23:16 2019

@author: PC
"""

import numpy as np
import datetime
import random

class Trader:
    ID=None
    base_Price=0
    def __init__(self,ID,base_Price):
        self.ID=ID
        self.base_Price=base_Price
    def set_price(self, price):
        self.base_Price=price
class Auctioneer:
    ID=None
    bid=0
    def __init__(self, ID,bid):
        self.ID=ID
        self.bid=bid
    def bidding(self):
        r=np.random.rand()
        
        if r>=0.4:
            #print(r,"\n")
            self.bid=self.bid+5*r
            #print(self.bid,"\n")
        
if __name__ == '__main__':
    Trader1=Trader(0,10)
    List_auctioneer=[]
    Number_auctioneer=4
    max_price=Trader1.base_Price
    max_id=0
    price_list=np.zeros(Number_auctioneer)
    for i in range(Number_auctioneer):
        auctioneer=Auctioneer(i,Trader1.base_Price)
        List_auctioneer.append(auctioneer)
    #open the auction
    print("Start a session\n")
    flag=0
    while 1:
        flag=0
        print("\n -----New round-----\n")
        for i in range(Number_auctioneer):
            List_auctioneer[i].bidding()
            print("\n Auctioneer ",i," bid ",List_auctioneer[i].bid,"\n")
            if(max_price<List_auctioneer[i].bid):
                max_price=List_auctioneer[i].bid
                max_id=i                
                Trader1.base_Price=max_price
                flag=1
                
        if flag==0:
            print("Stop the session!\n")
            print("Auctionner:",max_id," is win with the bidding ", List_auctioneer[max_id].bid)
            break
    #check the second price
    for i in range(Number_auctioneer):
        price_list[i]=List_auctioneer[i].bid
    price_list=np.array(np.sort(price_list))
    print("\nSecond price:",price_list[2])
    