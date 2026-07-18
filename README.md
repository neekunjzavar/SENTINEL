# SENTINEL

Autonomous application-security agent: scans an authorized target with real security tooling (ZAP, semgrep, nuclei), reasons about the findings, and drafts remediation as a pull request.

**Status:** environment setup (see below). No agent code yet.

## Scope & ethics

Only ever run against apps we own or intentionally-vulnerable training targets (OWASP Juice Shop, DVWA). Scope-locking is enforced in code, not just policy — see `orchestrator/scope.py` once it exists.

## Setup checklist

- [ ] Anthropic API key (console.anthropic.com)
- [ ] Docker Desktop installed
- [ ] Juice Shop running locally (`docker run`)
- [ ] GitHub repo connected as remote

## Architecture (target)

```
Recon (ZAP spider) -> Orchestrator agent -> Analysis/RAG (OWASP/CWE grounding) -> Remediation agent -> PR
                                          -> Dashboard (React)
```
