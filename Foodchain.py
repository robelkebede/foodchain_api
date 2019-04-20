import requests
import mysql.connector
import json
#import bip39

class foodchain:
    def __init__(self,url,username,pass_key):
        self.url = url
        self.username = username
        self.pass_key = pass_key


        mydb = mysql.connector.connect(
                host="127.0.0.1",
                user="root",
                password="password",
                database="foodchain",
                port=3306
        )
        
        if mysql:
            print("connected")
        cursor = mydb.cursor()
        cursor.execute('select * from foodchain.users where username="'+self.username+'" && pass_key="'+self.pass_key+'" ')

        user =cursor.fetchall()
        if len(user) == 0:
            raise "You are not an authinticated user"

        #get private and public key
        r = requests.post(self.url+":8000/get_user_api/",data={"pass_key":self.pass_key}).text;
        key = json.loads(r)["id"]
        self.public_key = key["publicKey"]
        self.private_key = key["privateKey"]

        #done

    def create(self,grower,company,package):
        #create a transaction
        create_transaction = requests.post(self.url+":8000/new_asset_api",data={'grower':grower,
                                                                       'package':package,
                                                                       'company':company,
                                                                       }).text
        #use bigchaindb_driver api 
        #how to send the key alongside with the data


        print(create_transaction)

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
    def view_asset(self,tx_id):
        #detail for a single item thes thing
        pass

    def history(self,tx_id):
        #returns the previous holders of the assets
        print("this is a tes for the history")



