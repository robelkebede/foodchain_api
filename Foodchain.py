
import requests
import mysql.connector
#import bip39

class foodchain:
    def __init__(self,url,username,pass_key):
        self.url = url
        self.username = username
        self.pass_key = pass_key

        mydb = mysql.connector.connect(
         host="localhost",
         user="root",
         password="",
         database="foodchain"
        )
        if(mysql):
            print("connected")
        cursor = mydb.cursor()
        cursor.execute('select * from foodchain.users where username="'+self.username+'" && pass_key="'+self.pass_key+'" ')

        user =cursor.fetchall()
        if len(user) == 0:
            raise "You are not an authinticated user"

        #import bip39 and generate public and private key
        key = None # puy the private and public key in hear
        #DONE

    def create(self,grower,company,package):
        #create a transaction
        create_transaction = requests.post(self.url+"/new_asset",data={'grower':grower,
                                                                       'package':package,
                                                                       'company':company,
                                                                      })
        #if the transaction is succesful return txid
        #get the data from the response
        #DONE 

    def all_assets(self):
        #return all users asset
        #return all asset from javascript json response
        pass

    def transfer(self,tx_id):
        #accepts private key and pulic key
        transfer_asset = requests.post(self.url+"/transfer",data={'tx_id':tx_id,
                                                                  'public_key':self.key.public_key
                                                                 })
        #returns sucesses
        #DONE
        pass

    def history(self,tx_id):
        #returns the previous holders of the asset
        print("this is a tes for the history")



