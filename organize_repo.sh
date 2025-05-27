#!/bin/bash

# Setup
mkdir -p programming-assignments culminating-project mini-projects

# Clear old README if re-running
rm -f README.md

# Start README
echo "# MarkK14's Coding Projects" >> README.md
echo "" >> README.md
echo "Organized portfolio of programming assignments and mini-projects. Files were converted from .txt/.zip into usable source code format." >> README.md
echo "" >> README.md
echo "## 📁 Folder Structure" >> README.md
echo "- \`programming-assignments/\` – Assignments 1–7 and misc" >> README.md
echo "- \`culminating-project/\` – Final project (likely TypeScript/React)" >> README.md
echo "- \`mini-projects/\` – Small zipped projects (e.g., calculators, games)" >> README.md
echo "" >> README.md

# Process .txt files
assignment_num=1
echo "### Programming Assignments" >> README.md
for file in *.txt; do
    cleaned_name=$(basename "$file" .txt | sed -E 's/[-_~#()]+/ /g' | sed 's/  */ /g' | sed 's/^ *//;s/ *$//' | awk '{ for (i=1;i<=NF;i++) $i=toupper(substr($i,1,1)) tolower(substr($i,2)); print }')

    if [[ $file == *"Assignment"* ]]; then
        folder="programming-assignments/assignment$assignment_num"
        mkdir -p "$folder"

        mv "$file" "$folder/main.py"
        echo "- Assignment $assignment_num: $cleaned_name" >> README.md
        ((assignment_num++))
    elif [[ $file == *"culminating"* || $file == *"CULMINATING"* ]]; then
        mkdir -p culminating-project
        mv "$file" culminating-project/main.py
        echo "- Culminating Project: $cleaned_name" >> README.md
    else
        mkdir -p programming-assignments/misc
        new_name="programming-assignments/misc/$(basename "$file" .txt).py"
        mv "$file" "$new_name"
        echo "- Misc: $cleaned_name" >> README.md
    fi
done

# Move App.tsx if exists
if [[ -f App.tsx ]]; then
    mv App.tsx culminating-project/
    echo "- Culminating Project: App.tsx (likely a frontend or React app)" >> README.md
fi

# Process .zip files
echo "" >> README.md
echo "### Mini Projects" >> README.md
for zip in *.zip; do
    foldername="mini-projects/$(basename "$zip" .zip)"
    mkdir -p "$foldername"
    unzip -q "$zip" -d "$foldername"
    rm "$zip"

    # Make the folder name human-readable for README
    cleaned_name=$(basename "$foldername" | sed -E 's/[-_.]+/ /g' | sed 's/  */ /g' | sed 's/^ *//;s/ *$//' | awk '{ for (i=1;i<=NF;i++) $i=toupper(substr($i,1,1)) tolower(substr($i,2)); print }')
    echo "- $cleaned_name" >> README.md
done

echo "" >> README.md
echo "_Generated automatically by \`organize_repo.sh\`_" >> README.md

echo "✅ Repo organized and README generated!"
