grep -rl "sample" . | while read file; do
    # Count occurrences of "CSC510" in the file
    count=$(grep -o "CSC510" "$file" | wc -l)
    # If count is at least 3, print count, size, and filename
    if [ "$count" -ge 3 ]; then
        size=$(wc -c < "$file")  # Get file size using wc
        echo "$count $size $file"
    fi
done | gawk '{ gsub("file_", "filtered_", $3); print $1, $2, $3 }' | sort -k1,1nr -k2,2n