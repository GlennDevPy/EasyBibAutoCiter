import requests
headers = {
    "X-AlCell": "change-refresh-holdout-70-test",
    "Authorization": "Bearer anuZaem3ChaichuGhoh8gaiNeequee",
    
}
s = requests.Session()
def singleL():
    print("Enter in the link to cite")
    l1 = input()
    singlelink = f"https://autocite.citation-api.com/api/v3/query?url={l1}"




print("Welcome to EZBibCiter [beta]")
print("[1] Textfile\n[2] Single Link\n[3] Enter Links Manually")
choice = input()
if choice == "1":
    textfile()
if choice == "2":
    singleL()
if choice == "3":
    manual()