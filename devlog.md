"# Devlog" 

## 2025-03-25 00:00
Started working on logger a while ago, but just starting to set up git repo. planning on splitting up into logger, encryption, and driver and working that way. 

Here are my notes I took from when I started working on the Logger, that I had written in a different document, adding them to my devlog after first commit

## March 22, 2025, 8:30 PM
Thoughts so far: Starting the logger component. It should take a log file name as a command-line argument and write logs received from stdin. Planning to begin with something really basic and expand from there.

## March 22 2025, 9:15 PM
Hit a few small issues. Forgot to handle the case where the user doesn't give a log filename, so I added a usage message and early exit. Also had to Google how to format timestamps correctly using datetime. Took a little longer than expected


## March 22, 2025, 10:05 PM
Got the base logger working. It takes input from stdin, writes it to a file, and stops on "QUIT". The file was not updating until I remembered to flush the output stream after writing. That took a while to figure out.


## March 23, 2025, 12:18 AM
Commit 1: Bare bones logger that reads stdin and writes raw messages to a file with QUIT support
Thoughts before continuing: Now that the basic logger works, I want to format each line properly. I need to split each line into an action and the rest of the message. Also planning to add input validation in case the line is malformed.


## March 23, 2025, 12:30 AM
Added split logic for separating action and message. I was getting index errors at first when the input didn’t have a space, so I added a check to skip lines that don’t split into two parts. Also tested the timestamp formatting and it seems to match the required format. Trying different sample inputs now.


## March 23, 2025, 1:00 AM
Commit 2: Final logger implementation with timestamp, action/message split, and error handling
