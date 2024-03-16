import requests
import json



#This program was written for the APCSP create task. This submission was created on replit and is posted here https://replit.com/@BhavyaPatel32/Song-Art-Getter?v=1
#JSON handling, used from https://www.dataquest.io/blog/python-api-tutorial/

def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

def colorPrint(lst):
  for i in range(len(links)):
    print("\x1b[34mLink " + str(i) + ": \x1b[0;35m" + links[i]+ "\n")



#Introduction
print("This is a song art getter. 1000x1000 quality images are returned in the form of hyperlinks. Click them to be directed to your image!")
#input
artist = input("Type the song you wish to search: ")

#API access taken from rapid API, used Deezer API, keys linked to my account with email patelbh@htps.us
querystring = {"q":artist}
url = "https://deezerdevs-deezer.p.rapidapi.com/search"
#connecting to API
headers = {
	"X-RapidAPI-Key": "7999e95164mshf9d91b106250c5bp18f182jsn0866d90cd647",
	"X-RapidAPI-Host": "deezerdevs-deezer.p.rapidapi.com"
}
#data request from API and assinging that to a variable
response = requests.request("GET", url, headers=headers, params=querystring)
#loading JSON into usable python format
data = json.loads(response.text)
#test statments below
#print(response.text)
#jprint(response.json())
#print(type(response.json()))

#JSON testing, writing JSON to a json file for analysis and debugging as well as seeing full information recieved by the API. Code to write to JSON file from https://www.geeksforgeeks.org/reading-and-writing-json-to-a-file-in-python/ 
json_object = json.dumps(response.json(), indent=4)
with open("output.json", "w") as outfile:
    outfile.write(json_object)


#Testing printing
#tracksOnly = {}
#sum
#print("Title: "+data["data"][0]["title"])
#print("Duration: " + str(data["data"][0]["duration"]))
#print("Explicit Lyrics?: "+str(data["data"][0]["explicit_lyrics"]))

#initializing a list that holds the links of the images
links = []
#iterating through the data to get the links
for i in range(len(data["data"])):
  #the API returns other types of images such as pictures and in different sizes, therefore, trying to see if the index contains data for "cover_xl", and if it does, append that value of the key cover_xl to the list called links
  try:
    links.append(data["data"][i]["album"]["cover_xl"])
    #if there isn't a link, ignore it.
  except:
    pass

if len(links) != 0:
  #if there are links, call on colorPrint to fancify the links so they look kool.
  print("\nHere are links for every result found: ")
  colorPrint(links)
else:
  #if there are no links, tell user that there aren't any links
  print("Sorry, no results found for that song. Please rerun the program!")