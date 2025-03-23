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
