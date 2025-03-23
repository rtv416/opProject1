import sys

def vigenere_encrypt(text, key):
    text = text.upper()
    key = key.upper()
    encrypted = []
    for i, char in enumerate(text):
        if not char.isalpha():
            return None  # invalid input
        shift = ord(key[i % len(key)]) - ord('A')
        encrypted_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        encrypted.append(encrypted_char)
    return ''.join(encrypted)

def vigenere_decrypt(text, key):
    text = text.upper()
    key = key.upper()
    decrypted = []
    for i, char in enumerate(text):
        if not char.isalpha():
            return None  # invalid input
        shift = ord(key[i % len(key)]) - ord('A')
        decrypted_char = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
        decrypted.append(decrypted_char)
    return ''.join(decrypted)

def main():
    passkey = None

    while True:
        line = sys.stdin.readline()
        if not line:
            break

        line = line.strip().upper()
        if not line:
            continue

        if line == "QUIT":
            break

        parts = line.split(maxsplit=1)
        if len(parts) < 2:
            print("ERROR Invalid command", flush=True)
            continue

        command, argument = parts[0], parts[1]

        if command == "PASS":
            if argument.isalpha():
                passkey = argument
                print("RESULT", flush=True)
            else:
                print("ERROR Passkey must contain only letters", flush=True)

        elif command == "ENCRYPT":
            if passkey is None:
                print("ERROR Password not set", flush=True)
            elif not argument.isalpha():
                print("ERROR Input must contain only letters", flush=True)
            else:
                encrypted = vigenere_encrypt(argument, passkey)
                print(f"RESULT {encrypted}", flush=True)

        elif command == "DECRYPT":
            if passkey is None:
                print("ERROR Password not set", flush=True)
            elif not argument.isalpha():
                print("ERROR Input must contain only letters", flush=True)
            else:
                decrypted = vigenere_decrypt(argument, passkey)
                print(f"RESULT {decrypted}", flush=True)

        else:
            print("ERROR Unknown command", flush=True)

if __name__ == "__main__":
    main()
