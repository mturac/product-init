<!-- product-init pull request template -->

## Summary

<!-- 1-3 sentences: what changed and why -->

## Required fields

- **golden_path_step**: <!-- 1..8 -->
- **AC ID**: <!-- e.g., AC-3 from SPEC.md -->
- **DEBT.md row** (if introducing debt): <!-- link/anchor in DEBT.md, or "n/a" -->

## Verification

- [ ] `python3 scripts/audit_constitution.py --project-dir <fixture>` exits 0
- [ ] `python3 scripts/audit_sow.py --project-dir <fixture>` exits 0
- [ ] Affected gate audits run locally and pass
- [ ] Tests added or updated; test output pasted below

## Test output

```
<!-- paste pytest / audit output -->
```
