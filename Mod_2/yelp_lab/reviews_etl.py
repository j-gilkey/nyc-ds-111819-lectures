import json
import requests
import mysql.connector
import config

client_id = "F475wXQIdgD3Q7epch9QDA"
api_key = "k6TYJi5qpisv2T3ZgvU2QpxXoJ6b5zEMbS7wJFKyvFlDMASkuvLUMKcMGfU4K5iefWZRT0TSMuAe77IIJxmg8hFW6aq_4NtijcWYp6w3i1yRfNOIZFdu5241j2LpXXYx"
headers = {
        'Authorization': 'Bearer {}'.format(api_key),
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

query = ("""SELECT business_id FROM yelp_businesses""")

cursor.execute(query)

data = cursor.fetchall()

def yelp_call(headers, url):
    response = requests.get(url, headers=headers)
    data = response.json()
    return data['reviews']

def parse_data(reviews, business_id):
    review_list = []

    for review in reviews:
        review_tuple = (review['id'], business_id, review['text'], review['time_created'])
        review_list.append(review_tuple)
    return review_list

def db_insert(cnx, cursor, parsed_results):
    add_business = ("""INSERT INTO yelp_reviews
               (review_id, business_id, reviews, time_created)
               VALUES (%s, %s, %s, %s)""")
    cursor.executemany(add_business, parsed_results)
    cnx.commit()
    print('Good job!')

def review_etl(id_list):
    for id in id_list:
        url = 'https://api.yelp.com/v3/businesses/' + id[0] + '/reviews'
        reviews = yelp_call(headers, url)
        parsed_results = parse_data(reviews, id[0])
        db_insert(cnx, cursor, parsed_results)


#review_etl(data)

#paginate(url_params, headers, url)
