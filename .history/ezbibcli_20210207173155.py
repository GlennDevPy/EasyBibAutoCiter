import requests
headers = {
    "X-AlCell": "change-refresh-holdout-70-test",
    "Authorization": "Bearer anuZaem3ChaichuGhoh8gaiNeequee",
    "Origin": "https://www.easybib.com",
    "Referer": "https://www.easybib.com",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Safari/537.36",
    ""
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