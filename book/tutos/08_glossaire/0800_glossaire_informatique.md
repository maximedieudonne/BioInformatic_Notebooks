# Glossaire informatique

## Paquet (package)

Un paquet (package) est un ensemble structuré de modules/fonctions + métadonnées (nom, version, dépendances, points d’entrée). Concrètement, c’est ce qui te permet de faire pip install monoutil et d’obtenir :

- un import monoutil propre (API stable),

- une CLI (commande terminal) quand tu déclares un entry point, des dépendances résolues automatiquement,

- une version traçable (tags Git, changelog),

- un artefact reproductible (wheel .whl) que la CI/HPC peut installer vite.