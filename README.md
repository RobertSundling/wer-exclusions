# WER Exclusions Manager

![GitHub License](https://img.shields.io/github/license/RobertSundling/wer-exclusions)
![GitHub issues](https://img.shields.io/github/issues/RobertSundling/wer-exclusions)
![GitHub last commit](https://img.shields.io/github/last-commit/RobertSundling/wer-exclusions)

This Python script, `wer_exclusions.py`, allows you to add or remove executables from the Windows Error Reporting (WER) exclusion list. This allows you to prevent them from being reported in Windows Error Reporting.

## Table of Contents

<!-- @import "[TOC]" {cmd="toc" depthFrom=2 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [Table of Contents](#table-of-contents)
- [Motivations](#motivations)
- [Features](#features)
- [Requirements](#requirements)
- [Usage](#usage)
  - [Adding an executable to the exclusion list:](#adding-an-executable-to-the-exclusion-list)
  - [Removing an executable from the exclusion list:](#removing-an-executable-from-the-exclusion-list)
- [Notes](#notes)
- [Error Handling](#error-handling)
- [License](#license)

<!-- /code_chunk_output -->

## Motivations

During development, applications are frequently modified and tested, and Windows Error Reporting (WER) can generate a lot of noise by reporting errors in applications when you're just trying to debug them.

Windows does provide the ability to exclude specific executables from Windows Error Reporting. However, the interface is not obvious. This tool provides a simple command-line interface to manage this exclusion list.

This script is suitable for use as part of an automated build process, allowing you to manage the WER exclusion list programmatically whenever a new executable is created.

## Features

* Add executables to the WER exclusion list.
* Remove executables from the WER exclusion list.
* Checks if an executable is already in the exclusion list before adding or removing.
* Handles errors and provides informative messages.

## Requirements

* Python 3.x
* No additional Python packages are required
* Windows operating system

## Usage

### Adding an executable to the exclusion list:

```sh
python wer_exclusions.py add executable_name.exe
```

### Removing an executable from the exclusion list:

```sh
python wer_exclusions.py remove executable_name.exe
```

## Notes

The WER exclusion list does *not* care about the path of the executable, only the name. Therefore, if your system has multiple executables with the same name, they will all be included or excluded from WER en masse.

## Error Handling

The script includes basic error handling. If an error occurs, a message will be printed to the console, and the script will exit with a non-zero exit code.

## License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.
