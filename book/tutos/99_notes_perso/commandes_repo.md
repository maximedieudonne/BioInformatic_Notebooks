# Commandes utiles pour gérer ce repo.

Mise à jour du Toc et création des fichiers automatiquement :

```bash
cd ~/repo/BioInformatic_Notebooks

ROOT="book"  # on crée sous book/tutos/...
read -r -d '' LIST <<'EOF'
tutos/00_metier/0000_metier_bioinformaticien

tutos/01_biodonnees/0100_type_images
tutos/01_biodonnees/0101_techniques_imagerie

tutos/02_routines/0200_principes_fair
tutos/02_rouines/0201_bibliographie
EOF

# Création conditionnelle des .md avec un titre par défaut
while IFS= read -r p; do
  [ -z "$p" ] && continue
  file="$ROOT/$p.md"
  dir="$(dirname "$file")"
  mkdir -p "$dir"
  if [ ! -f "$file" ]; then
    title="# $(basename "$p" | sed 's/^[0-9a-zA-Z]*_//; s/_/ /g')"
    printf "%s\n\n_TODO: contenu à écrire._\n" "$title" > "$file"
    echo "Créé: $file"
  else
    echo "Existant: $file"
  fi
done <<< "$LIST"
```