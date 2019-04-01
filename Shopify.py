
import shopify

import requests

URL =  "https://finarb.myshopify.com/admin/oauth/authorize"

PARAMS = {'API_KEY':'978f0e59597a7b4addab471e24455de2','scope':'read_orders'}

r = requests.get(url = URL, params = PARAMS)


API_KEY = '978f0e59597a7b4addab471e24455de2'
SHARED_SECRET ='ee18d5fb67cefb25dea5e532da7c6199'

shop_url = "https://%s:%s@finarb.myshopify.com/admin" % (API_KEY, SHARED_SECRET)


shopify.ShopifyResource.set_site(shop_url)

shopify.Shop()

# Get the current shop
shop = shopify.Shop.current()

# Get a specific product
product = shopify.Product.find(179761209)

# Create a new product
new_product = shopify.Product()
new_product.title = "Burton Custom Freestyle 151"
new_product.product_type = "Snowboard"
new_product.vendor = "Burton"
success = new_product.save() #returns false if the record is invalid
# or
if new_product.errors:
    #something went wrong, see new_product.errors.full_messages() for example

# Update a product
product.handle = "burton-snowboard"
product.save()

# Remove a product
product.destroy()

shopify.Currency()


shop = shopify.Shop.current()




shopify.InventoryLevel()

shop = shopify.Shop.current()

# Get a specific product
product = shopify.Product.find(179761209)

# Create a new product
new_product = shopify.Product()
new_product.title = "Burton Custom Freestyle 151"
new_product.product_type = "Snowboard"
new_product.vendor = "Burton"
success = new_product.save() #returns false if the record is invalid
# or
if new_product.errors:
    #something went wrong, see new_product.errors.full_messages() for example

# Update a product
product.handle = "burton-snowboard"
product.save()

# Remove a product
product.destroy()