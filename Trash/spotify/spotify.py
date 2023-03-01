import csv
import json

file_name = 'spotify/spotify.csv'
json_file_name = 'spotify/songs.json'

songs_list = []

with open(file_name, 'r', encoding='UTF8') as data_file:
    for line in csv.DictReader(data_file):
        songs_list.append(line)

with open(json_file_name, 'w', encoding='UTF8') as json_file:
    json.dump(songs_list, json_file, indent=4)

#Lai programma izvada terminālī tikai dziesmas nosaukumu

for song in songs_list:
    print(f"{song['Title']} {song['Popularity']}")

#Izveido sarakstu ar unikāliem dziesmas gadiem
for song in songs_list:
    print (song,['Year'])

song_years = []
song_genres = []
for song in songs_list:
    if song['Year'] not in song_years:
        song_years.append(song['Years'])
    if song['Genred'] not in song_genres:
        song_genres.append(song['Genres'])

song_years.sort()
print(song_years)
print(song_genres)