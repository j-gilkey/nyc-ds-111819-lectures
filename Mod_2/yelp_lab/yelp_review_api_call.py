import json
import requests

url = 'https://api.yelp.com/v3/businesses/search'

client_id = "F475wXQIdgD3Q7epch9QDA"
api_key = "k6TYJi5qpisv2T3ZgvU2QpxXoJ6b5zEMbS7wJFKyvFlDMASkuvLUMKcMGfU4K5iefWZRT0TSMuAe77IIJxmg8hFW6aq_4NtijcWYp6w3i1yRfNOIZFdu5241j2LpXXYx"
headers = {
        'Authorization': 'Bearer {}'.format(api_key),
    }

term = 'Tea'
location = 'Alphabet City'
radius = 1000
limit  = 50

url_params = {
                'term': term.replace(' ', '+'),
                'location': location.replace(' ', '+'),
                'radius' : radius,
                'limit' : limit
            }

response = requests.get(url, headers=headers, params=url_params)

data = response.json()

def parse_data(businesses):
    biz_list = []

    for business in businesses:
        if 'price' in business.keys():
            biz_tuple = (business['id'], business['name'], business['rating'], business['review_count'], business['price'] )
            biz_list.append(biz_tuple)
        else:
            biz_tuple = (business['id'], business['name'], business['rating'], business['review_count'], None )
            biz_list.append(biz_tuple)
    return biz_list

business_data = parse_data(data['businesses'])

print(business_data[0])
