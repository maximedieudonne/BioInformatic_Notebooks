# Créer une documentation en ligne Markdown.

Ce document explique comment écrire une documentation comme celle ci. L'objectif est que la documentation soit publique, open source, clair.
La motivation vient d'un besoin personel de répertorier l'ensemble des notes acquises lors de la veille technique formation, apprentissage en lien avec l'analyse de donnée et le métier d'ingénieur de recherche, et bio-informaticien.

# Guide détaillé : Qu’est-ce que Cookiecutter, comment l’installer et créer un repo Github avec

Ce document explique étape par étape ce qu’est **Cookiecutter**, comment l’installer facilement, et comment utilser le template pour créer un repo Github. 

---

## 1. Qu’est-ce que Cookiecutter ?

**Cookiecutter** est un outil open source Python qui permet de générer rapidement la structure complète d’un projet à partir de modèles (templates) réutilisables.

### À quoi sert Cookiecutter ?

- Automatiser la création de la base d’un projet logiciel ou scientifique.
- Garantir une organisation standardisée, claire et adaptée aux bonnes pratiques.
- Éviter de copier-coller un vieux projet et perdre du temps à organiser ses dossiers/fichiers.
- Faciliter la reproductibilité et la collaboration en partant d’une base propre et documentée.

### Comment ça marche ?

- Cookiecutter utilise des **templates** (souvent hébergés sur GitHub).
- Ces templates contiennent :
  - Une structure de fichiers et dossiers
  - Des fichiers avec des variables que l’on remplit au moment de la création (exemple : nom du projet, auteur, description)
  - Des scripts ou fichiers de configuration
- Cookiecutter te pose des questions pour personnaliser ton projet (nom, licence, gestion de l’environnement, dépendances…).
- À partir de tes réponses, il génère un dossier complet prêt à l’emploi.

### Technologies sous-jacentes

- Basé sur le moteur de template **Jinja2** pour rendre dynamique la génération des fichiers.
- Travaille en ligne de commande, compatible avec tous les environnements Python.

---

## 2. Comment installer Cookiecutter ?

### Prérequis

- Avoir Python installé (version 3.3 ou supérieure recommandée).
- Avoir `pip`, le gestionnaire de paquets Python.

### Installation simple via pip

Ouvre un terminal (PowerShell sous Windows, Terminal sous Mac/Linux) et tape la commande :

```bash
pip install "cookiecutter>=1.7.0"
```

### Vérification

Pour vérifier que Cookiecutter est bien installé, exécute :

```bash
cookiecutter --version
```

Si la commande est reconnue, tu es prêt·e à l’utiliser.

> **Remarque :** Si la commande `cookiecutter` n’est pas trouvée, il peut s’agir d’un problème de variable d’environnement PATH (surtout sous Windows). Dans ce cas, essaie :

```bash
python -m cookiecutter --version
```

---

## 3. Utiliser Cookiecutter pour créer un projet

### Étape 1 : Choisir un template

Tu peux utiliser :

- Un template officiel (exemple : `https://github.com/drivendata/cookiecutter-data-science` pour des projets data science)
- Un dépôt GitHub public contenant ton template personnalisé
- Ton propre template local (dossier avec la structure du template)

### Étape 2 : Lancer la commande Cookiecutter

Dans ton terminal, tape :

```bash
cookiecutter https://github.com/drivendata/cookiecutter-data-science
```

> Remplace l’URL par celle de ton template.

### Étape 3 : Répondre aux questions

Cookiecutter te posera une série de questions pour personnaliser le projet, par exemple :

- Nom du projet
- Nom du module Python
- Auteur
- Description
- Gestionnaire d’environnement (conda, pip…)
- Licence open source
- Framework de test ou formatting à utiliser

Ces questions sont définies dans un fichier `cookiecutter.json` dans le template.

### Étape 4 : Génération du projet

Après avoir répondu, Cookiecutter crée un nouveau dossier portant le nom de ton projet, avec :

