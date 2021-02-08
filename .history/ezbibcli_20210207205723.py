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
    l1 = 'https://www.watertechonline.com/wastewater/article/15547113/what-chemicals-are-used-and-controlled-in-primary-industrial-wastewater-treatment'
    singlelink = f"https://autocite.citation-api.com/api/v3/query?url={l1}"
    singler = s.get(singlelink, headers=headersMain, timeout=3)
    try:
        score = re.search('score\":(.*?),', singler.text)[1]
    except:
        score = 'Missing'

    try:
        title = re.search('title\":\"(.*?)\"', singler.text)[1]
    except:
        title = 'Missing'

    try:
        webtitle = re.search('_mediumTitle\":\"(.*?)\"', singler.text)[1]
    except:
        webtitle = 'Missing'

    try:
        authorF = re.search('given\":\"(.*?)\"', singler.text)[1]
    except:
        authorF = 'Missing'

    try:
        authorL = re.search('family\":\"(.*?)\"', singler.text)[1]
    except:
        authorL = 'Missing'


    dD = re.search('_publishedDay\":\"(.*?)\"', singler.text)[1]
    if dD == '':
        dD = "Missing"


    dM = re.search('_publishedMonth\":\"(.*?)\"', singler.text)[1]
    if dM == '':
        dM = "Missing"


    dY = re.search('_publishedYear\":\"(.*?)\"', singler.text)[1]
    if dY == '':
        dY = "Missing"

    checklist = {
        "title": title,
        "webtitle": webtitle,
        "authorF": authorF,
        "authorL": authorL,
        "dD": dD,
        "dM": dM,
        "dY": dY,
    }

    tocheck = ['mediumTitleFound', 'contentTitleFound', 'contributorsFound', 'publishedDayFound', 'publishedMonthFound', 'publishedYearFound']
    #medtitle is website title
    if score == "100":
        if safeM is True:
            #check 1 by 1 for if in the dict - and ask is it okay? if not fill in if yes continue
            #make cite
            pass
        else:
            pass
            #make citeation
    else:
        check = []
        for plz in tocheck:
            xPlz = re.search(f'{plz}\":(.*?),\"', singler.text)[1]
            if xPlz == "0":
                check.append(plz)
            else:
                pass
        
        print(f"\nCurrent Citation Progress:\n{checklist}\n")
        if "mediumTitleFound" in check:
            print("Website Title?")
            webtitle = input()
        if "contentTitleFound" in check:
            print("Article Title?")
            title = input()
        if "contributorsFound" in check:
            print("Author First Name?")
            authorF = input()
            print("Authors Last Name?")
            authorL = input()
        if "publishedDayFound" in check:
            print("Published Day?")
            dD = input()
        if "publishedMonthFound" in check:
            print("Published Month?")
            dM = input()
        if "publishedYearFound" in check:
            print("Published Year?")
            dY = input()
        
        checklist = {
        "title": title,
        "webtitle": webtitle,
        "authorF": authorF,
        "authorL": authorL,
        "dD": dD,
        "dM": dM,
        "dY": dY,
        }       
        print(f"\nUpdated Citations:\n{checklist}\n")
        print("Do you want to make any edits? (Y or N)")
        cedits = input()
        if cedits.upper() == "Y":
            print("\nTo which section? (non case sensitive but spelling sensitive)")
            section 
        else:
        #convert to cite

print("Welcome to EZBibCiter [beta]")
print("[1] Textfile\n[2] Single Link\n[3] Enter Links Manually")
choice = input()

if choice == "1":
    #textfile()
    print("\nSafe Mode? (Y or N)")
    safe = input()
    if safe.upper() == "Y":
        safeM = True
    else:
        safeM = False
    pass

if choice == "2":
    print("\nSafe Mode? (Y or N)")
    safe = input()
    if safe.upper() == "Y":
        safeM = True
    else:
        safeM = False
    singleL()

if choice == "3":
    #manual()
    print("\nSafe Mode? (Y or N)")
    safe = input()
    if safe.upper() == "Y":
        safeM = True
    else:
        safeM = False
    pass
