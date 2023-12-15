import http.client
import json

currency_from = "USD"
currency_to = "CZK"
my_personal_key = "5d05c740a5687982d8e28e9f"

host = "v6.exchangerate-api.com"
endpoint = "/v6/{}/latest/{}"
method_requests = "GET"
key_for_rates = "conversion_rates"

conn = http.client.HTTPSConnection(host)
conn.request(method_requests, endpoint.format(my_personal_key, currency_from))
response = conn.getresponse()
print(response.status, response.reason)
body = response.read()
print(body)
y = json.loads(body)
print(y)
conversion_rates = y[key_for_rates]
print(conversion_rates)
EUR_to_CZK = conversion_rates[currency_to]
print(EUR_to_CZK)