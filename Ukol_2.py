#Cast_1: Vyhledej informace o konkrétním subjektu na základě jeho identifikačního čísla (IČO)

import requests

ICO = input("Zadej identifikační číslo subjektu (IČO): ")


try:
    response = requests.get(f"https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/{ICO}")
    #response = requests.get("https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/" + ICO)
    data = response.json()
    name = data["obchodniJmeno"]
    address = data["sidlo"]["textovaAdresa"]
    print(name)
    print(address)

except Exception:
   print("Zadané IČO neexistuje.")

#Cast_2: Hledání podle názvu subjektu
import requests

nazev_subjektu = input("Zadej název subjektu: ")

headers = {
    "accept": "application/json",
    "Content-Type": "application/json",
}
data = {"obchodniJmeno": nazev_subjektu}
try:
    res = requests.post("https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/vyhledat", 
                    headers=headers, json=data)

    response = res.json()

    print(f"Nalezeno subjektů: {response['pocetCelkem']}")

    for subjekt in response["ekonomickeSubjekty"]:
        # .get() prevents KeyError if a rare record is missing a field
        jmeno = subjekt.get("obchodniJmeno", "N/A")
        ico   = subjekt.get("ico", "N/A")
        print(f"{jmeno}, {ico}")

except Exception:
    print("Zadaný název neexistuje.")
