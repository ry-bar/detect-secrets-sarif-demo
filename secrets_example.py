# This file intentionally contains fake secrets for testing `detect-secrets`.
# Do NOT reuse these patterns in real projects.

# Private key block that should be flagged by scanners.
FAKE_PRIVATE_KEY = """-----BEGIN PRIVATE KEY-----
MIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDEMOCKFAKEKEY1
8W9JqJ9gdmotKkB3h0d6Vgmm6JYh2n6f6l4j/Cxi7e1Bsv5pBQv0n78Qr0+2ZgZy
ynDA5jTAVf9K8hJFRIl7ga2PSa7dRLXBGdr9PnaqkBSbnYQUSdTVz7gmVMf+3+2q
oIIgxsDvw7DDf+QOSwrj9mNoWiWgPDGEHfX4mW50lR+uFAKEuZY4gdIjMAV1xN5F
FAKEKEYLINEKEEPSTHISFAKEONLY3kNn2A0kAZjZyKJwIDAQABAoIBAEuu5X6fake
oz7q9k16jLw9UlScwkvdQ1xwDA3lGlEPTP2r0y7Vv6wYr2m3eVZJFAKEKEYLINE
-----END PRIVATE KEY-----"""  # FAKE SECRET: demo only for detect-secrets

# Fake JWT token representing a session cookie.
JWT_SESSION_TOKEN = (
    "eyFake.JwtPayload.SignaturePartThatLooksRealButIsNot"  # FAKE SECRET: demo only for detect-secrets
)

# Fake bearer token used for an internal service.
INTERNAL_BEARER_TOKEN = "Bearer faketoken1234567890ABCDEFGHIJKLMNOP"  # FAKE SECRET: demo only for detect-secrets

# Pretend connection string for Azure storage.
AZURE_STORAGE_CONNECTION = (
    "DefaultEndpointsProtocol=https;AccountName=fakedemo;"
    "AccountKey=FAKEAzuReAccountKeyValue1234567890==;EndpointSuffix=core.windows.net"
)  # FAKE SECRET: demo only for detect-secrets


def dump_secret_lengths():
    """
    Return lengths so linting tools feel like this is used.
    """
    return {
        "private_key_len": len(FAKE_PRIVATE_KEY),
        "jwt_len": len(JWT_SESSION_TOKEN),
        "bearer_len": len(INTERNAL_BEARER_TOKEN),
    }
