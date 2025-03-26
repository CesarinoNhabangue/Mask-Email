import re

def mask_email(email):

    if not email or '@' not in email:
        return "Invalid email format"
    
    # Split the email into username and domain
    username, domain = email.split('@', 1)
    
    # Handle short usernames
    if len(username) <= 2:
        masked_username = username[0] + '*' * len(username)
    else:
        # Show first and last character, mask the rest
        masked_username = username[0] + '*' * (len(username) - 2) + username[-1]
    
    return f"{masked_username}@{domain}"

# Examples
emails = [
    "john.doe@example.com",
    "alice.smith@gmail.com",
    "bob@yahoo.co.uk",
    "contact@company.org",
    "a@b.com"  # Short username example
]

for email in emails:
    print(f"Original: {email}")
    print(f"Masked:   {mask_email(email)}")
    print()