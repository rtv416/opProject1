import sys
import re
from subprocess import Popen, PIPE
from datetime import datetime

def get_timestamp():
    now = datetime.now()
    return now.strftime("%Y-%m-%d %H:%M")

def is_valid_string(s):
    return re.fullmatch(r'[a-zA-Z]+', s) is not None

def send_and_receive(proc, message):
    proc.stdin.write(message + '\n')
    proc.stdin.flush()
    return proc.stdout.readline().strip()

def main():
    if len(sys.argv) != 2:
        print("Usage: python driver.py <logfile>")
        return

    log_file = sys.argv[1]
    history = []

    # Start subprocesses
    logger = Popen(['python', 'logger.py', log_file], stdin=PIPE, text=True)
    encryption = Popen(['python', 'encryption.py'], stdin=PIPE, stdout=PIPE, text=True)

    def log(action, message):
        timestamped = f"{action} {message}"
        logger.stdin.write(timestamped + '\n')
        logger.stdin.flush()

    log("START", "Driver started.")

    while True:
        print("\nChoose an option:")
        print("1. password")
        print("2. encrypt")
        print("3. decrypt")
        print("4. history")
        print("5. quit")

        choice = input("Enter your choice: ").strip().lower()
        log("CMD", choice)

        if choice == "password" or choice == "1":
            print("\nUse a string from history? (y/n)")
            use_hist = input("> ").strip().lower()

            if use_hist == 'y' and history:
                for i, item in enumerate(history):
                    print(f"{i+1}. {item}")
                print("0. Enter new string")
                try:
                    idx = int(input("Select number: ").strip())
                    if idx == 0:
                        password = input("Enter new password: ").strip()
                    else:
                        password = history[idx - 1]
                except:
                    print("Invalid selection.")
                    continue
            else:
                password = input("Enter new password: ").strip()

            if not is_valid_string(password):
                print("Error: Only letters allowed.")
                continue

            result = send_and_receive(encryption, f"PASS {password.upper()}")
            if result.startswith("RESULT"):
                print("Password set.")
            else:
                print("Error:", result[6:])

        elif choice == "encrypt" or choice == "2":
            print("\nUse a string from history? (y/n)")
            use_hist = input("> ").strip().lower()

            if use_hist == 'y' and history:
                for i, item in enumerate(history):
                    print(f"{i+1}. {item}")
                print("0. Enter new string")
                try:
                    idx = int(input("Select number: ").strip())
                    if idx == 0:
                        text = input("Enter string to encrypt: ").strip()
                    else:
                        text = history[idx - 1]
                except:
                    print("Invalid selection.")
                    continue
            else:
                text = input("Enter string to encrypt: ").strip()

            if not is_valid_string(text):
                print("Error: Only letters allowed.")
                continue

            history.append(text)
            result = send_and_receive(encryption, f"ENCRYPT {text.upper()}")
            if result.startswith("RESULT"):
                encrypted = result[7:]
                print("Encrypted:", encrypted)
                history.append(encrypted)
                log("ENCRYPT", f"{text.upper()} -> {encrypted}")
            else:
                print("Error:", result[6:])
                log("ERROR", result[6:])

        elif choice == "decrypt" or choice == "3":
            print("\nUse a string from history? (y/n)")
            use_hist = input("> ").strip().lower()

            if use_hist == 'y' and history:
                for i, item in enumerate(history):
                    print(f"{i+1}. {item}")
                print("0. Enter new string")
                try:
                    idx = int(input("Select number: ").strip())
                    if idx == 0:
                        text = input("Enter string to decrypt: ").strip()
                    else:
                        text = history[idx - 1]
                except:
                    print("Invalid selection.")
                    continue
            else:
                text = input("Enter string to decrypt: ").strip()

            if not is_valid_string(text):
                print("Error: Only letters allowed.")
                continue

            history.append(text)
            result = send_and_receive(encryption, f"DECRYPT {text.upper()}")
            if result.startswith("RESULT"):
                decrypted = result[7:]
                print("Decrypted:", decrypted)
                history.append(decrypted)
                log("DECRYPT", f"{text.upper()} -> {decrypted}")
            else:
                print("Error:", result[6:])
                log("ERROR", result[6:])

        elif choice == "history" or choice == "4":
            print("\nHistory:")
            for i, item in enumerate(history):
                print(f"{i+1}. {item}")

        elif choice == "quit" or choice == "5":
            send_and_receive(encryption, "QUIT")
            logger.stdin.write("QUIT\n")
            logger.stdin.flush()
            log("EXIT", "Driver shutting down.")
            print("Byeeeee <3.")
            break

        else:
            print("Invalid option.")
            log("ERROR", "Invalid menu selection.")

    encryption.wait()
    logger.wait()

if __name__ == "__main__":
    main()
