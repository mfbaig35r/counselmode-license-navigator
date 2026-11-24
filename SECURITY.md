# Security

## Reporting a vulnerability

Report it privately through GitHub:
[**Report a vulnerability**](https://github.com/mfbaig35r/counselmode-license-navigator/security/advisories/new)
(also under this repository's Security tab). Only the maintainers can see the report. Please don't open a public issue
for a security problem.

Include what you found, where (the hosted server, the PyPI package, or this repository), and how to reproduce it. You
will get a reply acknowledging the report, and updates until it is resolved. If you'd like credit in the release
notes for the fix, say how you'd like to be named.

## What's in scope

- The hosted server at `https://licenses.counselmode.com/mcp`.
- The `counselmode-licenses` package on PyPI, latest release.
- The code and workflows in this repository.

The hosted server is read-only and stateless: it has no accounts, stores nothing, and keeps no record of questions.
Reports that show otherwise, such as a request that changes data, reaches files that should not be served, or leaves
a trace of what someone asked, are exactly what we want to hear about.

## Not security issues

A wrong or outdated license answer is a data problem, not a vulnerability. Please report it with the
[wrong-answer issue template](https://github.com/mfbaig35r/counselmode-license-navigator/issues/new/choose) so the fix
is visible to everyone.

## Supported versions

Only the latest release on PyPI, and the hosted server, which always runs it.
