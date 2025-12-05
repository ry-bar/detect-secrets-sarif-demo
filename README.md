# detect-secrets SARIF Demo

This repository is a tiny Python codebase that intentionally contains fake secrets so we can demonstrate a GitHub Actions workflow that:

1. Runs [Yelp's `detect-secrets`](https://github.com/Yelp/detect-secrets) scanner.
2. Converts the findings to SARIF using [`ry-bar/detect-secrets-sarif-action`](https://github.com/ry-bar/detect-secrets-sarif-action).
3. Uploads the SARIF file to GitHub Code Scanning via [`github/codeql-action/upload-sarif`](https://github.com/github/codeql-action).

## Important disclaimer!!

- **All secrets in this repository are 100% fake and for educational testing only.**
- Do not copy any of these patterns into real projects.
- The code is intentionally simplistic—its only job is to look like a plausible app with hard-coded secrets so `detect-secrets` has something to find.

## Files

- `app.py`: Pretend CLI entry point referencing fake API keys.
- `config_example.py`: Mock configuration module packed with obviously bad credentials.
- `secrets_example.py`: Contains a fake private key, bearer token, and JWT-like token.
- `.github/workflows/security-scan-demo.yml`: GitHub Actions workflow that runs the scan, converts it to SARIF, and uploads it.

Run `detect-secrets scan` locally if you want to debug changes before pushing.
