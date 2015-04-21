while read line; do
    openssl aes-256-cbc -d -in aes.bin -out decrypted.txt -k $line
    if [ $? -eq 0 ]; then cat decrypted.txt; exit; fi
done < ../Web-2_30/passwords.txt
