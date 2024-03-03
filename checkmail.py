import requests
from termcolor import colored
from gtts import gTTS
from playsound import playsound
import os

# Remplacez 'VOTRE_CLE_API' par votre clé API Hunter réelle
API_KEY = ''
EMAIL_A_TESTER = input("Veuillez entrer l'adresse e-mail à tester : ")

def annoncer_resultat(texte, est_valide):
    tts = gTTS(text=texte, lang='fr')
    fichier_temp = "resultat.mp3"
    tts.save(fichier_temp)
    playsound(fichier_temp)
    if est_valide:
        print(colored(texte, "green"))
    else:
        print(colored(texte, "red"))
    os.remove(fichier_temp)

def verifier_email_hunter(email):
    url = f"https://api.hunter.io/v2/email-verifier?email={email}&api_key={API_KEY}"
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        status = data['data']['status']
        score = data['data']['score']
        if status == "valid":
            texte = f"L'adresse e-mail '{email}' est valide. Score: {score}%"
            annoncer_resultat(texte, True)
        else:
            texte = f"L'adresse e-mail '{email}' n'est pas valide. Score: {score}%"
            annoncer_resultat(texte, False)
    else:
        texte = "Erreur lors de la vérification de l'e-mail. Veuillez vérifier votre clé API et réessayer."
        annoncer_resultat(texte, False)

verifier_email_hunter(EMAIL_A_TESTER)
