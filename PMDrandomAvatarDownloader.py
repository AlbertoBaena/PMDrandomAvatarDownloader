import pypokedex, random, requests

n = int(random.uniform(1,493))


url = "https://www.serebii.net/dungeonsky/headshot/" + str(n) + ".png"
r = requests.get(url)
if(r.status_code != 404): 
    print("Downloading " + str(n) + " (" + pypokedex.get(dex=n).name + ")")
    open(str(n) + "-" + pypokedex.get(dex=n).name + ".png", 'wb').write(r.content)