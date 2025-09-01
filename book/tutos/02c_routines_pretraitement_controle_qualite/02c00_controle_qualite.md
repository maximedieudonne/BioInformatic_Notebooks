# Controle qualite# C’est quoi le QC en imagerie ?

Le QC (Quality Control), c’est l’ensemble des vérifications systématiques qui garantissent que :

- l’image acquise représente fidèlement l’échantillon,

- les artefacts sont maîtrisés (ou documentés),

- les étapes d’analyse (prétraitements, segmentation, tracking, ML) produisent des résultats fiables et reproductibles.

L’idée : détecter tôt un problème (microscope, acquisition, données, algorithmes) pour corriger ou stopper avant de tirer des conclusions biologiques fausses.

# Les 6 niveaux de QC en imagerie

1. QC matériel / plateforme

Vérifie que le système optique et la chaîne de détection fonctionnent dans les spécifications.

Exemples : PSF, résolution, uniformité d’illumination, registration inter-canaux, stabilité mécanique (drift), calibration d’échelle (µm/pixel), linéarité du capteur.

2. QC à l’acquisition

Ce que tu règles au moment de la prise d’image pour éviter l’irrécupérable.

Exemples : exposition (éviter la saturation), focus, échantillonnage conforme à Nyquist, z-step cohérent, durée d’acquisition vs photoblanchiment.

3. QC des données (fichiers)

Intégrité et métadonnées complètes.

Exemples : format OME-TIFF/NGFF, tailles cohérentes (X/Y/Z/C/T), pixel size présent, horodatages, LUTs standards, contrôle d’orientation/axes.

4. QC des prétraitements

Tu corriges ce qui est systématique mais réversible.

Exemples : flat-field / shading (illumination inhomogène), soustraction du fond, dénoyautage (sans baver sur les bords), déconvolution (PSF mesurée/théorique), registration multi-canaux.

5. QC de la segmentation / features

Vérifie que les objets détectés correspondent à la réalité biologique et aux annotations.

Exemples : métriques pixel (IoU/Dice), objet (F1 objets, erreurs de comptage), distributions de taille/forme plausibles, erreurs typiques (sous-segmentation, sur-segmentation, fusion, trous).

6. QC du tracking / modèles ML

Vérifie la cohérence temporelle (trajectoires, identités) et la validité des modèles (pas de fuites de données, calibration).

Exemples : tracking (ID switches, longévité des pistes), ML (split train/val/test, AUC/F1, calibration (ECE), généralisation sur lots/jours différents).


# Mesures clés et repères pratiques

Repères = ordres de grandeur usuels, à adapter par modalité (widefield, confocal, spinning, light-sheet) et objectif/NA.

1) **Matériel**

- PSF / Résolution : largeur latérale proche des valeurs attendues ; z plus large que xy (normal).

- Uniformité d’illumination : coefficient de variation (CV) du fond < 10–15% (après correction, résiduel < ~2–5%).

- Registration inter-canaux : < 0,5 pixel de décalage (perles multicanaux).

- Drift : < 1 pixel/min (ou corrigé numériquement si constant).

- Calibration : µm/pixel cohérent avec objectif + taille pixel caméra.

2) **Acquisition**

- Saturation : viser < 1% de pixels saturés ; dynamique explorée sans écrêtage.

- SNR : suffisant pour que le segmenteur sépare fond/objet (à estimer avec une mesure simple type Tenengrad/variance locale).

- Nyquist : échantillonner à ≥ 2–3 pixels par plus petit détail (xy) ; z-step ≈ 0,5–1× résolution axiale.

- Photoblanchiment : pente d’intensité vs temps faible et stable.

3) **Données**

- OME/REMBI : métadonnées présentes (échelles X/Y/Z, temps, canaux, intensités).

- Intégrité : hash/empreinte si gros volumes, absence de corruption/axes inversés.

4) **Prétraitements**

- Flat-field : vignettage corrigé (profil plat ± quelques %).

- Denoising : sans élargir les objets ; contrôle par profils de bords.

- Déconvolution : amélioration du contraste sans halos/artéfacts ; PSF documentée.

- Registration : décalage résiduel < 0,5 pixel si colocalisation.

5) **Segmentation / Features**

- Pixel : Dice/IoU élevés (p.ex. Dice ≥ 0,8 sur un échantillon annoté).

- Objet : F1 objet élevé ; erreurs de fusion/scission documentées.

- Features : distributions (aire, circularité) plausibles et stables par lot.

6) **Tracking / ML**

- Tracking : peu d’ID switches, pistes longues et continues ; métriques type DET/TRA en vert sur un sous-ensemble.

- ML : séparation claire train/val/test, aucune fuite ; métriques (F1/PR-AUC) stables en validation croisée ; calibration correcte (ECE bas).

# Artefacts courants & remèdes rapides

- Vignettage / gradients → flat-field (BaSiC/CIDRE), illumination Köhler.

- Bruit / grain → débruitage modéré (NL-means/Wavelets), binning au besoin.

- Saturation / bande dynamique → ajuster gain/expo ; HDR si nécessaire.

- Aberrations chromatiques → registration par perles multicanaux.

- Drift / jitter → correction post-hoc (phase correlation), stabilisation mécanique.

