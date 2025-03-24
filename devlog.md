"# Devlog" 

2025-03-25 00:00
Started working on logger a while ago, but just starting to set up git repo. planning on splitting up into logger, encryption, and driver and working that way. 

Here are my notes I took from when I started working on the Logger, that I had written in a different document, adding them to my devlog after first commit

March 22, 2025, 8:30 PM
Thoughts so far: Starting the logger component. It should take a log file name as a command-line argument and write logs received from stdin. Planning to begin with something really basic and expand from there.

March 22 2025, 9:15 PM
Hit a few small issues. Forgot to handle the case where the user doesn't give a log filename, so I added a usage message and early exit. Also had to Google how to format timestamps correctly using datetime. Took a little longer than expected


March 22, 2025, 10:05 PM
Got the base logger working. It takes input from stdin, writes it to a file, and stops on "QUIT". The file was not updating until I remembered to flush the output stream after writing. That took a while to figure out.


March 23, 2025, 12:18 AM
Commit 1: Bare bones logger that reads stdin and writes raw messages to a file with QUIT support
Thoughts before continuing: Now that the basic logger works, I want to format each line properly. I need to split each line into an action and the rest of the message. Also planning to add input validation in case the line is malformed.


March 23, 2025, 12:30 AM
Added split logic for separating action and message. I was getting index errors at first when the input did not have a space, so I added a check to skip lines that do not split into two parts. Also tested the timestamp formatting and it seems to match the required format. Trying different sample inputs now.


March 23, 2025, 1:00 AM
Commit 2: Final logger implementation with timestamp, action/message split, and error handling

March 23, 2025, 8:00 AM
Thoughts so far: Starting the encryption module. The program will receive commands from stdin and respond to stdout. Commands include PASS, ENCRYPT, DECRYPT, and QUIT. 

March 23, 2025, 8:15 AM
Reviewed the logic again. Key wraps around the input. Planning to use modular arithmetic to handle character shifting. Will keep everything uppercase for simplicity.

March 23, 2025, 8:35 AM
Wrote stubs for vigenere_encrypt and vigenere_decrypt. Unsure about wrapping logic but will test with simple strings. Using key should work.

March 23, 2025, 9:00 AM
Started implementing vigenere_encrypt. Found some issues with ASCII math at first but got a basic version working for all-uppercase letters.

March 23, 2025, 9:25 AM
Decryption was failing due to negative values. Fixed by wrapping with modulo 26 after subtracting the shift value. Seems to decrypt properly now.

March 23, 2025, 9:50 AM
Confirmed HELLO with key KEY encrypts to RIJVS. Matches expected output. Decryption also returns original string now.

March 23, 2025, 10:10 AM
Began writing main input loop. Using readline from stdin. Also converting to uppercase early in the process.

March 23, 2025, 10:30 AM
Implemented input parsing using split(maxsplit=1) to separate the command and the argument. Will handle malformed input next.

March 23, 2025, 10:55 AM
PASS command implemented. Stores the current passkey. Added isalpha check to validate passkey format.

March 23, 2025, 11:10 AM
ENCRYPT and DECRYPT working with stored passkey. Added error if user tries to encrypt or decrypt without setting a passkey.

March 23, 2025, 11:45 AM
Added error checking to reject strings with non-alphabet characters. Using str.isalpha() to enforce it.

March 23, 2025, 12:15 PM
Added flush=True to all print statements. Without it, output was delayed or missing when piping to subprocess.

March 23, 2025, 12:45 PM
Tested several combinations of PASS, ENCRYPT, and DECRYPT. Results are consistent and match expectations.

March 23, 2025, 1:30 PM
Added fallback case for unknown commands. Program now prints "ERROR Unknown command" if command isn't recognized.

March 23, 2025, 2:00 PM
Verified that QUIT command exits cleanly. Removed some test print statements and added more checks for edge cases.

March 23, 2025, 2:30 PM
Tested running ENCRYPT and DECRYPT back-to-back. No issues. Passkey is being stored and reused correctly across commands.

March 23, 2025, 3:00 PM
Cleaned up whitespace and made sure all inputs are forced to uppercase. Added strip() to avoid trailing newline issues.

