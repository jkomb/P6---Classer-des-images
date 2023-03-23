# P6---Classer-des-images-de-chien
Une association vous demande de réaliser un algorithme de détection de la race du chien sur une photo, 
afin d'accélérer leur travail d’indexation.

Vous avez peu d’expérience sur le sujet, vous décidez donc de contacter un ami expert en classification d’images.

Il vous conseille dans un premier temps de pré-processer des images avec des techniques spécifiques 
(e.g. whitening, equalization, éventuellement modification de la taille des images) et de réaliser 
de la data augmentation (mirroring, cropping...).

Ensuite, il vous incite à mettre en œuvre deux approches s’appuyant sur l’état de l’art et l’utilisation de CNN 
(réseaux de neurones convolutionnels), que vous comparerez en termes de temps de traitement et de résultat :

Une première en réalisant votre propre réseau CNN, en vous inspirant de réseaux CNN existants. 
Prenez soin d'optimiser certains hyperparamètres (des layers du modèle, de la compilation du modèle et de l’exécution du modèle)


Une deuxième en utilisant le transfer learning, c’est-à-dire en utilisant un réseau déjà entraîné, et en le modifiant 
pour répondre à votre problème.

Pour lancer l'application, il est nécessaire de créer un nouvel environnement virtuel et d'installer l'ensemble des librairies
requises pour le projet à l'aide de la commande :
```pip install -r requrements.txt```

Après avoir activé votre nouvel environnement virtuel, changez de répertoire vers celui de l'application 
(dossier 'Application_streamlit')

Depuis la ligne de commande, exécuter la commande suivante pour lancer l'application dans votre navigateur par défaut :
```streamlit run main.py```
