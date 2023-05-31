# Développez une application Web en utilisant Django

Création d'un applicatif web pour la création d'articles et de commentaires associés à cet article

L'interface est écrite en Python avec le framwork Django


## Interface

![App Screenshot](https://github.com/RodWeb53/P9_LITReview/blob/main/src/media/Ecran_base.png)


## Mise en place du programme

`Pré-requis : python 3 doit être installé sur votre machine`

- Télécharger ce code dans ''code'' > ''Download ZIP''
- Décompresser le dossier

### 1. Création de l'environnement virtuel

Ouvrez le terminal, allez dans le dossier que vous avez téléchargé

Tapez la commande suivante pour créer l'environnement virtuel

    python -m venv env

### 2. Lancement de l'environnement virtuel

Sous Windows tapez la commande suivante :

    env\Scripts\activate.bat

Sous MAC ou Linux tapez la commande suivante :

    source env/bin/activate

### 3. Intallation des dépendance

Tapez la commande suivante :

    pip install -r requirements.txt

### 4. Lancement du serveur

Aller dans un terminal et tapez les commandes suivantes :

    cd src

    python manage.py runserver

### 5 Lancement du navigateur

Dans votre navigateur tapez l'adresse suivante :

    http://127.0.0.1:8000/

## Listes des utilisateurs
     
     ___________________________________
    | *Identifiant* |   *Mot de passe*  |
    |---------------|-------------------|
    | Utilisateur1  |   LITREview2023   |
    | Utilisateur2  |   LITREview2023   |
    | Utilisateur3  |   LITREview2023   |
    | Utilisateur4  |   LITREview2023   |
    | Utilisateur5  |   LITREview2023   |
    | Utilisateur6  |   LITREview2023   |
    | Utilisateur7  |   LITREview2023   |
    |_______________|___________________|

## Mot de passe

LITREview2023

## Générer un rapport avec flake8-html

Le rapport flake8 créer un rapport montrant que le code ne contient pas d'érreur de peluchage

    Le rapport sera créer à l'aide du fichier setup.cfg
    le fichier de configuration permet de ne pas prendre en analyse l'environnement virtuel
    Limite la longueur des lignes à 119
    Et paramètre le répertoire de sortie

    Taper la commande "flake8" a la racine du projet
