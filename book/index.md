# Notes pour Bio-informaticien·nes

Cette page répertorie un ensemble de notes utiles pour les ingénieur·es et chercheur·ses.
L’objectif est d’offrir des tutoriels, fiches pratiques et cours couvrant les principaux aspects de l’analyse de données issues du vivant, de la planification des expériences jusqu’à la mise en production et la reproductibilité.


# Comment utiliser ce site

- **Lire** : parcourez les sections Tutos et Notebooks via le sommaire à gauche.

- **Notebook** : Les notebooks sont déjà exécutés.

- **Reproduire en local (WSL/Linux)** :

```bash
# cloner
git clone <votre-fork-ou-ce-repo>.git && cd BioInformatic_Notebooks
# construire le site
jupyter-book build book
# publier localement (structure complète : CSS/JS/images)
rsync -a --delete book/_build/html/ docs/
touch docs/.nojekyll
```
- **Contribuer** : ouvrez une issue pour proposer un tuto, ou soumettez une pull request (PR) avec :

    - le fichier .md (ou .ipynb) dans book/tutos/ ou book/notebooks/,
    - l’entrée correspondante ajoutée dans book/_toc.yml, 
    - si nécessaire, la mise à jour de .binder/environment.yml.

# Ajouter un nouveau contenu

- Fichier ajouté : book/tutos/mon-sujet.md ou book/notebooks/mon_sujet.ipynb.
- Sommaire mis à jour (book/_toc.yml) :

```yaml
parts:
  - caption: "Notebooks"
    chapters:
      - file: notebooks/mon_sujet
  - caption: "Tutos"
    chapters:
      - file: tutos/mon-sujet
```
- Dépendances ajoutées si besoin : .binder/environment.yml.
- Build & publication :


```bash
conda activate bioinfo
```

```bash
jupyter-book clean --all book
jupyter-book build book
rsync -a --delete book/_build/html/ docs/
touch docs/.nojekyll
git add -A && git commit -m "Publier nouveau contenu" && git push
```
