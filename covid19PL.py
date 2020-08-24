import json,urllib.request
token = "TUTAJ_TOKEN"
req = urllib.request.Request(url=f"https://www.dbanaszewski.com/api/covid/?token={token}")
data = urllib.request.urlopen(req).read()
output = json.loads(data)
ilosckoronawirusow = output["all_infected"]
iloscnowa = output["infected"]
deaths = output["all_death"]
deathstoday = output["death"]
today = output["date"]
print(f"Statystyki na dzień {today}:")
print(f"  - ilość aktywnych koronawirusów wynosi {ilosckoronawirusow}, przybyło nowych {iloscnowa} koronawirusów w Polsce.")
print(f"  - nie żyje już {deaths} osób, dzisiaj zmarło {deathstoday}.")
