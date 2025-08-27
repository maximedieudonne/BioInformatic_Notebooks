# Le métier de bio-informaticien·ne, c’est quoi ?

La bio-informatique se situe à l’interface entre la biologie, l'informatique et les statistique. 
Le métier consiste à :

- concevoir des analyses de données biologiques (NGS, protéomique, imagerie, métabolomique, phénotypage, etc.) ;

- développer des scripts/pipelines robustes et reproductibles ;

- interpréter les résultats avec les équipes expérimentales ;

- diffuser des outils, des jeux de données et des bonnes pratiques FAIR.

# Domaines d’application (exemples)

- Génomique : contrôle qualité (FastQC/MultiQC), alignement (BWA/Bowtie2), appel de variants (bcftools/GATK), annotation.

- Transcriptomique (RNA-seq) : quasi-mapping (salmon), quantification, tests différentiels, enrichissements fonctionnels.

- Épigénomique : ChIP-seq/ATAC-seq, analyse de pics, intégration multi-omiques.

- Protéomique : identification/quantification, recherche de PTM, intégrations protéome-génome.

- Imagerie : segmentation, extraction de features, apprentissage profond, tracking.

- Microbiome/Métagénomique : classification taxonomique, profils fonctionnels, diversité.


# Les piliers du métier

- Programmation scientifique : Python (numpy/pandas/matplotlib), R (tidyverse/bioconductor).

- Systèmes : Linux/CLI, gestion de paquets (conda/mamba), conteneurs (Docker/Singularity/Apptainer).

- Statistique & modélisation : tests, modèles linéaires, contrôle du FDR, apprentissage machine.

- Reproductibilité : Git/GitHub, notebooks (Jupyter), pipelines (Snakemake/Nextflow), CI.

- Données & FAIR : métadonnées, formats standards (FASTQ/SAM/BAM/VCF/GFF), dépôts publics.

- Interop & infra : HPC/SLURM, Cloud, stockage, sécurité/éthique/RGPD.


# Un workflow type (NGS)

1. Planifier : design expérimental, puissance/statistiques, métadonnées.

2. Acquérir : FASTQ + checks (intégrité, encodage).

3. QC : FastQC/MultiQC, trimming si besoin.

4. Aligner/Quantifier : BWA/Bowtie2, salmon/kallisto.

5. Analyser : variantes, expression différentielle, enrichissements.

6. Valider : contrôles positifs, réplicats, sensibilités/spécificités.

7. Documenter & publier : figures, rapport, dépôt de données, archivage.


# Boîte à outils recommandée

- Gestion d’environnements : conda/micromamba (fichiers environment.yml).

- Pipelines : Snakemake/Nextflow + profils HPC/Cloud.

- Qualité : MultiQC ; tests unitaires simples sur fonctions critiques.

- Visualisation : matplotlib/plotly/seaborn, IGV, UCSC Genome Browser.

- Packaging : pyproject.toml, versions épinglées, conteneurs pour la prod.

- Collab : Git/GitHub (issues, PR), conventions de nommage et de logs.


# Qualité, éthique, diffusion

- Traçabilité : versions d’outils, références génomiques, paramètres ; journal d’analyse.

- Éthique & RGPD : pseudonymisation, contrôles d’accès, consentements, DPIA si nécessaire.

- FAIR : formats ouverts, DOIs, documentation d’accès/reprise, licences claires.

# Bonnes pratiques CNRS (recommandations rapides)

- Données : séparer brutes / intermédiaires / résultats, versionner les scripts mais pas les gros binaires (utiliser des DOIs ou DRS).

- Paramètres : conserver un fichier YAML/TOML centralisé des paramètres d’analyse.

- Rapports : générer automatiquement un rapport QC (Notebook/Quarto/Markdown + MultiQC).

- Formation : documenter pré-requis, temps d’exécution, taille des données, budgets HPC.

- Pérennité : fournir une image conteneur (ou un environment.yml figé) + un how-to-reproduce.