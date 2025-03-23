import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 logger.py <log_filename>")
        sys.exit(1)

    log_filename = sys.argv[1]

    try:
        with open(log_filename, 'a') as logfile:
            while True:
                line = sys.stdin.readline()
                if not line:
                    break

                line = line.strip()
                if line == "QUIT":
                    break

                logfile.write(line + '\n')
                logfile.flush()

    except Exception as e:
        print(f"ERROR: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
