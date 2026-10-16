# Log Parsing

This project is part of the Holberton School software engineering curriculum (`holbertonschool-interview`). It focuses on processing standard input (stdin) line by line in Python, extracting HTTP metrics such as total file size and status code frequencies, and handling signals like keyboard interruptions.

## Learning Objectives

* How to read from `sys.stdin` line by line.
* Parsing strings and using regular expressions or string methods to extract specific data formats.
* Handling exceptions (`ValueError`, `KeyboardInterrupt`).
* Storing and updating aggregated metrics in dictionaries.
* Formatting and sorting output data according to specific criteria.

## Requirements

* Allowed editors: `vi`, `vim`, `emacs`
* All files interpreted/compiled on Ubuntu 14.04 LTS using Python 3 (version 3.4.3)
* All files must end with a new line
* The first line of all files must be exactly `#!/usr/bin/python3`
* Code should follow the PEP 8 style (version 1.7.x)
* All files must be executable

## Files

| File | Description |
| ---- | ----------- |
| [0-stats.py](0-stats.py) | Python script that reads stdin line by line and computes metrics. |

## Usage

Run the script locally by piping a log generator into it:

```bash
./0-generator.py | ./0-stats.py
