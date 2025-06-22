# Sync Breeze Enterprise 10.0.28
# Victim machine: OS Windows 7, version 6.1 build 7601: service pack 1
How I pwned.


# Step one: We need to build a fuzzer and download the software.
File is included in the scripts.
Use fuzz.py, not my code.



# step 2: Attach to syncbsr
Send payload one.
offset.py, modified cred to:Hack south



# step 3 get the offset:
msf-pattern_offset -q 42306142
[*] Exact match at offset 780

# Step 4: ID bad bytes.


# Step 5 make a exploit but first get the jmp esp
1. Jump = jmp
2. esp = stack pointer.
3. This is our stack pointer jump to execute code at.
4. “JMP ESP” instruction, the execution flow is redirected to the address stored in the ESP register.

# Upon running our payload.

# Image one of the software.
![dasdfg](https://github.com/user-attachments/assets/f8c1a26f-4a93-4d9a-bcbb-72e99d8d7866)


# Image 2 shell as NT AUTHROITY.
![dadf](https://github.com/user-attachments/assets/3996aec3-8546-4fcb-addd-b35dd8172116)


