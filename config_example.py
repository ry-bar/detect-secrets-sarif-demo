# This file intentionally contains fake secrets for testing `detect-secrets`.
# Do NOT reuse these patterns in real projects.

# Pretend configuration module full of sensitive values.
DATABASE_CONFIG = {
    "url": "postgres://demo_user:SuperSecretPass123@db.example.local:5432/demo",  # FAKE SECRET: demo only for detect-secrets
    "readonly_url": "postgres://readonly:ReadOnlyPass987@db.example.local:5432/demo",  # FAKE SECRET: demo only for detect-secrets
}

AWS_CREDENTIALS = {
    "aws_access_key_id": "AKIAFAKEACCESSKEY1234",  # FAKE SECRET: demo only for detect-secrets
    "aws_secret_access_key": "fakeAWSsecretKeyValue987654321",  # FAKE SECRET: demo only for detect-secrets
}

SERVICE_ACCOUNTS = {
    "jira": {
        "api_token": "jira_demo_api_token_FAKE1234567890",  # FAKE SECRET: demo only for detect-secrets
        "password": "JiraAdminPass!@#2024",  # FAKE SECRET: demo only for detect-secrets
    },
    "github_app": {
        "client_id": "Iv1.abcdef1234567890",  # FAKE SECRET: demo only for detect-secrets
        "client_secret": "fakegithubclientsecret987654321",  # FAKE SECRET: demo only for detect-secrets
    },
}

API_KEYS = {
    "twilio_auth_token": "twilio_demo_auth_token_FAKE1234567890",  # FAKE SECRET: demo only for detect-secrets
    "stripe_signing_secret": "stripe_signing_secret_demo_value_123456",  # FAKE SECRET: demo only for detect-secrets
}


def print_config_summary():
    """
    Print a harmless summary so the module looks realistic.
    """
    print(f"Configured database host: {DATABASE_CONFIG['url'].split('@')[-1]}")
    print(f"Service accounts available: {', '.join(SERVICE_ACCOUNTS.keys())}")
