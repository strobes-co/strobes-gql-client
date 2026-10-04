# Wiki sources

These Markdown files are the source for the project
[Wiki](https://github.com/strobes-co/strobes-gql-client/wiki). They're kept in
the repo so they can be reviewed in pull requests and browsed offline.

- **[Home.md](Home.md)** is the wiki landing page.
- **[_Sidebar.md](_Sidebar.md)** and **[_Footer.md](_Footer.md)** render as the
  navigation sidebar and footer on GitHub wikis.
- Links between pages use GitHub-wiki style (page name without `.md`, spaces as
  hyphens), so they resolve both on the published wiki and when browsing here.

## Publishing to the GitHub wiki

GitHub serves a wiki from a separate git repository
(`<repo>.wiki.git`). To publish or update these pages:

```bash
# One-time: create the first wiki page via the GitHub UI so the wiki repo exists.
git clone https://github.com/strobes-co/strobes-gql-client.wiki.git
cp wiki/*.md strobes-gql-client.wiki/
cd strobes-gql-client.wiki
git add .
git commit -m "Update wiki from repo wiki/ sources"
git push
```

(Keep the leading-underscore files `_Sidebar.md` and `_Footer.md` — GitHub uses
those names specifically.)

## Page index

| Page | Topic |
|---|---|
| [Home](Home.md) | Overview & navigation |
| [Installation](Installation.md) | Install the package |
| [Configuration & Authentication](Configuration-and-Authentication.md) | Host, API token, org ID |
| [Quickstart](Quickstart.md) | First read / write / export |
| [Core Concepts](Core-Concepts.md) | Client, queries vs. mutations, responses, pagination, errors |
| [Search Query Language](Search-Query-Language.md) | Filter syntax & field reference |
| [Assets](Assets.md) | Assets |
| [Findings](Findings.md) | Findings (bugs) |
| [Engagements](Engagements.md) | Engagements |
| [Comments](Comments.md) | Comments |
| [Vault Documents](Vault-Documents.md) | Vault documents |
| [Reports](Reports.md) | Report templates & generation |
| [Exporting Data](Exporting-Data.md) | Async CSV & streaming exports |
| [Connectors & Scan Logs](Connectors-and-Scan-Logs.md) | Configurations & scan logs |
| [File Uploads & CSV Imports](File-Uploads-and-CSV-Imports.md) | Uploads & imports |
| [Python API Reference](Python-API-Reference.md) | Every client method |
| [GraphQL API Reference](GraphQL-API-Reference.md) | Public queries & mutations |
| [Troubleshooting](Troubleshooting.md) | Common errors |
