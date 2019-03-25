# IMPORT LIBRARIES

from squareconnect.rest import ApiException
from squareconnect.apis.locations_api import LocationsApi
from squareconnect.apis.transactions_api import TransactionsApi
from squareconnect.apis.v1_transactions_api import V1TransactionsApi
import pandas as pd
import json

# GETTING LOCATION

def get_loc_id(square):
    loc_id =[]
    api_instance = LocationsApi()
    api_instance.api_client.configuration.access_token = square["access_token"]
    api_response = api_instance.list_locations()
    x= api_response.locations[0]
    loc_id = str(x.id)
    return loc_id


# CALLING SQUARE API
def get_item(loc_id,sqaure):

    #api_instance = TransactionsApi()
    api_instance = V1TransactionsApi()



    api_instance.api_client.configuration.access_token = square["access_token"]
    api_response = api_instance.list_payments(location_id= loc_id)

    Item_name=[]
    Item_qauntity=[]
    Item_price=[]
    Item_Date=[]
    Order_ID = []
    Mer_ID =[]


    for i in range(0,len(api_response)):
        dt =api_response[i].created_at
        ordid = api_response[i].id
        merid = api_response[i]._merchant_id
        for r in range(0,len(api_response[i].itemizations)):
            Item_name.append(api_response[i].itemizations[r].name)
            Item_price.append(api_response[i].itemizations[r].single_quantity_money.amount)
            Item_qauntity.append(api_response[i].itemizations[r].quantity)
            Item_Date.append(dt)
            Order_ID.append(ordid)
            Mer_ID.append(merid)



    data = {'Name': Item_name, 'Quantity': Item_qauntity, 'Date': Item_Date,'Cost': Item_price,'Order ID': Order_ID,'Merchant_ID': Mer_ID }
        df = pd.DataFrame(data)
        df.to_csv('square.csv')
    pass

def main(square):
    loc_id = get_loc_id(square)

    get_item(loc_id,square)
    pass

if __name__ == "__main__":
    with open('/home/arajan/Documents/Githubrepo/POS_Integration/square.json') as jsonfile:
        square = json.load(jsonfile)
    main(square)
