# Comprendre le fonctionnement de Python

Ce document introduit un ensemble de notions qui permettent d'obtenir une vision globale du fonctionnement de python.
Disposer d'un ensemble de connaissance propre aux spécifités et au fonctionnement de python permet de mieux aborder les manipulations requises pour 
optimisation dles ressources GPU (par exemple cela est requis dans la programmation de d'algotyhme de deep-learning avec CUDA).

## Introduction générale au language Python

1. **Définition et origine**

Python est un langage de programmation.

> [!NOTE]
> **Définition de la programmation** : Programmer consiste à écrire des instructions pour un ordinateur.
> Un ensemble d'instructions est appelé un programme. Pour que l'ordinateur puisse comprendre ces instructions, on utilise un langage informatique. Un langage 
> informatique est comparable à une langue, mais avec beaucoup moins de mots, et il possède une grammaire précise à respecter.

Python a été développé à la fin des années 80 par un programmeur nommé Guido van Rossum. Guido van Rossum, étant fan de la célèbre série britannique "Monty Python", a décidé de nommer le langage "Python".

Python est open source et est en constante évolution. Cela signifie qu'il peut être utilisé librement.

2. **Usages et Applications de Python**
- Polyvalence : Grâce à ses nombreuses bibliothèques de fonctions, Python est très utilisé dans le milieu scientifique
- Tâches courantes : Il permet d'automatiser rapidement des tâches fastidieuses et de réaliser des prototypes d'applications
- Domaines spécifiques : C'est le langage principalement utilisé pour le Big Data et le Machine Learning


- Facilité d'apprentissage : Python est un langage très populaire car il est facile à apprendre. Il fait d'ailleurs partie du programme des lycées pour faire suite à la programmation Scratch.
- Productivité : Il permet aux développeurs de se concentrer sur ce qu'ils font plutôt que sur comment ils le font
- Concision : C'est un langage très concis qui permet d'effectuer beaucoup de choses avec peu de code
- Portabilité : L'un des gros avantages d'un langage interprété comme Python est sa capacité à fonctionner sur de nombreux systèmes d'exploitation.
Par exemple, un script écrit sur un Mac peut être exécuté sur un PC, ce qui ne serait pas possible directement avec un langage compilé qui nécessiterait un exécutable pour chaque plateforme cible.
- Flexibilité : Avec Python, tout est possible : on peut créer des programmes complexes en programmation orientée objet ou des scripts très simples de quelques lignes.

3. **Les spécificités de Python**

Python est un language de programmation intéprété.

!!! definition "Définition de la programmation"
    Programmer consiste à écrire des instructions pour un ordinateur…

!!! labtip "Astuce labo"
    Crée un environnement conda par projet.

!!! reminder "Rappel"
    Sauvegarde tes notebooks avant d’exécuter des cellules lourdes.

!!! definition "Language Compilé et language interprété"
    Il existe deux grandes familles de langages de programmation :
    1. Langages Compilés :
        - Exemples : C++, C#, Cobol
        - Fonctionnement : Lorsque l'on écrit du code avec un langage compilé, il faut d'abord le compiler pour pouvoir l'exécuter
        Cette compilation transforme le code en langage machine pour en faire un exécutable
        - Inconvénient : Pour un gros programme, la compilation peut prendre un certain temps
        - Avantage : Le programme généré est rapide à s'exécuter
    2. Langages Interprétés :
        - Exemples : Perl, SQL, et notre Python
        - Fonctionnement : Quand on écrit du code, celui-ci est lu par un interpréteur, un logiciel qui lit le script pour l'exécuter
        - Avantage : Il n'y a pas de temps perdu à la compilation
        - Inconvénient : C'est un peu plus lent à l'exécution
    Cas hybride : Certains langages, comme Java, sont entre les deux, car ils sont compilés non pas pour créer un exécutable direct, mais pour être lancés dans une > machine virtuelle


Le typage est dynamique :

Dans de nombreux langages (comme le C++), les variables doivent être "typées" (on parle de typage statique), ce qui signifie qu'il faut déclarer le type de chaque variable (un nombre entier, un réel, une chaîne de caractères, par exemple).
Avec Python, le typage est dynamique, c'est-à-dire que l'on ne spécifie pas le type des variables. 
Cela simplifie l'écriture du code, mais demande tout de même de la rigueur.

L'indentation pour les Blocs de Code :
Contrairement à la plupart des langages où les blocs de code sont encadrés par des accolades, en Python, c'est l'indentation du code qui indique si l'on entre ou sort d'un bloc. 
Bien que déroutant au début, cela s'avère puissant pour écrire un code lisible par le plus grand nombre.
