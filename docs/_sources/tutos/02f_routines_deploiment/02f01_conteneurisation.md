# Conteneurisation

J'ai appris la différence ntre une image, Docker, Docker Desktop, Singularity/Apptainer, 

Une image d'un logiciel est la recette pour reproduire ce logiciel.


Cas d'usage pour un bio-informaticien. On écrit un code machine learning qui utilise Pytorch.
Pour ce code il faut un environement spécifique (package, version), creer un docker de son code permet de reproduire l'environnement avec le code.

Cuda signifie Calcul Unified D A
Cuda est une suite logiciel developper par Nvidia qui permet au package comme pytorch de communiquer avec le GPU.

Le GPU signifie Graphical Processor Unit.

Les étapes à suivre pour creer une image DOcker de son code.

Il faut installer WSL. WSL est le Window Sub Linux
Il faut installer DOcker Desktop qui va permettre de faire tourner un moteur DOcker sur WSL.

Il faut installer le driver Nvidia. LE driver permet la communication entre pytorch et le GPU.




