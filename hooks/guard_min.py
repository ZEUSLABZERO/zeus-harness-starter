#!/usr/bin/env python3
"""A minimal Claude Code PreToolUse hook: refuse one kind of call before it runs.

Claude Code sends the tool name and its input as JSON on stdin. Exit code 2 refuses the call and
the text on stderr goes back to the agent, which then has to choose another approach.

This starter refuses a single thing: a shell commit command that carries the flag for skipping
the commit checks. It is a text match on the command, nothing more — it does not follow what a
script does once it runs. Treat it as a seat belt, not a sandbox.

Standard library only. On any error the hook lets the call through, so a broken hook never
blocks your work.
"""
import json
import re
import sys

SKIP_FLAG = "--no-" + "verify"
RULE = re.compile(r"git\s+(commit|push)\b[^\n;|&]*" + re.escape(SKIP_FLAG))


def main() -> int:
    try:
        data = json.loads(sys.stdin.read() or "{}")
        if data.get("tool_name") == "Bash":
            command = str((data.get("tool_input") or {}).get("command", ""))
            if RULE.search(command):
                sys.stderr.write("guard: refused — this command skips the commit checks. Fix the cause instead.\n")
                return 2
    except Exception:
        return 0
    return 0


if __name__ == "__main__":
    sys.exit(main())
