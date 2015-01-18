import json
import requests

api_key = "e602eb3b-e66b-41d0-930b-e8e9fb9b2c0e"
customer_id = "cus_KAd5ZzI0-yICtF"
postmates_url = "https://api.postmates.com"

def post_delivery_quote(source_address, delivery_address):
    url = postmates_url + "/v1/customers/" + customer_id + "/delivery_quotes/"
    payload = {
        'pickup_address': source_address,
        'dropoff_address': delivery_address
    }
    result = requests.post(url, data=payload, auth=(api_key,''))
    return result

def post_create_delivery(payload):
    url = postmates_url + "/v1/customers/" + customer_id + "/deliveries"
    result = requests.post(url, data=payload, auth=(api_key,''))
    return result
