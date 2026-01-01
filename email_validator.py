"""Email validation utilities."""

import re

def is_valid_email(email):
    """Validate email format using regex pattern."""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def is_valid_domain(email):
    """Check if email has a valid domain."""
    if '@' not in email:
        return False
    domain = email.split('@')[1]
    return '.' in domain and len(domain) > 3

def normalize_email(email):
    """Convert email to lowercase and strip whitespace."""
    return email.strip().lower()

def batch_validate_emails(emails):
    """Validate a list of emails and return valid/invalid lists."""
    valid = []
    invalid = []
    for email in emails:
        if is_valid_email(email):
            valid.append(email)
        else:
            invalid.append(email)
    return {'valid': valid, 'invalid': invalid}
