grep -l "sample" * | while read file; do
    count=$(grep -o "CSC510" "$file" | wc -l)
    if [ "$count" -ge 3 ]; then
        size=$(wc -c < "$file")
        echo "$file $count $size"
    fi
done | sort -k2,2nr -k3,3n | gawk '{sub(/file_/, "filtered_", $1); print $0}'