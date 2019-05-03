import requests #beautiful soup 4 ###pip install bs4

head = {"User-agent": "windows 98", "Referer": "Heheheheh", "CDN-LOOP": "Dont hack me plz"}
#mcookies = {"gzuis":"yasduifadvbzxcjvuio    wçbhffsadfsakdf"}
dices = {"meunome":"Rynan", "pasenha":"asuasudsafa"}


req=None
try:
    req = requests.post("https://putsreq.com/4Gv4AhDhSn6VSV4acKqm", headers=head,data=dices)
    #print(type(req))
    #print(req)
    print(req.text)
except Exception as e:
    print("nao deu meu irmao", e)