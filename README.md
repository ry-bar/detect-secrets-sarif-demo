# detect-secrets SARIF Demo

This repository is a tiny Python codebase that intentionally contains **17 fake secrets** across at least five secret types so we can demonstrate a GitHub Actions workflow that:

1. Runs [Yelp's `detect-secrets`](https://github.com/Yelp/detect-secrets) scanner.
2. Converts the findings to SARIF using [`ry-bar/detect-secrets-sarif-action`](https://github.com/ry-bar/detect-secrets-sarif-action).
3. Uploads the SARIF file to GitHub Code Scanning via [`github/codeql-action/upload-sarif`](https://github.com/github/codeql-action).

## Important disclaimer!!

- **All secrets in this repository are 100% fake and for educational testing only.**
- There are **17 deliberate fake vulnerabilities/secrets** seeded throughout the codebase so scanners have plenty to find.
- Do not copy any of these patterns into real projects.
- The code is intentionally simplistic—its only job is to look like a plausible app with hard-coded secrets so `detect-secrets` has something to find.

## Files

- `app.py`: Pretend CLI entry point referencing fake API keys.
- `config_example.py`: Mock configuration module packed with obviously bad credentials.
- `secrets_example.py`: Contains a fake private key, bearer token, and JWT-like token.
- `.github/workflows/security-scan-demo.yml`: GitHub Actions workflow that runs the scan, converts it to SARIF, and uploads it.

## Seeded fake secrets

Each fake secret is deliberately chosen to look like a high-signal pattern for scanners:

1. **`app.py` – Stripe API key**: Mimics an `sk_` style Stripe secret key.
2. **`app.py` – Slack bot token**: Looks like an `xoxb-` bot token to demonstrate chat tokens.
3. **`app.py` – GitHub personal access token**: Uses a `ghp_`-style prefix so PAT detectors fire.
4. **`config_example.py` – Primary database URL**: Hard-coded `postgres://user:[REDACTED]@host` connection string.
5. **`config_example.py` – Read-only database URL**: Second DB string to show multiple credentials in one file.
6. **`config_example.py` – AWS access key ID**: Uppercase alphanumeric value styled like a real key ID.
7. **`config_example.py` – AWS secret access key**: Companion secret to mirror the typical pair.
8. **`config_example.py` – Jira admin username**: Hard-coded service-account username example.
9. **`config_example.py` – Jira admin password**: Password string with punctuation to trigger detectors.
10. **`config_example.py` – GitHub App client ID**: `Iv1.` prefix as seen in real GitHub App credentials.
11. **`config_example.py` – GitHub App client secret**: Long lowercase/number string for secret scanning.
12. **`config_example.py` – Twilio auth token**: Hex-like token resembling auth secrets.
13. **`config_example.py` – Stripe signing secret**: `whsec_` prefix like webhook signing secrets.
14. **`secrets_example.py` – Private key block**: PEM-formatted key that any scanner should catch.
15. **`secrets_example.py` – JWT session token**: Three-part dot-separated token showing JWT structure.
16. **`secrets_example.py` – Bearer token**: `Bearer ...` string to mimic service-to-service tokens.
17. **`secrets_example.py` – Azure storage connection string**: Includes an `AccountKey` field with base64-ish value.