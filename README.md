# karolina-python-project-1

## Business description
The purpose of this project is to build a tool that enables users to perform a visual analysis of data from messanger.
Clients of this application are other techinical users which would use this tool from a command line.

## Project requirements

### Functional requirements
- Script is run from a command line that starts the application.
- User provides a path to a json file in the following format...
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
...
