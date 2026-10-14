"""Summarize a deliberately simplified, synthetic sign-in log. No network access."""
import argparse
from collections import Counter
from pathlib import Path
import re

RECORD = re.compile(r"^\S+ user=(\S+) result=(failure|success) ip=(\S+)$")

def summarize(lines):
    outcomes = Counter()
    failed_users = Counter()
    malformed = 0
    for line in lines:
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        match = RECORD.fullmatch(line)
        if not match:
            malformed += 1
            continue
        user, result, _address = match.groups()
        outcomes[result] += 1
        if result == "failure":
            failed_users[user] += 1
    return outcomes, failed_users, malformed

def format_summary(summary):
    outcomes, users, malformed = summary
    result = [
        f"Events read: {sum(outcomes.values())}",
        f"Failed sign-ins: {outcomes['failure']}",
        f"Successful sign-ins: {outcomes['success']}",
        f"Skipped malformed lines: {malformed}",
        "Failures by user:",
    ]
    result.extend(f"  {user}: {count}" for user, count in sorted(users.items()))
    if not users:
        result.append("  none")
    return "\n".join(result)

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", nargs="?", type=Path,
                        default=Path(__file__).with_name("sample-auth.log"))
    args = parser.parse_args()
    try:
        lines = args.input.read_text(encoding="utf-8").splitlines()
    except (OSError, UnicodeError) as error:
        parser.error(f"Cannot read input: {error}")
    print(format_summary(summarize(lines)))

if __name__ == "__main__":
    main()
