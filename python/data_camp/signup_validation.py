"""
Data Camp Project ID 2198
Title: "Building Core Sign-Up Functions to Help Validate New Users
"""
top_level_domains = [
    ".org",
    ".net",
    ".edu",
    ".ac",
    ".gov",
    ".com",
    ".io"
]

# Start coding here. Use as many cells as you need.
def validate_name(name):
    if type(name) == str and len(name) > 2:
        return True
    
    else:
        return False
    

def validate_email(email):
    if type(email) == str and '@' in email and top_level_domain in email:
        return True
    
    else:
        return False
    