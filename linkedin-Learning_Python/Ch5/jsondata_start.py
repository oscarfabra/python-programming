# 
# Example file for parsing and processing JSON
#
import urllib.request 
import json

def printResults(data):
  # Use the json module to load the string data into a dictionary
  the_JSON = json.loads(data)
  
  # now we can access the contents of the JSON like any other Python object
  if "title" in the_JSON["metadata"]:
    print(the_JSON["metadata"]["title"])
  
  # output the number of events, plus the magnitude and each event name  
  count = the_JSON["metadata"]["count"]
  print(str(count) + " events recorded")

  # for each event, print the place where it occurred
  for feature in the_JSON["features"]:
    print(feature["properties"]["place"])
  print("------------\n")

  # print the events that only have a magnitude greater than 4
  for feature in the_JSON["features"]:
    if feature["properties"]["mag"] >= 4.0:
      print("%2.1f" % feature["properties"]["mag"], feature["properties"]["place"])
  print("------------\n")
  
  # print only the events where at least 1 person reported feeling something
  print("Events that were felt:")
  for feature in the_JSON["features"]:
    felt_reports = feature["properties"]["felt"]
    if felt_reports != None and felt_reports > 0:
      print("%2.1f" % feature["properties"]["mag"], feature["properties"]["place"], "reported " + str(felt_reports) + " times")
  print("------------\n")
  
def main():
  # define a variable to hold the source URL
  # In this case we'll use the free data feed from the USGS
  # This feed lists all earthquakes for the last day larger than Mag 2.5
  url_data = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"

  # Open the URL and read the data
  web_url = urllib.request.urlopen(url_data)
  print ("Result code: " + str(web_url.getcode()))
  if(web_url.getcode() == 200):
    data = web_url.read()
    printResults(data)
  else:
    print("Received error, cannot parse results")

if __name__ == "__main__":
  main()
