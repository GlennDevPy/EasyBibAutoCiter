import requests

def singleL():
    print("Enter in the link to cite")
    singlelink = input(0
    )




print("Welcome to EZBibCiter [beta]")
print("[1] Textfile\n[2] Single Link\n[3] Enter Links Manually")
choice = input()
if choice == "1":
    textfile()
if choice == "2":
    singleL()
if choice == "3":
    manual()