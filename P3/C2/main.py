import requests
import re

from bs4 import BeautifulSoup

with open("P3/C2/index.html", "r", encoding="utf-8") as file:
    page_content = file.read()

soup = BeautifulSoup(page_content, 'html.parser')

title = soup.find("title")
h1 = soup.find("h1")

print(title.text)
print(h1.text)

produits = soup.find_all("li")

for produit in produits:
    nom = produit.find("h2").text
    prix = produit.find("p").text
    description = produit.find_all("p")[1].text

    prix_entier = re.findall(r'\d+', prix)
    prix_entier = [int(nombre)*1.2 for nombre in prix_entier]

    print(f"Nom du produit : {nom}")
    print(f"Prix du produit : {prix_entier}")
    print(f"Description du produit : {description}")
    print()



