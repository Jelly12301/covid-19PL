import json,urllib.request
data = urllib.request.urlopen("https://api.covid19api.com/dayone/country/poland").read()
output = json.loads(data)
ilosckoronawirusow = output[len(output) - 1]["Confirmed"]
koronawirusydata = output[len(output) - 1]["Date"]
iloscnowa = output[len(output) - 1]["Confirmed"] - output[len(output) - 2]["Confirmed"]
print("W dniu", koronawirusydata, "ilość aktywnych koronawirusów wynosi", ilosckoronawirusow, "przybyło nowych", iloscnowa, "koronawirusów w Polsce.")
