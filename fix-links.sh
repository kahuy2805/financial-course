#!/bin/bash

# Fix all lesson links in index.html to match actual filenames

cd /sessions/kind-charming-bardeen/mnt/Course/Stock_Trading_Course_HTML

# Get all actual lesson files and create sed commands
for file in pages/lesson-*.html; do
    filename=$(basename "$file" .html)
    
    # Extract lesson number from filename (e.g., "1-1" from "lesson-1-1-what-is-stock-market.html")
    if [[ $filename =~ lesson-([0-9]+)-([0-9]+)- ]]; then
        chapter="${BASH_REMATCH[1]}"
        lesson="${BASH_REMATCH[2]}"
        
        # Replace lesson-X.Y.html with the actual filename
        sed -i "s|pages/lesson-${chapter}\.${lesson}\.html|pages/${filename}.html|g" index.html
        sed -i "s|pages/lesson-${chapter}\.${lesson}\.html|pages/${filename}.html|g" pages/*.html
    fi
done

# Fix exercise links
for i in {1..14}; do
    sed -i "s|pages/exercises-${i}\.html|pages/chapter-${i}-exercises.html|g" index.html 2>/dev/null || true
done

echo "Links fixed!"
