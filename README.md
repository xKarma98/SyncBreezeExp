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


# Step 5 make a exploit but first get the jmp esp
1. Jump = jmp
2. esp = stack pointer.
3. This is our stack pointer jump to execute code at.
4. “JMP ESP” instruction, the execution flow is redirected to the address stored in the ESP register.
