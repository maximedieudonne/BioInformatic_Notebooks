# Comment créer un projet

Pour creer un projet, les étapes à suivre sont : 

1. **Créer le dossier projet et son arborecence**

```bash
mkdir -p demo-projet/{data,scripts}
```

*note : "-p" permet de creer des sous-dossier et "{}" permet de créer plusieurs sous-dossier. Attention pas d'espace après les virgules. 

2. **Créer un environement**

L'environnement peut être crée à partir de mamba ou de conda. Pour la suite, nous montrons en ligne comment creer un environement conda à partir d'un fichier "environment.yml"
Un fichier environment.yml doit préciser "name", "channels" , "dependencies" et "pip" pour ce qui est installé via pip.

```bash
cat > environment.yml <<'YAML'
name: demo-project
channels:
    conda-forge
dependencies:
    - python=3.11
    - numpy
    - pandas
    - scikit-image
    - opencv
    - matplotlib
    - jupyterlab
    - ipykernel
    - pip
    - pip:
        - tqdm
YAML
```
Pour vérifier le contenu

```bash
cat environment.yml
```

ensuite pour creer l'environnement conda à partir du fichier environment.yml

```bash
conda env create -f enironment.yml
```

Puis il suffit d'activer l'environnement : 

```bash
conda activate demo-project
```

3. **Télécharger les données**

Exemple de téléchargement de données : 

```bash
mkdir -p data/ctc
wget -O data/ctc/Fluo-N2DL-HeLa.zip \
  https://data.celltrackingchallenge.net/training-datasets/Fluo-N2DL-HeLa.zip
unzip -q data/ctc/Fluo-N2DL-HeLa.zip -d data/ctc
```