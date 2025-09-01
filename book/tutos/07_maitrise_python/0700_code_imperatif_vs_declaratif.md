# Code impératif vs déclaratif

- **code impératif** = tu dis *comment* faire.

Exemple setup.py: 

```python
# setup.py (ancien style)
from setuptools import setup

setup(
    name="monpaquet",
    version"0.1",
    install_requires=["numpy","pandas"]
)
```

Ici, Python **exécute** du code. On pourrais mettre des if, for, import -> flexible mais imprévisible.

- **code déclaratif** = tu dis *ce que tu veux*, sans décrire comment.

Exemple pyproject.toml

```python
[project]
name = "monpaquet"
version = "0.1"
dependencies = ["numpy","pandas"]
```

Ici, on **déclare** les indos. Pas de code exécuté -> plus simple, plus sûr, standardisé.





