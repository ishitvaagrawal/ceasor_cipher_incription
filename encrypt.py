input_file = "Plaintext.txt"
output_file = "Cipher.txt"
key = int(input("Enter the key: "))
encrypted_text = ""

with open(input_file, "r") as file:
    text = file.read()

for ch in text:
    if ch.isalpha():
        if ch.islower():
            ch = chr((ord(ch) - ord('a') + key) % 26 + ord('a'))
        elif ch.isupper():
            ch = chr((ord(ch) - ord('A') + key) % 26 + ord('A'))
    elif ch.isdigit():
        ch = chr((ord(ch) - ord('0') + key) % 10 + ord('0'))

    encrypted_text += ch

with open(output_file, "w") as file:
    file.write(encrypted_text)

print("Encryption complete. Check", output_file)