
from squareconnect.rest import ApiException
from squareconnect.apis.locations_api import LocationsApi
api_instance = LocationsApi()
api_instance.api_client.configuration.access_token = 'EAAAEOBMM7-B8GAqhBJEIqAgodrXyq7EmVZc_uGdx_GxdqF-IQG6lwITGsmPdV9J'
api_response = api_instance.list_locations()
x= api_response.locations[0]
location_id = str(x.id)



from squareconnect.apis.transactions_api import TransactionsApi
api_instance = TransactionsApi()


from squareconnect.apis.v1_transactions_api import V1TransactionsApi


api_transaction = V1TransactionsApi()


api_instance.api_client.configuration.access_token = 'EAAAEOBMM7-B8GAqhBJEIqAgodrXyq7EmVZc_uGdx_GxdqF-IQG6lwITGsmPdV9J'
api_response = api_instance.list_payments(location_id='3KK1N9SVK8QP1')

Item_name=[]
Item_qauntity=[]
Item_price=[]
Item_Date=[]

for i in range(0,len(api_response)):
    Item_Date.append(api_response[i].created_at)
    for r in range(0,len(api_response[i].itemizations)):
        Item_name.append(api_response[i].itemizations[r].name)
        Item_price.append(api_response[i].itemizations[r].single_quantity_money[0])
        Item_qauntity.append(api_response[i].itemizations[r].quantity)
        
data = {'Name': Item_name, 'Quantity': Item_qauntity, 'Date': Item_Date, 'Cost': Item_price}
    df = pd.DataFrame(data)
    df.to_csv('square.cs')
