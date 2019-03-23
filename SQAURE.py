
from squareconnect.rest import ApiException
from squareconnect.apis.locations_api import LocationsApi
api_instance = LocationsApi()
api_instance.api_client.configuration.access_token = 'EAAAEOBMM7-B8GAqhBJEIqAgodrXyq7EmVZc_uGdx_GxdqF-IQG6lwITGsmPdV9J'
api_response = api_instance.list_locations()
print (api_response.locations)


from squareconnect.apis.transactions_api import TransactionsApi
api_instance = TransactionsApi()
api_instance.api_client.configuration.access_token = 'EAAAEOBMM7-B8GAqhBJEIqAgodrXyq7EmVZc_uGdx_GxdqF-IQG6lwITGsmPdV9J'
api_response = api_instance.list_transactions(location_id='3KK1N9SVK8QP1')

from squareconnect.apis.orders_api import OrdersApi
api_instance = OrdersApi()
api_instance.api_client.configuration.access_token = 'EAAAEOBMM7-B8GAqhBJEIqAgodrXyq7EmVZc_uGdx_GxdqF-IQG6lwITGsmPdV9J'
body = {
  "idempotency_key": "8193148c-9586-11e6-99f9-28cfe92138cf",
  "line_items": [
    {
      "name": "coke",
      "quantity": "2",
      "variation_name" : "Regular",
      "base_price_money": {
        "amount": 3300,
        "currency": "INR"
      }
    }
  ]
}
api_response = api_instance.create_order(location_id='3KK1N9SVK8QP1',body=body)



from squareconnect.apis.v1_transactions_api import V1TransactionsApi

api_instance = V1TransactionsApi()
api_instance.api_client.configuration.access_token = 'EAAAEOBMM7-B8GAqhBJEIqAgodrXyq7EmVZc_uGdx_GxdqF-IQG6lwITGsmPdV9J'
api_response = api_instance.list_payments(location_id='3KK1N9SVK8QP1')



from squareconnect.apis.v1_items_api import V1ItemsApi
api_instance = V1ItemsApi()
api_instance.api_client.configuration.access_token = 'EAAAEOBMM7-B8GAqhBJEIqAgodrXyq7EmVZc_uGdx_GxdqF-IQG6lwITGsmPdV9J'
api_response = api_instance.list_items(location_id='3KK1N9SVK8QP1')

from squareconnect.apis.TransactionsApi import TransactionsApi




from squareconnect.apis.v1_transactions_api import V1TransactionsApi
from squareconnect.apis.orders_api import OrdersApi

from squareconnect.apis import reporting_api



# create an instance of the Location API class


api_orders = OrdersApi()
api_orders.api_client.configuration.access_token = 'EAAAEOBMM7-B8GAqhBJEIqAgodrXyq7EmVZc_uGdx_GxdqF-IQG6lwITGsmPdV9J'
api_orders.batch_retrieve_orders(location_id='3KK1N9SVK8QP1')

OrdersApi.create_order(location_id= '3KK1N9SVK8QP1')


OrdersApi.api_client.configuration.access_token = 'EAAAEOBMM7-B8GAqhBJEIqAgodrXyq7EmVZc_uGdx_GxdqF-IQG6lwITGsmPdV9J'
api_reporting = reporting_api()

api_reporting.api_client.configuration.access_token = 'EAAAEOBMM7-B8GAqhBJEIqAgodrXyq7EmVZc_uGdx_GxdqF-IQG6lwITGsmPdV9J'

try:
    # ListLocations

except ApiException as e:
    print ('Exception when calling LocationApi->list_locations: %s\n' % e)


api_orders.list_orders(location_id='3KK1N9SVK8QP1')
