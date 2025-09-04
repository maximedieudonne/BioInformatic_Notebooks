# Creer un paquet bioinfo


Ce document présente les pratiques modernes pour creer un paquet (package) python utilse aux études bio-informatiques.
Ce document explique ce qu'est un paquet python, comment en creer un avec les bonnes routines métier d'ingénieur de recherche.

##  C’est quoi un “paquet” Python et pourquoi c’est utile en recherche ?

> [!IMPORTANT]
> Un paquet (package) est un ensemble structuré de modules/fonctions + métadonnées > (nom, version, dépendances, points d’entrée). Concrètement, c’est ce qui te permet de faire pip install monoutil et d’obtenir :
>- un import monoutil propre (API stable),
>- une CLI (commande terminal) quand tu déclares un entry point, des dépendances résolues automatiquement,
> - une version traçable (tags Git, changelog),
> - un artefact reproductible (wheel .whl) que la CI/HPC peut installer vite.

## Pourquoi c’est important en recherche ?

- **Reproductibilité** : même code + mêmes versions de deps ⇒ mêmes résultats (ou au moins même pipeline).

- **Diffusion et pérennité** : tes collègues (ou la future toi) ré-utilisent l’outil sans bricoler l’environnement.

- **Intégration pipeline** : Nextflow/Snakemake/CI savent installer ton outil comme une brique standard.

- **Crédibilité & citabilité** : versionnage clair, DOI possibles, packaging conforme aux bonnes pratiques.

## Faut-il toujours empaqueter un code d’analyse ?

Non.

Pas nécessaire pour l’exploration ad-hoc (notebook unique, une fois).

Recommandé dès que tu : (i) réutilises l’analyse, (ii) la partages, (iii) l’intègres à un pipeline, (iv) veux une CI, (v) publies.
Règle simple : si quelqu’un d’autre doit l’exécuter (toi dans 6 mois y compris), emballe-le.

## Les étapes clefs pour créer un paquet python en bio-informatique

Les étapes clefs pour créer un paquet python oriénté bio-informatique sont les suivantes : 

1. Ecrire le code python

2. Déclarer les métadonnées + deps dans pyproject.toml (déclaratif, standard).

3. Construction d'un wheel via le Backend de build (setuptools, hatch…).

4. Pip installe la wheel + ses dépendances.

5. Les utilisateurs ont tes entry points (scripts CLI, plugins, etc.)

6. Installation éditable en dev, en utilisant  pip install -e .

# Pyproject.toml plutot que setup.py


# Le système de build

Le système de build est l'ensemble des règles et outils qui transforment le code source Python en une **distribution installable** (paquet).
C'est comme un "make" pour le language C, mais adapté à Python.

Un système de build prend : 
- le code source (src/monpaquet/)
- les métadonnées (nom, version, dépendances)
- les fichiers annexes (README, licence)

et produit un paquet distribuable (par ex une wheel)

# Le backend de build
Un backend de build = l'outil qui sait comment faire le build.
Le backend de build est iniqué dans [build-system]du pyproject.tolm

Exemple:
- setuptools.build_meta -> backend historique, très utilsé.
- hatchling.build -> backend moderne, rapide.
- poetry.core.masonry.api -> backend de Poetry.
- pdm.backend -> backend de PDM

Tu choisis ton backend -> pip saura comment construire ton paquet.

# Roue/ Wheel

Une wheel (.whl) est le format binaire standard des paquets Python (PEP 427)
- Contient le code prêt à installer (pas besoin de recompiler)
- c'est ce que pip installe quand tu fais pip install numpy
- avantage : installation rapide et reproductible (pas de setup.py)

# Entry point

un **entry point** = une "porte d'entrée" pour un paquet.
Très  utilisé pour créer des **commandes en ligne de commande (CLI)**
 Exemple dans pyproject.toml!

 ```toml
[project.scripts]
annotate-variants = "genome_annontator.cli:main"

Après l'installation, l'utilisateur peut taper dans son terminal : 

```bash
annotate-variants input.vcf
````

et ça appelle la fonction main() dans genome_annotator/cli.py