# Segmenter une image de cellule

## Introduction

**Le principe de la segmentation :** 
Segmenter un volume image de celulles consiste à délimiter la frontiere de chacune des cellules présentes sur l'image. Générallement cela ce fait en en basant sur la démarcation de la membrane ou du cytoplasme. 

**Interet de la segmentation :**

La biologie cellulaire quantitative necessite des mesures de plusieurs caractéristique de la cellule comme la forme, la position, l'expression ADN et l'expression protéinique. 
Pour obtenir ces informations spécifiquement à une cellule ciblée, il faut d'abord segmenter le volume image en differents corps cellullaire.


## Les différentes méthodes de segmentation

Cette tache peut être plutot facile à réaliser lorsque les cellules sont suffisament séparées les unes des autrs, par exemple dans le cas de culture in-vitro mono-dispersé. Cependant les cellule peuvent etre collé les unes les autres dans de nombreux tissus et etre difficile à séparer via un algorythme. ([1])

**Méthodes complétement manuelles**

- **2012** : Schindelin, J., Arganda-Carreras, I., Frise, E., Kaynig, V., Longair, M., Pietzsch, T., Preibisch, S., Rueden, C., Saalfeld, S., Schmid, B., et al. Fiji: an open-source platform for biological-image analysis. Nature methods 9, 676–682 (2012).

**Pipelines personalisables**

- **2006** : Carpenter, A. E., Jones, T. R., Lamprecht, M. R., Clarke, C., Kang, I. H., Friman, O., Guertin, D. A., Chang, J. H., Lindquist, R. A., Moffat, J., et al. CellProfiler: image analysis software for identifying and quantifying cell phenotypes. Genome biology 7, R100 (2006).

- **2011** : Sommer, C., Straehle, C., Koethe, U. & Hamprecht, F. A. Ilastik: Interactive learning and segmentation toolkit in 2011 IEEE international symposium on biomedical imaging: From nano to macro (2011), 230–233.

- **2018**: McQuin, C., Goodman, A., Chernyshev, V., Kamentsky, L., Cimini, B. A., Karhohs, K. W., Doan, M., Ding, L., Rafelski, S. M., Thirstrup, D., et al. CellProfiler 3.0: Next-generation image processing for biology. PLoS biology 16 (2018).

- **2019**: Berg, S., Kutra, D., Kroeger, T., Straehle, C. N., Kausler, B. X., Haubold, C., Schiegg, M., Ales, J., Beier, T., Rudy, M., Eren, K., Cervantes, J. I., Xu, B., Beuttenmueller, F., Wolny, A., Zhang, C., Koethe, U., Hamprecht, F. A. & Kreshuk, A. ilastik: interactive machine learning for (bio)image analysis. Nature Methods. ISSN: 1548-7105 (Sept. 2019).


**Méthodes automatiques**


- **2016**: Apthorpe, N., Riordan, A., Aguilar, R., Homann, J., Gu, Y., Tank, D. & Seung, H. S. Automatic neuron detection in calcium imaging data using convolutional networks in Advances in Neural Information Processing Systems (2016), 3270–3278. 

-  **2018**: Guerrero-Pena, F. A., Fernandez, P. D. M., Ren, T. I., Yui, M., Rothenberg, E. & Cunha, A. Multiclass weighted loss for instance segmentation of cluttered cells in 2018 25th IEEE International Conference on Image Processing (ICIP) (2018), 2451–2455.
 

- **2018**: Al-Kofahi, Y., Zaltsman, A., Graves, R., Marshall, W. & Rusu, M. A deep learning-based algorithm for 2-D cell segmentation in microscopy images. BMC bioinformatics 19, 1–11 (2018).

- **2018**: Chen, J., Ding, L., Viana, M. P., Hendershott, M. C., Yang, R., Mueller, I. A. & Rafelski, S. M. The Allen Cell Structure Segmenter: a new open source toolkit for segmenting 3D intracellular structures in fluorescence microscopy images. bioRxiv, 491035 (2018).

- **2018**: Funke, J., Mais, L., Champion, A., Dye, N. & Kainmueller, D. A benchmark for epithelial cell tracking in Proceedings of the European Conference on Computer Vision (ECCV) (2018).

**Avantages**:
**Inconvenients**: Méthodes entrainées sur des dataset particuliers, diffuculté à généraliser.


# Bibliographie : 

[1] Stringer, C., Wang, T., Michaelos, M., & Pachitariu, M. (s. d.). Cellpose : A generalist algorithm for cellular segmentation.


