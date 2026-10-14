# CC GitHub workshop lab

This repository records GitHub practice for the University of Montana Cybersecurity Collective.

## Learning goals
- Make useful commits and inspect their differences.
- Write documentation another person can follow.
- Review files before publishing.

All workshop examples use harmless, synthetic information.

## File guide
- `learning-log.md`: example workshop takeaways.
- `summarize_logs.py`: a small Python parser for the synthetic sample format.
- `sample-auth.log`: fictional sign-in events, including successes and failures.
- `expected-output.txt`: the result to compare with the script's output.
- `test_summary.py`: tests of counts, empty input, and malformed records.
- `.gitignore`: starter rules for untracked local files.
- `.env.example`: blank configuration names for teaching. The parser does not need credentials.

## How to use
The browser workshop needs no installation. Read the files and compare the documented input/output.

To run the optional parser, install Python 3 and open a terminal in this folder:
```text
python summarize_logs.py sample-auth.log
python -m unittest -v test_summary.py
```
If your computer uses `python3` instead, substitute that command. No third-party packages are required.

## Example result
The supplied six events produce four failures and two successes. See `expected-output.txt` for the full summary.

## Contribution and reasoning
This is a supplied teaching example for the CC workshop. It separates parsing from formatting so the counting behavior can be checked independently. If you adapt it, describe your own changes rather than claiming the supplied code as your original work.

## Limitations
This parser supports only the deliberately simplified format in the sample. It does not parse arbitrary production SSH logs, validate every timestamp or address, or establish that a failed sign-in is an attack. A real monitoring tool would need additional validation and context.

## Next step
Add a test for another input case and explain the resulting change in a commit.

## Safe publishing
Keep live credentials and private keys outside repositories. Review contents, screenshots, history, and permission to share. `.gitignore` does not remove tracked files or earlier commits and does not protect browser uploads automatically.

## Documentation review exercise
This proposed sentence helps a first-time reader recognize the workshop example.
