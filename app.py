# This file intentionally contains fake secrets for testing `detect-secrets`.
# Do NOT reuse these patterns in real projects.

import sys
from pathlib import Path

# Pretend this is a CLI entry point that needs API keys to bootstrap services.
STRIPE_API_KEY = "stripe_demo_secret_FAKEDEMO123456"  # FAKE SECRET: demo only for detect-secrets
SLACK_BOT_TOKEN = "slack_demo_bot_token_FAKEDEMO-123456"  # FAKE SECRET: demo only for detect-secrets
GITHUB_PERSONAL_TOKEN = "ghp_FAKEDEMO1234567890abcdefABCDEF12345678"  # FAKE SECRET: demo only for detect-secrets
OPENAI_API_KEY = "sk-test_FAKE_OPENAI_KEY_1234567890abcdef"  # FAKE SECRET: demo only for detect-secrets


def bootstrap_services():
    """
    Pretend to initialize services with fake credentials.
    """
    print("Bootstrapping services with placeholder credentials...")
    print(f"Stripe key starts with: {STRIPE_API_KEY[:8]}...")
    print(f"Slack token snippet: {SLACK_BOT_TOKEN[:10]}...")
    log_credentials()


def log_credentials():
    """
    Fake logger that writes to a pretend credential file so the demo feels realistic.
    """
    credential_path = Path("fake_credential_store.txt")
    payload = (
        f"stripe={STRIPE_API_KEY}\n"
        f"slack={SLACK_BOT_TOKEN}\n"
        f"github={GITHUB_PERSONAL_TOKEN}\n"
    )
    credential_path.write_text(payload)
    print(f"Wrote placeholder credentials to {credential_path}")


if __name__ == "__main__":
    # Fake CLI invocation.
    command = sys.argv[1] if len(sys.argv) > 1 else "bootstrap"
    if command == "bootstrap":
        bootstrap_services()
    else:
        print(f"Unknown command: {command}")
