# verbum

A version bumping library.

## Examle

```python
from verbum import verbum

current_release = "1.1.1"
new_release = verbum.bump_version(current_release, verbum.BumpType.ALPHA)
print(new_release)  # 1.1.1a1
```

## Version strings

### Input

verbum is opinionated and version strings accepted by `bump_version` are a subset of valid strings
specified in [PEP440](https://peps.python.org/pep-0440/).

### Output

Version strings output by `bump_version` are [PEP440](https://peps.python.org/pep-0440/) compliant.

### Ruleset on top of PEP440

1. Three version numbers are mandatory: `X.Y.Z`.
2. A leading forth number (epoch) is forbidden.
3. Pre-release identifier like alpha, beta and release-candidates are only allowed with their
   abbreviations:
   - `alpha` -> `a`
   - `beata` -> `b`
   - `release-candidate` -> `rc`
4. Other variante as `rc` are not supported for release-candidates.
5. Pre-release identifier must follow the scheme `{a|b|rc}N` where `N` is an interger.
6. Pre-release and post-release counter must start with 1 not 0.
   A 0 is interpreted as not set. This means e.g. bumping a post-release on this `1.1.1rc0`
   would result in `1.1.1.post1`.
7. Additional identifiers or separators are forbidden.

### Valid examples

```text
1.2.3a1
1.2.3b1
1.2.3rc1
1.2.3

1.2.3.post1
1.2.3a1.post1
1.2.3b1.post1
1.2.3rc1.post1
```
