# ZONE D'IMPORT DES LIBRAIRIES -------------------------------------------------
# Système
import sys
# Scraping et compréhension du code html
import requests
from bs4 import BeautifulSoup
# Comptage
from collections import Counter
# Processing des données
import pandas as pd

# ZONE D'INGESTION DES ENTRANTS ------------------------------------------------
# 1. Mots puissants
f = open("mots_puissants.txt", "r")
mots_puissants_raw = f.read().split(', ')
mots_puissants = [mots_puissants_raw[i].lower() for i in range(len(mots_puissants_raw))]

# 2. Information
info = sys.argv[1]

# ZONE DE CRÉATION DES FONCTIONS -----------------------------------------------
def extract_content(info):

  if 'http' in info[:5]:

    # Initialisation
    domaine = info.split("/")[2]
    df = pd.read_csv('forage_sites.csv')

    r = requests.get(info)
    soup = BeautifulSoup(r.text, 'html.parser')

    forage_cible = df[df['site'] == domaine]
    to_find = list(forage_cible['to_find'])[0]
    attr_1 = list(forage_cible['attr_1'])[0]
    attr_2 = list(forage_cible['attr_2'])[0]

    texte_raw = soup.findAll(to_find, attrs = {attr_1 : attr_2})
    texte_liste = [texte_raw[num_paragraphe].getText() for num_paragraphe in range(len(texte_raw))]
    texte = '. '.join(texte_liste)

  else:
    texte = info
  
  return texte

def Cleaning_content(content):

  content_dblDots = content.replace('..', '.')
  content_lower = content_dblDots.lower()
  content_clean = content_lower.split('. ')

  return content_clean

def Scoring_vocabulaire(content, mots):

  Score_mots = 0
  Increment_mots = 1
  Score_ez = 0
  Increment_ez = 2

  Score_vocabulaire = 0

  mots_detectes = []
  mots_ez = []

  for num_phrase in range(len(content)):
    phrase = content[num_phrase]

    for num_mot in range(len(mots)):
      mot_puissant = mots[num_mot]

      if mot_puissant in phrase:
        Score_mots += Increment_mots
        mots_detectes.append(mot_puissant)
  
    # Test d'impératif = ez-vous / ez-nous
    premier_mot = phrase.split(' ')[0].split('-')[0]
    if 'ez' in premier_mot[-3:] and 'chez' not in premier_mot:
      Score_ez += Increment_ez
      mots_ez.append(premier_mot)
  
  Score_vocabulaire = Score_ez + Score_mots

  comptages_md = list(dict(Counter(mots_detectes)).items())

  Scoring_dict = {"Score_vocabulaire" : Score_vocabulaire,
                  "Score_mots" : Score_mots,
                  "Score_mots_detail" :comptages_md,
                  "Score_ez" : Score_ez,
                  "Score_ez_details" : mots_ez}
  return Scoring_dict

# ZONE MAIN --------------------------------------------------------------------
texte = extract_content(info)
texte_clean = Cleaning_content(texte)
Scoring_voc = Scoring_vocabulaire(texte_clean, mots_puissants)

print(Scoring_voc)
