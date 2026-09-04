---
name: n8n-credentials-and-security-official
description: Use when an n8n workflow needs authentication, credentials, API keys, OAuth, bearer tokens, or any secret value.
---

# n8n Credentials and Security

## Invariants

- Put secrets only in n8n credentials. Never place them in node parameters, expressions, SDK code, chat output, logs, pin data, or workflow exports.
- Never request, display, recover, or return credential secret values. Credential metadata and IDs are sufficient for binding.
- A credential label in workflow code is cosmetic; discover and bind the actual credential ID.
- If a user pastes a secret, do not repeat it. Explain that it must be stored in n8n and continue with placeholders or credential discovery.

## Workflow

1. Prefer the native service node and its credential type.
2. Otherwise use HTTP Request with an official credential type. Use generic Header Auth, Query Auth, or OAuth only when no service credential applies.
3. Call `list_credentials` with the needed type/project filters. If multiple plausible credentials remain and the choice changes the account or environment, ask which one; do not ask for the secret or cosmetic label.
4. Fetch the node's live parameter shape, set its authentication discriminator, then bind the credential ID with the supported credential operation.
5. Validate the node and workflow. Test only within the user's authorized side-effect scope.

## Stop rules

- Stop before sending a secret into any non-credential field or output.
- Stop and explain when no safe credential mechanism exists; do not fall back to hardcoding.
- Do not create credentials programmatically. If the required credential is absent, tell the user the exact type to create or authorize in the n8n UI, then resume after it exists.

## Selective references

- Read [references/CREDENTIAL_SYSTEM.md](references/CREDENTIAL_SYSTEM.md) for credential discovery and binding.
- Read [references/HTTP_REQUEST_WITH_AUTH.md](references/HTTP_REQUEST_WITH_AUTH.md) for authenticated HTTP Request setup.
- Read [references/CUSTOM_CREDENTIALS.md](references/CUSTOM_CREDENTIALS.md) when no built-in credential type fits.
- Read [references/FINDING_API_DOCS.md](references/FINDING_API_DOCS.md) when the upstream auth scheme is unclear.
- Read [references/DETAILED_GUIDE.md](references/DETAILED_GUIDE.md) for the original decision tree and examples.
