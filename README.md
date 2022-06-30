# Algorithmes de Scorings
*By Kyllian BEGUIN, Bramly MBAKOP, Yaël GALESNE, Baptiste THIOLLIER*
## Avant propos  
Nous avons développé cet algorithme durant le Hackathon organisé par l'école "Sup de Vinci", du 27/06/2022 au 01/07/2022.  
Cet algorithme n'a pas pour objectif d'affirmer si une information est fausse. Il permet néanmoins d'estimer sa motivation à véhiculer une information de façon claire.  
## Comment l'algorithme fonctionne ?
**DISCLAIMER : À L'HEURE ACTUELLE, LES ALGORITHMES DE COHÉRENCE ET AUTEUR SONT À RÉALISER**  
Nous construisons un score à partir d'une information.  
Ce score est construit en 3 parties :
* Vocabulaire
* Cohérence
* Auteur
## Pré-requis
* Python 3.8 minimum
* installer les bibliothèques utilisées : `pip install - requirements.txt'`
## Comment utiliser l'algorithme ?
Il suffit de lancer la commande :  
`python3 scoring_vocabulaire.py 'VOTRE_TEXTE'`  
Si vous souhaitez analyser un article comme celui-ci ([lien](https://www.wikistrike.com/2022/06/la-baisse-de-la-fertilite-chez-les-vaccines-est-de-plus-en-plus-probable.html)), changez la variable VOTRE_TEXTE par votre lien :  
`python3 scoring_vocabulaire.py 'https://www.wikistrike.com/2022/06/la-baisse-de-la-fertilite-chez-les-vaccines-est-de-plus-en-plus-probable.html'`  
## Logs
30/06/2022 : Nous mettons l'algorithme d'analyse du vocabulaire à disposition de quiconque souhaiterais analyser un texte ou un site dont la source est disponible dans notre tableau de forage et à jour.
