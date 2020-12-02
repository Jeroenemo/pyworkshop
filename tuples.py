# Unpacking a tuple use _ to omit end values. Does stack. 

student =("Marcy", 11, "History", 3.5, [5,4], 'yo')
name, age, subject, gpa, _, _ = student

def http_status_code():
    return 200, 'OK'

code, name = http_status_code()