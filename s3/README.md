## I don't need cold storage because I have too few total storage size

## Bash to Get All Objects

```bash
aws s3api list-objects-v2 --bucket jimchen4214-archive --prefix archive-20240602/ --output json > all_objects.json
```

## A Utility Script to Check Restored Objects

```bash
bucket="jimchen4214-archive"

# Function to check restore status
check_restore() {
    key="$1"
    restore_status=$(aws s3api head-object --bucket "$bucket" --key "$key" --query 'Restore' --output text)

    if [[ $restore_status == *"ongoing-request=\"true\""* ]]; then
        echo "ongoing"
    elif [[ $restore_status == *"ongoing-request=\"false\""* ]]; then
        echo "completed"
    elif [[ -z $restore_status ]]; then
        echo "not_started"
    else
        echo "unknown"
    fi
}

export -f check_restore
export bucket

# Run in parallel and collect results
results=$(jq -r '.Contents[].Key' all_objects.json | parallel -j 20 check_restore)

# Count the results
ongoing=$(echo "$results" | grep -c "ongoing")
completed=$(echo "$results" | grep -c "completed")
not_started=$(echo "$results" | grep -c "not_started")
unknown=$(echo "$results" | grep -c "unknown")

echo "Ongoing restores: $ongoing"
echo "Completed restores: $completed"
echo "Not started: $not_started"
echo "Unknown status: $unknown"
```
