import urllib2, urllib, json
baseurl = "https://query.yahooapis.com/v1/public/yql?"
place=raw_input ("Enter the location\n")
x=str(place)
k=0
print "your choice of location for weather forecasting is "+x
yql_query = '''select * from weather.forecast where woeid in (select woeid from geo.places(1) where text=" '''+x+''' ")'''
yql_url = baseurl + urllib.urlencode({'q':yql_query}) + "&format=json"
print "Retrieving data from ",yql_url
result = urllib2.urlopen(yql_url).read()
data = json.loads(result)
info=json.dumps(data,indent=4)
#print info
print data["query"]["results"]["channel"]["description"] 
#print " Forecasted temperature for next few days in "+x+" is:"
while k<=8:
    z=((int(data["query"]["results"]["channel"]["item"]["forecast"][k]["high"])-32)*5)/9
    y=((int(data["query"]["results"]["channel"]["item"]["forecast"][k]["low"])-32)*5)/9
    i=data["query"]["results"]["channel"]["item"]["forecast"][k]["date"]
    conditions=data["query"]["results"]["channel"]["item"]["forecast"][k]["text"]
    print "Date:",i                                                           
    print "Maximum:", z
    print "Minimum:", y
    print "Conditions:",conditions
    k=k+1
