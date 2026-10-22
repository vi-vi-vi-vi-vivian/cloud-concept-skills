# cloud-concept-skills

Community-maintained Huawei Cloud skills; not an official Huawei Cloud project.

## Repository contract

- `skills/<name>/` contains the install payload only. Put gates, evals, and `skillcheck.toml` under `qa/<name>/`.
- Run `./qa/<name>/validate.sh` for a changed skill or `./tools/validate-all.sh` for the repository.
- Keep `skills/`, `qa/` (`VERSION`, changelog), `docs/catalog.yml`, and `docs/skills/<name>.md` synchronized.
- English lives at `skills/en/<name>`; Simplified Chinese at `skills/cn/<name>-cn`. Update pairs together under `docs/localization.md`; `tools/validate-localization.py` is the parity gate.
- ClawHub publishes only `skills/en`; never run ClawHub sync against `skills/cn`.
- Never commit credentials, `.env*`, generated workspaces, or gate reports.
- Do not auto-install `hcloud`. Real BSS calls run only when a skill-specific opt-in environment variable enables them.
- Billing and onboarding stay read-only. Cost-estimation creates stay within the allowlist and confirmation gates; unsubscribe stays console-only.

## Skill structure and loading

- Organize substantial skills by Shared, Service, Helper, Recipe, and Persona responsibilities. Use the definitions in `docs/authoring.md`; these are content roles, not five mandatory skills or loading stages.
- Give each command contract one canonical location. Category indexes and workflows link to it. FCAPS is a cross-service index; it does not replace service names or describe execution effects.
- Keep command contracts in four columns: command, action, inputs and sources, constraints. Store dated verification records separately by full command ID. Discover detailed parameters with current CLI help; resolve only missing resource identifiers.
- Define cross-command field bindings once in Helpers, including input type, producer, selection condition, and output field. Preserve command versions and resource scope; refresh help when CLI metadata changes.
- Classify effects from the documented operation behavior. HTTP methods and operation prefixes alone do not establish read-only behavior.
- Use shallow reference directories when they reduce unrelated reading. Each pointer states when to read its target. A known workflow can link directly to a needed contract.
- Preserve the requested implementation scope. A planned recipe contains its goal and one or two guidance sentences; it is not an executable workflow.
- Keep unfinished skills under `development/`. Publish, register, and create localization pairs only when promoting a draft to the installable catalog.
- Verify CLI facts before writing contracts. Record help checks and live API calls separately. Empty responses, permission failures, and successful resource queries are distinct results. Help or dry-run success does not establish live API success.
- Keep validation scripts outside runtime references. Store raw outputs and validation reports in an ignored workspace; redact credentials and sensitive response fields.

## Billing semantic split

Keep facts, dimensions, measures, and routing thin in `references/semantic/*.yml`. Put CLI contracts, concrete codes, enum values, response paths, and command examples in `references/related-commands.md` and its linked command references.

## FCAPS platform contracts

- Keep FCAPS as the directory skeleton. Use tool/target-system files inside each category; tool entrypoints only route and define tool-specific discovery. Do not duplicate contracts in a second tool hierarchy.
- Distinguish the agent host, remote target OS, and Kubernetes context. A CLI name or cloud image label alone does not establish the target environment. Preserve command modes that change observation scope or effects.
- Keep environment-specific evidence separate. A Linux pass is not a Windows pass; local kind is not CCE. Missing tools, no records, authorization failure, and unexecuted conditional collection remain distinct.
- Read final Markdown commands for post-write validation. Bind successful evidence to the actual row and revision; derive verification summaries from records. Keep source/migration notes and test fixtures outside runtime references.

## Document references

- Keep document routing separate from command contracts. Bundle conditional reading guidance and metadata indexes; keep bulk source text, images and caches outside the install payload.
- Generate document metadata from a declared source snapshot. Store provenance hashes in QA; review changed sources before changing validated commands. A cached page or successful link check is not current-environment evidence.
- Prefer publisher-provided Markdown; use the same document's HTML when Markdown yields no article. Verify document identity and body, not the suffix or HTTP status. Keep one catalog entry across formats; record archive and curated-link dates separately.
- Known commands bypass document lookup. Search catalogs for matching entries rather than loading the whole catalog. Source repair steps do not grant execution authorization.
