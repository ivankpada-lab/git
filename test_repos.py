import os
import requests
from dotenv import load_dotenv

load_dotenv()
cle = os.getenv("GITHUB_TOKEN")

url = "https://api.github.com/users/ivankpada-lab/repos"
headers = {"Authorization": "Bearer " + cle}

try:
    reponse = requests.get(url, headers=headers)
    if reponse.status_code == 200:
        repos = reponse.json()
        for depot in repos:
            print(depot["name"], depot["language"])
    else:
        print("Echec de la requete, code :", reponse.status_code)
except requests.exceptions.ConnectionError:
    print("Erreur de connexion")