- Rolling-shutter / banding → paramètres caméra, temps d’expo plus long, correction logicielle.

- Z-step erroné → recalibrer l’axe z ; vérifier le fichier de commande.

# Documentation & traçabilité (FAIR)

- Métadonnées : microscope, objectif/NA, taille pixel, lasers/longueurs d’onde, filtres, temps d’expo, gain, dates, opérateur, échantillon, conditions.

- Versions : logiciels/plug-ins, paramètres de prétraitement, scripts.

- Contrôles : images de perles, lames de test, rapports QC (PDF/HTML).

- Données : formats ouverts (OME-TIFF / OME-NGFF), organisation claire (Plate/Well/Field/Time).

# Routine QC (planning réaliste)

- À chaque acquisition : check rapide (saturation, focus, drift, uniformité visible), note d’expo/gain, mini-rapport.

- Hebdo : PSF, uniformité, registration multicanaux (perles), rapport standardisé.

- Projet : QC de prétraitement + échantillons annotés pour valider segmentation/tracking, critères GO/NO-GO.

- Publication : annexe QC (métadonnées, PSF, uniformité, exemples d’artefacts + corrections, métriques de seg/tracking/ML sur vérité terrain).

# Règles “GO/NO-GO” (exemples)

- Saturation massive, métadonnées manquantes, z-step faux → NO-GO (reprise acquisition).

- Uniformité dégradée mais corrigeable, faible drift, bruit modéré → GO avec correction documentée.

- Segmentation instable (Dice < 0,7), tracking avec nombreux ID switches → stop analyse, revoir prétraitement/modèle/paramètres ; constituer un set d’annotations plus solide.

# Ce que produit un bon QC (livrables)

- Rapport QC (HTML/PDF) : PSF, uniformité, saturation, drift, exemples avant/après correction, métriques de seg/tracking/ML.

- Jeu d’images de référence (perles, lames tests) + paramètres d’acquisition.

- Échantillons annotés (vérité terrain) pour valider segmentation/tracking.

- Scripts/Notebooks versionnés + fichiers YAML des paramètres.


| Type d’image                            | Contrôles qualité spécifiques                                                                                                                                    | Exemples de protocoles QC                                                                                                                                                                    |
| --------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Microscopie (optiques)**              | Vérif. PSF, uniformité d’illumination, calibration, drift, artefacts optiques, SNR, contrôle saturation, flat-field, métadonnées complètes                       | Images de billes (PSF), contrôle régulier de l’uniformité avec lames fluorescentes, vérification focus manuel/auto, script FIJI pour détecter la saturation, calcul du SNR sur fond/cellules |
| **Microscopie électronique (MEB/MET)**  | Résolution nanométrique, étalonnage échelle, contrôle bruit/fond, vérif. d’artefacts de préparation (cryo, coloration), intégrité des champs                     | Images d’étalons nanométriques, vérification du contraste, annotation de la morphologie des objets, contrôle absence de zones brûlées/ombres                                                 |
| **IRM/IRMf**                            | Contrôle distorsion géométrique, uniformité du champ magnétique, bruit thermique, calibrations spatiales, absence d’artefacts de mouvement, SNR, intégrité DICOM | Fantômes de calibration (géométrie/homogénéité), rapport d’absence d’artefacts de mouvement (qualité patient/acquisition), vérification DICOM/métadonnées                                    |
| **TEP/TEP-CT**                          | Correct. du bruit de fond, cohérence temporelle, co-registration avec CT, uniformité détecteurs, contrôle de radioactivité, calibrations 3D                      | Suivi de la co-registration sur images fusionnées, vérif. d’uniformité sur la série, calibration radioactivité vs référents, script d’analyse du bruit de fond par coupe                     |
| **Scanner CT/X**                        | Uniformité densité Hounsfield, calibrat. spatiale, contrôles de bruit, artefacts (métal, mouvement), résolution, intégrité DICOM                                 | —                                                                                                                                                                                            |
| **Échographie**                         | Vérification résolution axiale/latérale, calibrat. échelle, contrôle artefacts (ombres, bruit speckle), intégrité temporelle, SNR                                | —                                                                                                                                                                                            |
| **Histologie numérisée**                | Uniformité scan, calibrat. couleur, fidélité spatiale, contrôle tilt/rotation, intégrité fichiers, métadonnées (objectif, tranche, teinture)                     | Analyse comparée de la colorimétrie sur différents scanners, script d’alignement/rotation, contrôle manuel sur région témoin                                                                 |
| **Cytométrie / High-content screening** | Vérif. uniformité champs, calibrat. intensité/canal, SNR, absence de saturation, intégrité des fichiers, vérif. segmentation/annotation automatique              | QC automatique : histogrammes d’intensité, taux d’objets détectés/ratés, contrôle d’intégrité des fichiers batch issus du système                                                            |


# Pour chaque modalité, les bonnes pratiques regroupent :

- Contrôle physique/métrologique régulier (soit via étalon, soit via phantom, soit via objet de référence)

- Validation de l’intégrité des fichiers et des métadonnées

- Test d’artefacts et vérification de la reproductibilité par lots/plateformes.

La mise en place de workflows QC automatisés (via scripts Python, FIJI, plugins spécialisés) est répandue pour garantir la robustesse de l’analyse bio-informatique.