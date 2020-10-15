import json,urllib.request
req = urllib.request.Request(url="https://nowywirus.pl/api/", headers={'User-Agent':' Mozilla/5.0 (Windows NT 6.1; WOW64; rv:12.0) Gecko/20100101 Firefox/12.0'})
data = urllib.request.urlopen(req).read()
output = json.loads(data)
cases = output[0]["cases"]
new_cases = output[0]["new_cases"]
deaths = output[0]["deaths"]
new_deaths = output[0]["new_deaths"]
print("Aktualne dane o covid-19 w polsce.")
print(f"Ilość potwierdzonych przypadków: {cases}.")
print(f"Ilość nowych zakażeń: {new_cases}.")
print(f"Zgony: {deaths}.")
print(f"Nowe zgony: {new_deaths}.")