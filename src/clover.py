

import requests
import json
from cloverapi.cloverapi_client import CloverApiClient
##api_client = CloverApiClient(api_key='58a4bb35-87da-abc7-6138-962388542938', merchant_id='1HQYHAGF9B181',api_url='https://api.clover.com:443')


api_client = CloverApiClient(api_key='1c911c53-5c01-7db3-e445-1c72ed33a877', merchant_id='NC1ZZ0V4K2W81',api_url='https://api.clover.com:443')

api_client.merchant_service.get_merchant()

## CREATE ITEM GROUP

ItemGroup = {'name': 'Ig1'}


api_client.inventory_service.create_item_group(ItemGroup)

ItemGroup = {'name': 'Ig2'}

api_client.inventory_service.create_item_group(ItemGroup)

api_client.inventory_service.get_item_groups()

api_client.inventory_service.delete_item_group_by_id("W84XAYT01Z1TC")


##Create Attributes for Item Group

attribute = {
     "name": "Color",
     "itemGroup": {'id': "T681GG0FG9ASW"}
}


api_client.inventory_service.create_attribute(attribute)



api_client.inventory_service.create_option('PNY4GA0PCHQXA',{"name":"Gray"})

# #CREATE ITEMS

api_client.inventory_service.create_inventory_item({
     "name": "pepsi",
     "price": 3455,
     "itemGroup": {"id": "T681GG0FG9ASW"}
})

api_client.inventory_service.create_inventory_item({
     "name": "hoodie",
     "price": 3999,
     "itemGroup": {"id": "T681GG0FG9ASW"}
})



api_client.inventory_service.get_inventory_items()

api_client.inventory_service.get_attributes()
api_client.inventory_service.get_options()

elements = [{ "item": {"id": "NFB771KYY6Q24"},"option": {"id": "SJCGAHVQHD9VE"}}]


api_client.inventory_service.create_or_delete_item_option_association()

##CREATE ORDER

##api_client.order_service.create_order(order=  {"item": {"id": "BP7JMG1ENXPGG"}, "state": "open"})

##api_client.order_service.create_order(order=  {"item": {"id": "BP7JMG1ENXPGG"}, "state": "open"})

api_client.order_service.create_order( {"item": {"id": "SH338FDES3RTY"}, "state": "open"})
api_client.order_service.create_order(order=  {"item": {"id": "BP7JMG1ENXPGG"}, "state": "open"})

api_client.order_service.create_order()

## GET ORDER ID'S

api_client.order_service.get_orders(HP9W6JV2TV5Z6)

## GET LINE ITEMS BY ORDER

api_client.order_service.get_line_items_by_order('HP9W6JV2TV5Z6')

#UPDATE ORDER BY LINE ITEM ID

api_client.order_service.

api_client.order_service.get_line_items_by_order()
api_client.order_service.get_order_by_id('6421JM0KT845G')


## ADD Line items by order ID


api_client.order_service.update_line_item_by_id()

api_client.inventory_service.get_inventory_items()
api_client.inventory_service.create_inventory_item()

api_client.order_service.ge

len(api_client.order_service.get_orders()['elements'])

api_client.inventory_service.get_inventory_items()

attribute_option = {
     "name": "Gray"
     "attribute":{'id' : "N4DPFX8BQGEEJ"}
}


