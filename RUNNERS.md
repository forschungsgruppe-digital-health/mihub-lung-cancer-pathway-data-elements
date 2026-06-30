# CI runners (self-hosted fallback)

> CI for this repo uses **GitHub-hosted runners** (`runs-on: ubuntu-latest`), which are **free and
> unlimited for public repositories**. This document is the fallback for the **interim period while
> the repo is still private** and the org's GitHub-hosted Actions are blocked by a billing/
> spending-limit failure. It mirrors the sibling patient-portal's
> [`deploy/RUNNER.md`](https://github.com/forschungsgruppe-digital-health/cross-hub-patientportal)
> but is much lighter (this repo's jobs are Python-only — no Docker, browser, or Java).

## TL;DR — which runner, when?

| Repo state | Runner | Why |
|---|---|---|
| **Public** (the target — see [`docs/go-public-checklist.md`](docs/go-public-checklist.md)) | `ubuntu-latest` (GitHub-hosted) | Free + unlimited for public repos; zero maintenance; matches the public sibling `mihub-lung-cancer-pathway`. |
| **Private (now)**, CI wanted | **self-hosted** (this doc) | GitHub-hosted is blocked org-wide (billing) → a self-hosted runner unblocks CI until the repo is public or billing is restored. |
| **Private**, CI optional | none | Verify locally and merge without CI — a private no-Pro repo has no required-check branch protection. |

## Why this is needed today

GitHub-hosted runners are blocked org-wide by an Actions **billing / spending-limit** failure —
every job fails in **~4 s with no logs**. (Same root cause documented for the sibling patient-portal
repo, which moved CI to the self-hosted runner `gksax`, PR #141.) Until the org's
**Settings → Billing & plans** is resolved — or this repo is made public — no GitHub-hosted job can
start.

## ⚠ Public-repo security — read before going public

GitHub **strongly discourages** self-hosted runners on **public** repositories: a pull request from
a fork can execute arbitrary code on the runner host. The public sibling
`mihub-lung-cancer-pathway` uses `ubuntu-latest` for exactly this reason. Therefore:

- **When this repo goes public, revert the workflows to `runs-on: ubuntu-latest`** (free, sandboxed)
  and **deregister/remove** any self-hosted runner.
- If a self-hosted runner is unavoidable on a public repo, first require approval for fork-PR runs:
  **Settings → Actions → General → "Require approval for all outside collaborators"** (or "…for all
  external contributors").

## What the jobs need (host prerequisites)

This repo's workflows are minimal — `validate.yml`, `skill-lint.yml`, `duplicate-check.yml`,
`citation-validate.yml`, `link-check.yml`. Python is installed **per job** by
`actions/setup-python`; the other tools (cff-validator, lychee) are pulled as actions. The host only
needs the runner basics: **`git`, `bash`, `curl`, `tar`** (Linux x64). No Docker, no browser, no Java.

## Register a self-hosted runner

Scope can be **repository-level** (this repo only) or **org-level** (shared by all FGDH repos —
preferred if an org runner like the patient-portal's `gksax` already exists; just make it visible to
this repo instead of installing a new one).

1. As a non-root **service user**, download the runner (latest:
   <https://github.com/actions/runner/releases>):
   ```bash
   sudo mkdir -p /srv/actions-runner && sudo chown "$USER" /srv/actions-runner
   cd /srv/actions-runner
   curl -o actions-runner.tar.gz -L \
     https://github.com/actions/runner/releases/download/v<X.Y.Z>/actions-runner-linux-x64-<X.Y.Z>.tar.gz
   tar xzf actions-runner.tar.gz
   ```
2. Get a **registration token** — repo **Settings → Actions → Runners → New self-hosted runner**, or:
   ```bash
   # repository-level:
   gh api -X POST repos/forschungsgruppe-digital-health/mihub-lung-cancer-pathway-data-elements/actions/runners/registration-token --jq .token
   # org-level:
   gh api -X POST orgs/forschungsgruppe-digital-health/actions/runners/registration-token --jq .token
   ```
3. Configure (work folder **must** be `_work`):
   ```bash
   ./config.sh \
     --url https://github.com/forschungsgruppe-digital-health/mihub-lung-cancer-pathway-data-elements \
     --token <REGISTRATION_TOKEN> \
     --name <runner-name> \
     --labels self-hosted,Linux,X64 \
     --work _work --unattended
   ```
4. Install + start as a systemd service (auto-starts on boot):
   ```bash
   sudo ./svc.sh install "$USER"
   sudo ./svc.sh start
   sudo ./svc.sh status     # expect "active (running)" + "Listening for Jobs"
   ```

Confirm online: repo **Settings → Actions → Runners**, or
`gh api repos/forschungsgruppe-digital-health/mihub-lung-cancer-pathway-data-elements/actions/runners`.

## Point the workflows at the runner

In each `.github/workflows/*.yml`, change `runs-on: ubuntu-latest` → `runs-on: self-hosted` (or a
custom label). **Revert to `ubuntu-latest` when going public** (see the security note above).

## Operating notes

- **Single runner ⇒ jobs run serially** — fine here (jobs are short, bind no ports).
- **Persistent state** between jobs (unlike ephemeral hosted VMs). If `_work` grows, prune it
  periodically; nothing here needs a Docker prune.

## Troubleshooting

| Symptom | Cause | Fix |
|---|---|---|
| Checks stuck `queued` forever | runner offline, or `runs-on` targets a label with no runner | start the service (`sudo ./svc.sh start`); or set `runs-on: ubuntu-latest` |
| All jobs fail in ~4 s, no logs | job ran on a GitHub-hosted runner (billing block) | ensure `runs-on: self-hosted`, **or** make the repo public (hosted becomes free) |
| Runner crash-loops creating the `_diag` log | the service user can't write the runner dir (root-owned files from a `sudo` run) | `sudo chown -R <service-user>:<service-user> /srv/actions-runner` |
| Job step "The operation was canceled" seconds in | runner restarted mid-job | re-run once the runner is stable |

## References

- [`.github/workflows/`](.github/workflows/) — currently `runs-on: ubuntu-latest`
- [`docs/go-public-checklist.md`](docs/go-public-checklist.md) — §5 (CI green) and §7 (release-please)
- patient-portal `deploy/RUNNER.md` — the fuller Docker/Chrome variant
- GitHub docs — [About self-hosted runners](https://docs.github.com/actions/hosting-your-own-runners/managing-self-hosted-runners/about-self-hosted-runners) · [Hardening for self-hosted runners](https://docs.github.com/actions/security-guides/security-hardening-for-github-actions#hardening-for-self-hosted-runners)
