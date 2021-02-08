import requests
import json
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
    projID = createProj()
    print("Enter in the link to cite")
    l1 = input()
    singlelink = f"https://autocite.citation-api.com/api/v3/query?url={l1}"
    singler = s.get(singlelink, headers=headersMain, timeout=3)
    sing = json.loads(singler.text)
    score = sing['results']['{}']['metrics']['score']    
    print(score)
    #parse data
    #see what im missing
    #then ask
    #then cite

singleL()
""" 

print("Welcome to EZBibCiter [beta]")
print("[1] Textfile\n[2] Single Link\n[3] Enter Links Manually")
choice = input()
if choice == "1":
    #textfile()
    pass
if choice == "2":
    singleL()
if choice == "3":
    #manual()
    pass """