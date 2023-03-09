__doc__ = """
    Ce module contient la définition des variables de chemins de destination ainsi que 
        l'importation des librairies nécessaires à la définition des 2 fonctions suivantes:
        
    - fetch_dogs_data() : qui sert à télécharger dans un sous-dossier du dossier de travail, 'images', 
        l'ensemble des images de la librairie 'Stanford Dogs Dataset'
        
    - load_dogs_data() : qui sert à charger les noms des images de chien, leur chemin d'accès ainsi que leur race dans un DataFrame
"""

import os
import urllib
import tarfile
import pandas as pd

DOWNLOAD_URL = "http://vision.stanford.edu/aditya86/ImageNetDogs/images.tar"
TAR_NAME = "images.tar"
DATA_PATH = "datas"
IMG_PATH = "datas/Images"
TAR_PATH = os.path.join(DATA_PATH, TAR_NAME)

def fetch_dogs_data(data_path=DATA_PATH, dwnld_url=DOWNLOAD_URL, tar_path=TAR_PATH):

    """
        fonction d'extraction des données depuis 'Stanford Dogs Dataset'
    """

    if not os.path.isdir(data_path):
        os.makedirs(data_path)
    urllib.request.urlretrieve(dwnld_url, tar_path)

    with tarfile.TarFile(tar_path, mode="r") as archive:
        archive.extractall(data_path)

    os.remove(tar_path)

def load_dogs_data(img_path=IMG_PATH):

    """
        fonction de création d'un dataframe associant noms d'image, chemin d'accès à l'image et races de chiens
    """
    dict_breed = dict()
    df_breed = pd.DataFrame(columns=['file_name', 'file_path', 'breed'])
    for _, dirs, files in os.walk(img_path):
        for curr_dir in dirs:
            breed = curr_dir.split('-')[1]
            curr_path = os.path.join(img_path, curr_dir)
            for file_name in os.listdir(curr_path):
                file_path = os.path.join(curr_path, file_name)
                df_breed = pd.concat([df_breed, pd.DataFrame({'file_name':[file_name],
                                                              'file_path':[file_path],
                                                             'breed':[breed]
                                                            })
                                     ])
    return df_breed