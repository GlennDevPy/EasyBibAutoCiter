import requests
import json
import re

safeM = True

headersMain = {
    "X-AlCell": "change-refresh-holdout-70-test",
    "Authorization": "Bearer anuZaem3ChaichuGhoh8gaiNeequee",
    "Origin": "https://www.easybib.com",
    "Referer": "https://www.easybib.com",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Safari/537.36",
    "Accept": "application/vnd.com.easybib.data+json",
    "Sec-GPC": "1"
}
s = requests.Session()


def createProj():
    cP = "https://bff.writing.chegg.com/graphql"
    headersCP = {
        "accept": "*/*",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.146 Safari/537.36",
        "content-type": "application/json",
        "Referer": "https://www.easybib.com/",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJjbGllbnQiOiJjZmUiLCJzaXRlIjoiZWFzeWJpYiIsImNoZWdnQWNjZXNzIjpbXSwiY2hlZ2dUb2tlbnMiOnsiYWNjZXNzX3Rva2VuIjpudWxsLCJpZF90b2tlbiI6bnVsbH0sInBhaWRNZW1iZXIiOmZhbHNlLCJ1c2VyX3JvbGUiOiJub3RfbG9nZ2VkX2luIiwiZW1haWwiOm51bGwsInNlc3Npb25JZCI6IjljODQ5cmJsbGVmb2VrcDZraDVjYjRpa3Y0IiwiY2hlZ2dVc2VyVXVpZCI6bnVsbCwiZXhwIjoxNjEyNzczNzA4fQ.Gxvf11kbzmhrC75u19IKSOEiGVg1hBTPxQ0esAPNZwQ",
        "Sec-GPC": "1",
        "Origin": "https://www.easybib.com"
    }
    data = {"operationName":"FoldersCreateProject","variables":{"folderId":None,"name":"EZBibCiter","defaultStyle":"mla8","public":True},"query":"mutation FoldersCreateProject($name: String!, $public: Boolean!, $defaultStyle: String!, $folderId: Int = null) {\n  createProject(name: $name, public: $public, defaultStyle: $defaultStyle, folderId: $folderId) {\n    id\n    name\n    defaultStyle\n    date: updatedAt\n    public\n    __typename\n  }\n}\n"}
    cPR = s.post(cP, headers=headersCP, data=json.dumps(data))
    ped = json.loads(cPR.text)
    bruh = (ped['data']['createProject']['id'])
    return bruh

def singleL():
    #projID = createProj()
    #print("Enter in the link to cite")
    #l1 = input()
    l1 = 'https://www.nytimes.com/2021/01/24/health/fauci-trump-covid.html?smid=tw-nytimes&smtyp=cur'
    singlelink = f"https://autocite.citation-api.com/api/v3/query?url={l1}"
    singler = s.get(singlelink, headers=headersMain, timeout=3)
    checklist = {
        "title": title
    }
    try:
        score = re.search('score\":(.*?),', singler.text)[1]
    except:
        score = 'EDIT'

    try:
        title = re.search('title\":\"(.*?)\"', singler.text)[1]
    except:
        title = 'EDIT'

    try:
        webtitle = re.search('publisher\":\"(.*?)\",', singler.text)[1]
    except:
        webtitle = 'EDIT'

    try:
        authorF = re.search('given\":\"(.*?)\"', singler.text)[1]
    except:
        authorF = 'EDIT'

    try:
        authorL = re.search('family\":\"(.*?)\"', singler.text)[1]
    except:
        authorL = 'EDIT'

    try:
        fDate = re.search('issued\":{\"date-parts\":\[\[\"(.*?)\"]]}', singler.text)[1]
    except:
        fDate = 'EDIT'

    checklist = {
        "title": title,
        "websitetitle": webtitle,
        "authorF": authorF,
        "authorL": authorL,
        "dD": dD,
        "dM": dM,
        "dY": dY,
    }
    print(score)
    if score == "100":
        if safeM is True:
            #check 1 by 1 frin the dict - and ask is it okay? if not fill in if yes continue
            #make cite
            pass
        else:
            pass
            #make citeation
    else:
        #check which ones are 0 for the XXXFound
        #prompt user to fill in        


singleL()
""" 

print("Welcome to EZBibCiter [beta]")
print("[1] Textfile\n[2] Single Link\n[3] Enter Links Manually")
choice = input()
if choice == "1":
    #textfile()
    print("\n Safe Mode? (Y or N)")
    safe = input()
    if safe.upper() == "Y":
        safeM = True
    else:
        safeM = False
    pass
if choice == "2":
    singleL()
    print("\n Safe Mode? (Y or N)")
    safe = input()
    if safe.upper() == "Y":
        safeM = True
    else:
        safeM = False
if choice == "3":
    #manual()
    print("\n Safe Mode? (Y or N)")
    safe = input()
    if safe.upper() == "Y":
        safeM = True
    else:
        safeM = False
    pass """