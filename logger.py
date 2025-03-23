import sys
import datetime

def get_timestamp():
    now = datetime.datetime.now()
    return now.strftime("%Y-%m-%d %H:%M")

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

                if line == "":
                    continue

                parts = line.split(maxsplit=1)
                if len(parts) < 2:
                    continue  # skip malformed input

                action = parts[0]
                message = parts[1]
                timestamp = get_timestamp()
                logfile.write(f"{timestamp} [{action}] {message}\n")
                logfile.flush()

    except Exception as e:
        print(f"ERROR: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
