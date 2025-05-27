#!/bin/bash

# Create main folders
mkdir -p programming-assignments/{cpp,java,arduino,python} culminating-project mini-projects

# STEP 1: Copy ECE150 C++ code to cpp folder and rename .txt to .cpp
cp -r /c/Users/markk/ECE150/* programming-assignments/cpp/
for file in programming-assignments/cpp/*.txt; do
  mv "$file" "${file%.txt}.cpp"
done

# STEP 2: Handle the rest of the .txt files in root
for file in *.txt; do
  filename=$(basename "$file" .txt)

  # Heuristics to determine language based on filename keywords
  if [[ $filename == *"arduino"* || $filename == *"wheel"* ]]; then
    mv "$file" "programming-assignments/arduino/$filename.ino"
  elif [[ $filename == *"java"* || $filename == *"Assignment #3"* || $filename == *"Assignment #4"* ]]; then
    mv "$file" "programming-assignments/java/$filename.java"
  elif [[ $filename == *"overview"* || $filename == *"Assignment #1"* || $filename == *"function"* ]]; then
    mv "$file" "programming-assignments/python/$filename.py"
  else
    echo "⚠️  Skipped ambiguous file: $file (please move manually)"
  fi
done

# STEP 3: Move TypeScript files to culminating-project
if [[ -f App.tsx ]]; then
  mv App.tsx culminating-project/
fi

# STEP 4: Unzip zipped projects into mini-projects/
for zip in *.zip; do
  foldername="mini-projects/$(basename "$zip" .zip)"
  mkdir -p "$foldername"
  unzip -q "$zip" -d "$foldername"
  rm "$zip"
done

echo "✅ Repo is now organized with accurate language folders!"