March 23, 2025, 4:15 PM
Revisited encryption and decryption logic one more time. Confirmed outputs again with new test cases.

March 23, 2025, 5:15 PM
Did final testing of all commands. PASS, ENCRYPT, DECRYPT, and QUIT all work. Error messages trigger when expected.

March 23, 2025, 5:45 PM
Commit: Final working encryption program with passkey storage, input validation, cipher logic, and proper error/flush handling.


March 23, 2025, 6:00 PM
Thoughts so far: Starting on the driver program. This will be the main program that launches the logger and encryption modules as subprocesses. It will also handle user interaction through a menu. Planning to begin by getting the subprocesses launched.

March 23, 2025, 6:10 PM
Set up the skeleton for the driver script. Parsed the log file name from sys.argv and added a usage message if it's missing.

March 23, 2025, 6:20 PM
Using subprocess.Popen to start the logger and encryption programs. Redirected stdin and stdout as needed. Still need to confirm communication between processes.

March 23, 2025, 6:35 PM
Added helper function to send a message to encryption and receive a response from stdout. Flushing the encryption stdin to make sure the message goes through.

March 23, 2025, 6:50 PM
Built a log() function that sends timestamped messages to the logger. For now, just testing that START gets logged properly when the program launches.

March 23, 2025, 7:00 PM
Started writing the main command menu. Prompting the user to choose from password, encrypt, decrypt, history, and quit.

March 23, 2025, 7:10 PM
Implemented initial input loop. Each command string gets logged before being handled. Still stubbed out the logic for what happens in each case.

March 23, 2025, 7:15 PM
Added a history list to store input strings and results. This will be session-only and allow selection from previous entries.

March 23, 2025, 7:20 PM
Began work on the password command. Prompting for a new string or choosing from history. Havent linked to encryption subprocess yet.

March 23, 2025, 7:30 PM
Hooked up the PASS command to encryption. Sends PASS to the subprocess. Prints feedback to the user depending on RESULT or ERROR.

March 23, 2025, 7:40 PM
Input validation added to password input. Using regex to make sure input only contains alphabetic characters. Logs error if not valid.

March 23, 2025, 7:50 PM
Encrypt command now working. Prompts for new string or allows user to pick from history. Sends ENCRYPT to subprocess and stores the result in history.

March 23, 2025, 8:00 PM
Tested encrypt command with HELLO and password KEY. Got the correct result back. Logs the original and encrypted string.

March 23, 2025, 8:05 PM
Added the decrypt command using the same logic as encrypt. Result is also stored in history. Using DECRYPT command to encryption process.

March 23, 2025, 8:10 PM
Confirmed that encrypt and decrypt both store input and output in history. This allows them to be reused in later operations.

March 23, 2025, 8:20 PM
Tested edge cases for history selection. Added try/except to handle non-integer or invalid indexes in selection menus.

March 23, 2025, 8:30 PM
Added option 0 to all history menus for entering a new string. This gives flexibility and matches project spec.

March 23, 2025, 8:40 PM
Added the history command. Just prints each item in the history list with numbering. Useful for tracking whats been entered so far.

March 23, 2025, 8:45 PM
Input to all menu choices now case-insensitive. Users can type either the number or the full command name in any case.

March 23, 2025, 8:50 PM
Added QUIT handling. Sends QUIT to both subprocesses and exits cleanly. Also logs the shutdown as an EXIT event.

March 23, 2025, 9:00 PM
Tested full session from start to finish. Everything worked as expected. Menu responds to each command, subprocesses communicate properly, and logs are created.

March 23, 2025, 9:10 PM
Minor refactor of repeated history code. Created helper function to reduce redundancy between encrypt, decrypt, and password commands.

March 23, 2025, 9:20 PM
Improved error messages for invalid menu selections. Logs an error if a user enters something invalid.

March 23, 2025, 9:30 PM
Ensured that passwords are not stored in history or logged. This was required in the spec. Confirmed they are only used for PASS.

March 23, 2025, 9:35 PM
Did another full walkthrough with test inputs. History builds up as expected and can be reused. All outputs are clean and aligned.

March 23, 2025, 9:40 PM
Commit: Final version of driver with full menu support, subprocess communication, logging, history management, input validation, and shutdown



