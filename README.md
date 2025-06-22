# SyncBreezeExp
How I pwned syncbreeze


# Step one: We need to build a fuzzer and download the software.
File is included in the scripts.
Use fuzz.py, not my code.

# step 2: Attach to syncbsr
Send payload one.
offset.py, modified cred to:Hack south

#step 3 get the offset:
msf-pattern_offset -q 42306142
[*] Exact match at offset 780

# Step 4: ID bad bytes.
