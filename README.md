# Generate_SEOTitle_with_Youtube
Exploiter les titres de Youtube pour créer des titres optimisés SEO

## Au préalable 

Vous aurez besoin d'une clé API, que vous pourrez générer en ayant un compte Google et en vous rendant sur la [Google Developers Console](https://console.developers.google.com)

Activez Youtube Data V3, puis faites une demande de clé. Cette clé remplacera __api_key_access__ dans notre script.

## Fonctionnement 

À partir d'un mot, ce script vous ressort la liste des X premières vidéos de Youtube
Je conseille de partir sur des recherches étrangères, ne sachant pas si Google indexe le titre des vidéos sur la SERP
Une étape de traduction sera à appliquer , script à venir !

## Optimisation 

Le script était de base fait pour effectuer plusieurs requêtes, je l'ai ici réarranger pour rendre sa compréhension accessible
N'hésitez à boucler sur une liste de keywords pour avoir beaucoup plus de résultats
Google applique des cotas de requête mais il est possible de passer au travers en créant plusieurs compte google et donc plusieurs clés API.
Ne soyez pas trop gourmand si vous souhaitez obtenir de bonne quantités de données et n'oubliez surtout pas de bien enregistré vos datas à chaque requête pour éviter de perdre tout votre travail.