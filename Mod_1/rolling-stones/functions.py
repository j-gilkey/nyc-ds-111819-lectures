def find_by_name(our_data,name):
    for album in our_data:
        if album['album'] == name:
            return album
    return None


def find_by_name(our_data,name):
    for album in our_data:
        if album['album'] == name:
            return album
    return None


def find_by_rank(our_data,rank):
    for album in our_data:
        if album['number'] == str(rank):
            return album
    return None

def find_by_year(our_data,year):
    return [album for album in our_data if album['number'] == str(year)]

def multiple_years(our_data, start, end):
    count = start
    album_list = []
    while count <= end:
        album_list.append(find_by_year(our_data,count))
        count += 1

def multiple_ranks(our_data,start, end):
    count = start
    album_list = []
    while count <= end:
        album_list.append(find_by_rank(count))
        count += 1

def all_titles(our_data):
    return [album['album'] for album in our_data]

def all_artists(our_data):
    return [album['artist'] for album in our_data]

def most_popular_artist(our_data):
    counter_dict = {}
    for artist in all_artists(our_data):
        if artist in counter_dict:
            counter_dict[artist] += 1
        else:
            counter_dict[artist] = 1
    maximum_albums = max(counter_dict.values())
    artist_lists = []
    for keys, values in counter_dict.items():
        if values == maximum_albums:
            artist_lists.append(keys)
    return artist_lists


def histogram_decades(our_data):
    decade_dict = {}
    for album in our_data:
        decade = int(album['year'])//10
        if decade in decade_dict:
            decade_dict[decade] += 1
        else:
            decade_dict[decade] = 1
    return decade_dict

def histogram_genres(our_data):
    genre_list = []
    for album in our_data:
        genre_list.extend(genre.strip() for genre in album['genre'].split(','))
    genre_dict = {}
    for genre in genre_list:
        if genre in genre_dict:
            genre_dict[genre] += 1
        else:
            genre_dict[genre] = 1
    return genre_dict

def file_splitter(splitting_device):
    return [line.strip().split(splitting_device) for line in lines]

def song_dict_maker(songs):
    output_list = []
    for song in songs:
        new_dict = {}
        new_dict['rank'] = song[0]
        new_dict['song'] = song[1]
        new_dict['artist'] = song[2]
        new_dict['year'] = song[3]
        output_list.append(new_dict)
    return output_list

def track_cleaner(data):
    copy_data = data.copy()
    for idx, album in enumerate(data):
        copy_data[idx]['tracks'] = list({track.split('-')[0].strip() for track in album['tracks']})
    return copy_data

def album_with_most_top_songs(song_dict,album_song_file):
    album_popularity_dict = {}
    for song in song_dict:
        for album in album_song_file:
            if song['song'] in album['tracks']:
                if album['album'] in album_popularity_dict:
                    album_popularity_dict[album['album']] += 1
                else:
                    album_popularity_dict[album['album']] = 1
#     print(album_popularity_dict)
    print(album_popularity_dict)
    most_pop_album_num = max(album_popularity_dict.values())

#     for keys, values in album_popularity_dict.items():
#         if values == most_pop_album_num:

    return [keys for keys, values in album_popularity_dict.items() if values == most_pop_album_num]

def album_with_top_songs(our_data,song_dict,album_song_file):
    albums_with_popular_songs = []
    for song in song_dict:
        for album in album_song_file:
            if song['song'] in album['tracks']:
                albums_with_popular_songs.append(album['album'])

    ultimate_album_list = []
    for album in albums_with_popular_songs:
        for top_albums in all_titles(our_data):
            if album in top_albums:
                ultimate_album_list.append(album)

    return list(set(ultimate_album_list))

def songs_on_top_albums(top_albums,album_song_file):
    set_titles = set(all_titles(top_albums))
    song_list = []
    for album in album_song_file:
        if album['album'] in set_titles:
            song_list.extend(album['tracks'])
    return song_list

def top_10_albums_by_songs(song_dict,album_song_file):
    album_popularity_dict = {}
    for song in song_dict:
        for album in album_song_file:
            if song['song'] in album['tracks']:
                if album['album'] in album_popularity_dict:
                    album_popularity_dict[album['album']] += 1
                else:
                    album_popularity_dict[album['album']] = 1
#     print(album_popularity_dict)
    sorted_by_value = sorted(album_popularity_dict.items(), key=lambda kv: kv[1],reverse=True)
    num_top_songs_on_album = {a:b for a,b in sorted_by_value[:10]}
    return iplot([{'type':'bar','x':list(num_top_songs_on_album.keys()),'y':list(num_top_songs_on_album.values())}])

from collections import Counter
def top_overall_artist(album_data,song_data):
    artist_album_count = Counter(all_artists(album_data))
    artist_song_count = Counter(all_artists(song_data))
#     print(artist_song_count)
#     print(artist_album_count)
    for artist in artist_album_count:
        if artist in artist_song_count:
            artist_song_count[artist] += artist_album_count[artist]
        else:
            artist_song_count[artist] = artist_album_count[artist]

    maximum_agg = max(artist_song_count.values())
#     print(maximum_agg)
    lst = []
    for key, value in artist_song_count.items():
        if value == maximum_agg:
            lst.append(key)
    return lst
