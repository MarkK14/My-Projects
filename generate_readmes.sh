#!/bin/bash

# Helper function to write a README for a given folder and language
write_readme() {
  folder=$1
  language=$2
  cat > "$folder/README.md" << EOF
# ${language^} Assignments

This folder contains ${language} assignments and code files written as part of various programming exercises or coursework.

Each file demonstrates key programming concepts in $language such as:
- Basic syntax and logic
- Input/output operations
- Functions and modularity
- Conditionals and loops

---
EOF
}

# Generate READMEs for each language-specific folder
write_readme "programming-assignments/cpp" "C++"
write_readme "programming-assignments/java" "Java"
write_readme "programming-assignments/arduino" "Arduino"
write_readme "programming-assignments/python" "Python"

# README for culminating project
cat > "culminating-project/README.md" << EOF
# Culminating Project

This is a React TypeScript project that showcases frontend design skills using components like \`App.tsx\`.

It was developed as part of a final assignment and demonstrates the use of:
- React components
- JSX/TSX syntax
- Modular UI structure
EOF

# README for mini-projects
cat > "mini-projects/README.md" << EOF
# Mini Projects

This folder contains smaller independent projects and exercises, each in its own folder. These include:
- Calculators
- Games
- Utilities

Each project is unzipped and self-contained.
EOF

echo "✅ All README.md files generated!"
