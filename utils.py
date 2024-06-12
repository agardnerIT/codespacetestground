import os
import hashlib
import requests

GITHUB_ORG_SLASH_REPOSITORY = os.environ.get("GITHUB_REPOSITORY") # eg. yourOrg/yourRepo

def hash_string(input_str, charset="UTF-8", algorithm="SHA256"):
    hash_factory = hashlib.new(algorithm)
    hash_factory.update(input_str.encode(charset))
    return hash_factory.hexdigest()

def send_startup_ping(codespace_mode: str):
    ## 1. Take lowercase GITHUB_ORG_SLASH_REPO and lowercase it.
    ## 2. For user privacy, calculate an irreversible one-way hash of this string
    hashed_org_slash_repo = hash_string(input_str=GITHUB_ORG_SLASH_REPOSITORY.lower(), charset="UTF-8", algorithm="SHA256")

    # testing_mode str to bool
    testing = False
    if codespace_mode == "testing":
        testing = True
    
    # Build content and send request
    url = "https://ljj95gnqj2.execute-api.us-east-1.amazonaws.com/default/ag-platform-engineering-codespace-bizevent-tracker"

    headers = {
        "User-Agent": "GitHub",
        "Content-Type": "application/json"
    }

    body = {
        "repo": hashed_org_slash_repo,
        "testing": testing
    }

    resp = requests.post(
        url=url,
        headers=headers,
        json=body
    )