while true ; do
    filename=$(python3 activeTeams.py)
    scp "$filename" "share:~/ructfe/violetq3w3e3/$filename" 
    sleep 60
done