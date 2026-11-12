# Working rules (starter)

Keep this file short. Rules that must always hold belong in hooks and checks, not in prose.

## Who we write for
[One or two sentences: the reader, and the moment the problem is felt.]

## Rules
- Numbers are measured values or values calculated by a stated formula. A point that could not be confirmed is written as "unconfirmed".
- No personal names, company names, absolute paths or real e-mail addresses in any file.
- When a check stops a commit, fix the cause. Never loosen the check to get through.
- Read the rules of each place you publish to before writing for it.
- Publishing, posting and paying happen only after a person approves.

## How work moves here
1. A person decides at the checkpoints.
2. Claude Code plans, builds and reports.
3. Hooks refuse what must not run (`hooks/guard_min.py`).
4. A second AI reads the result before it ships.
5. Only what passed goes out.
