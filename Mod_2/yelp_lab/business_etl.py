import json
import requests
import mysql.connector
import config

url = 'https://api.yelp.com/v3/businesses/search'

client_id = "F475wXQIdgD3Q7epch9QDA"
api_key = "k6TYJi5qpisv2T3ZgvU2QpxXoJ6b5zEMbS7wJFKyvFlDMASkuvLUMKcMGfU4K5iefWZRT0TSMuAe77IIJxmg8hFW6aq_4NtijcWYp6w3i1yRfNOIZFdu5241j2LpXXYx"
headers = {
        'Authorization': 'Bearer {}'.format(api_key),
    }

print(headers)

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

DB_NAME = 'yelp_tea'

cnx = mysql.connector .connect(
    host = config.host,
    user = config.user,
    passwd = config.password,
    database = DB_NAME,
    use_pure=True
)

cursor = cnx.cursor()

def yelp_call(url_params, headers, url):
    response = requests.get(url, headers=headers, params=url_params)
    data = response.json()
    return data['businesses']

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

def db_insert(cnx, cursor, parsed_results):
    add_business = ("""INSERT INTO yelp_businesses
               (business_id, name, rating, review_count, price)
               VALUES (%s, %s, %s, %s, %s)""")
    cursor.executemany(add_business, parsed_results)
    cnx.commit()
    print('Good job!')

def paginate(url_params, headers, url, max = 266):
    cur = 0
    while cur < max:
        url_params['offset'] = cur
        businesses = yelp_call(url_params, headers, url)
        parsed_results = parse_data(businesses)
        db_insert(cnx, cursor, parsed_results)
        cur += 50

#paginate(url_params, headers, url)
