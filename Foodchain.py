import requests
import mysql.connector
from bigchaindb_driver import BigchainDB
import json
#import bip39

bdb_root_url = "http://127.0.0.1:9984"

class foodchain:
    def __init__(self,url,username,pass_key):
        self.url = url
        self.username = username
        self.pass_key = pass_key
        self.bdb = BigchainDB(bdb_root_url)


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
        #use bigchaindb_driver api 

        FoodItem={'grower':grower,
                        'package':package,
                        'company':company,
                        'id':'4242'
                 }
        metaData ={
                "action":"new asset api",
                "date":"timestamp"
                }

        assetData = {
                "data":{
                "type":"Food",
                "item":FoodItem
            }
        }

        prepared_creation_tx = self.bdb.transactions.prepare(

            operation="CREATE",
            signers = self.public_key,
            asset = assetData,
            metadata = metaData

        )


        fulfilled_creation_tx = self.bdb.transactions.fulfill(
                prepared_creation_tx, private_keys=self.private_key)


        sent_creation_tx = self.bdb.transactions.send_commit(fulfilled_creation_tx)
        print(sent_creation_tx == fulfilled_creation_tx)

        print(fulfilled_creation_tx)

        #I THINK THE PROBLEM WITH TRANSFER ASSET AND CREATE TRANSACTION IN API ARE THE SAME

        return fulfilled_creation_tx

        #if the transaction is succesful return txid
        #get the data from the response
        #DONE 

    def all_assets(self):
        #return all users asset
        #return all asset from javascript json response
        pass

    def transfer(self,tx_id,send_to):
        #accepts private key and pulic key
        """transfer_asset = requests.post(self.url+":8000/transfer",data={'tx_id':tx_id,
                                                    'public_key':self.public_key,
                                                                   'private':self.private_key
                                                                 }) """

        creation_tx = self.bdb.transactions.retrieve(tx_id)

        asset_id  =creation_tx['id']


        transfer_asset = {
                'id':asset_id
            }

        output_index = 0

        output = creation_tx['outputs'][output_index]

        transfer_input = {
               'fulfillment': output['condition']['details'],
                'fulfills': {
                'output_index': output_index,
                'transaction_id': creation_tx['id'],
                },
             'owners_before': output['public_keys'],
        }

        prepared_transfer_tx = self.bdb.transactions.prepare(
            operation='TRANSFER',
            asset=transfer_asset,
            inputs=transfer_input,
            recipients=send_to,
         )

        fulfilled_transfer_tx = self.bdb.transactions.fulfill(
              prepared_transfer_tx,
              private_keys=self.private_key,
         )

        sent_transfer_tx = self.bdb.transactions.send_commit(fulfilled_transfer_tx)
         
        print(sent_transfer_tx == fulfilled_transfer_tx)

        #returns sucesses
        #DONE
        pass
    def view_asset(self,tx_id):
        #detail for a single item thes thing
        name=self.bdb.assets.get(search=key)
        print(name)

    def history(self,key):
        #this is the most confusing 

        #returns the previous holders of the assets
        print("this is a tes for the history")