- Tous les fichiers de base configurés selon tes choix
- La structure de dossiers recommandée (données, scripts, tests, documentation, etc.)
- Fichiers de configuration (environnement, licence, README)

Tu peux directement commencer le développement dedans.

---

## 4. Exemple concret : Création de ton projet `NeuroMorpho_ML_Pipeline`

J'ai utilisé le template **cookiecutter-data-science** pour générer un dépôt structuré pour un projet ML sur les données NeuroMorpho.

Voici les options que j'ai choisi :

```bash
ccds
```
(Commande raccourcie pour cookiecutter-data-science)
Choix des paramètres avec réponses types, par exemple :

project_name: NeuroMorpho_ML_Pipeline
repo_name: NeuroMorpho_ML_Pipeline
module_name: NeuroMorpho_ML_Pipeline
author_name: Maxime Dieudonné
description: Demo project ML techniques for NeuroMorpho data analysis
dataset_storage: none
environment_manager: conda
dependency_file: environment.yml
pydata_packages: basic
testing_framework: pytest
linting_and_formatting: flake8 + black + isort
open_source_license: MIT
docs: mkdocs
include_code_scaffold: no


### Ce que ça a créé

- Un dossier `NeuroMorpho_ML_Pipeline/` avec le code de ton module
- Des dossiers `data/`, `notebooks/`, `tests/`, `docs/` (documentation MkDocs)
- Un fichier `environment.yml` pour créer un environnement conda avec toutes les dépendances
- Un `README.md` pré-rempli avec la description
- Des fichiers de licence (MIT), de configuration pour tests (pytest) et linting (flake8, black, isort)
- Une base pour la documentation avec MkDocs prête à éditer

On a une structure reproductible, prête à être versionnée sous Git, partagée sur GitHub et maintenue par toute équipe.

---

## 5. Conseils d’usage

- Modifie les fichiers `README.md` et ceux dans `docs/` pour documenter précisément ton projet.
- Utilise `conda env create -f environment.yml` pour recréer l’environnement de travail.
- Mets ton code dans le dossier du module (ici `NeuroMorpho_ML_Pipeline/`).
- Ajoute des tests dans `tests/` et exécute `pytest` pour la qualité.
- Gère la documentation avec `mkdocs serve` et publie-la sur GitHub Pages si besoin.
- Versionne tout avec Git et héberge sur GitHub (utilise la commande `git push`).

---

## 6. Ressources utiles

- [Documentation officielle Cookiecutter (anglais)](https://cookiecutter.readthedocs.io/en/stable/)
- [Exemple Cookiecutter Data Science github](https://github.com/drivendata/cookiecutter-data-science)
- [Tutoriel vidéo rapide en français](https://www.youtube.com/watch?v=Ple0vlNbUI8)
- Guide Microsoft Visual Studio (français) pour Cookiecutter : création via interface GUI [lien ici](https://learn.microsoft.com/fr-fr/visualstudio/python/quickstart-04-python-in-visual-studio-project-from-cookiecutter?view=vs-2022)

---

### En résumé

| Étape          | Action clé                                 |
|----------------|-------------------------------------------|
| Présentation   | Cookiecutter = automatisation création projet |
| Installation   | `pip install cookiecutter`                 |
| Lancement     | `cookiecutter <url_du_template>`          |
| Personnalisation | Répondre aux questions configurables     |
| Résultat       | Projet complet généré, prêt à coder       |
| Maintien       | Versionnement git, documentation, tests   |

Avec Cookiecutter, tu gagnes un temps précieux et tu assures la cohérence de tes projets, ce qui est idéal pour un travail scientifique et collaboratif de qualité.

---

# commandes 
```bash
mkdocs serve --config-file docs/mkdocs.yml  
````

```bash
mkdocs build --config-file docs/mkdocs.yml  
````

```bash
mkdocs gh-deploy --config-file docs/mkdocs.yml
```
