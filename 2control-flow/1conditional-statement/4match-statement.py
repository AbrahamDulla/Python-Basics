# Python does not have a built-in switch statement.
# However, you we use the if-elif-else construct to implement
# the functionality of a switch statement.

# But we can use something called a match case statement
# we can use a match statement as an alternative to an if statement.
# The match statement In Python was introduced in version 3.10

# example

http_status = 400

match http_status:
    case 200 | 201:
        print("Success")
    case 400:
        print("Bad request")
    case 500 | 501:
        print("Server Error")
    case _:
        print("Unknown Error")
