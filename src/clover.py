



from cloverapi.cloverapi_client import CloverApiClient
api_client = CloverApiClient(api_key='58a4bb35-87da-abc7-6138-962388542938', merchant_id='1HQYHAGF9B181',api_url='https://api.clover.com:443')

api_client.merchant_service.get_merchant()