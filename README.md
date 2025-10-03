# Messenger annalizer 

## Business description
Messenger provides a possibility to generate json files which contain the whole conversation history.
The purpose of this project is to build a tool that enables users to perform a visual analysis of this data from messanger.
Clients of this application are other analysists which would use this tool from a command line.

## Project requirements

### Functional requirements
- Script 'run.sh' is run from a command line that starts the application.
- The application is a command line program, it means that inputs are provided in console and output are also displayed in console. 
- User provides a path to a json file in the following: [messages.schema.json](https://github.com/wezdenko/karolina-python-project-1/blob/main/message.schema.json)
- User can perform 3 operations:
  - Count all messages in the given period (accepted date format: `YYYY-MM-DD`) and display the number.
  - Count number of messages sent by each user in the given period (accepted date format: `YYYY-MM-DD`) and display the number. Results should be ordered in a
    descening order and displayed in the following format: `{user_name}: {message_count}`
  - Count number of occurrences for each word and display top 'n' results sorted in a decreasing order (the grouping of words should be case-insensitive).
    The 'n' is a positive integer defined by a user. Results should be displayed in a console in the following format: `{order_number}. {word}: {word_count}`
- After successful operation user can perform another operation.
- In case of error caused by input from the user the program should print the error message and repeat the last question.
- In case of error caused by json file the program should print the error message and exit.
- User can exit the program at any time using Ctrl+C.

### Non-functional requirements
- Program always runs correctly as long the input and json file is correct.
- Program uses python in version 3.12.
- Only modules from a [standard library](https://docs.python.org/3.12/library/index.html) can be used.
- The program is easy to set-up and run (documentation for that is provided).
- Program handles json files up to 5MB in size.
- Program is well maintained in this repository.
