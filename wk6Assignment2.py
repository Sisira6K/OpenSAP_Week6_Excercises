import requests
word = input("Please enter a search term:")
url =  "https://itunes.apple.com/search?term="+ word+"&entity=album"
response = requests.get(url)
r = response.json()
value = r["resultCount"]
print("The search returned", value,"results.")
result = r["results"]
for i in result:
    artist = i["artistName"]
    album = i["collectionName"]
    trackcount = i["trackCount"]
    print("Artist:", artist,"- Album:", album, "- Track Count:", trackcount)