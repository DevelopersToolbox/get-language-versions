<!-- markdownlint-disable -->
<p align="center">
    <a href="https://github.com/DevelopersToolbox/">
        <img src="https://cdn.wolfsoftware.com/assets/images/github/organisations/developerstoolbox/black-and-white-circle-256.png" alt="DevelopersToolbox logo" />
    </a>
    <br />
    <a href="https://github.com/DevelopersToolbox/get-language-versions/actions/workflows/cicd.yml">
        <img src="https://img.shields.io/github/actions/workflow/status/DevelopersToolbox/get-language-versions/cicd.yml?branch=master&label=build%20status&style=for-the-badge" alt="Github Build Status" />
    </a>
    <a href="https://github.com/DevelopersToolbox/get-language-versions/blob/master/LICENSE.md">
        <img src="https://img.shields.io/github/license/DevelopersToolbox/get-language-versions?color=blue&label=License&style=for-the-badge" alt="License">
    </a>
    <a href="https://github.com/DevelopersToolbox/get-language-versions">
        <img src="https://img.shields.io/github/created-at/DevelopersToolbox/get-language-versions?color=blue&label=Created&style=for-the-badge" alt="Created">
    </a>
    <br />
    <a href="https://github.com/DevelopersToolbox/get-language-versions/releases/latest">
        <img src="https://img.shields.io/github/v/release/DevelopersToolbox/get-language-versions?color=blue&label=Latest%20Release&style=for-the-badge" alt="Release">
    </a>
    <a href="https://github.com/DevelopersToolbox/get-language-versions/releases/latest">
        <img src="https://img.shields.io/github/release-date/DevelopersToolbox/get-language-versions?color=blue&label=Released&style=for-the-badge" alt="Released">
    </a>
    <a href="https://github.com/DevelopersToolbox/get-language-versions/releases/latest">
        <img src="https://img.shields.io/github/commits-since/DevelopersToolbox/get-language-versions/latest.svg?color=blue&style=for-the-badge" alt="Commits since release">
    </a>
    <br />
    <a href="https://github.com/DevelopersToolbox/get-language-versions/blob/master/.github/CODE_OF_CONDUCT.md">
        <img src="https://img.shields.io/badge/Code%20of%20Conduct-blue?style=for-the-badge" />
    </a>
    <a href="https://github.com/DevelopersToolbox/get-language-versions/blob/master/.github/CONTRIBUTING.md">
        <img src="https://img.shields.io/badge/Contributing-blue?style=for-the-badge" />
    </a>
    <a href="https://github.com/DevelopersToolbox/get-language-versions/blob/master/.github/SECURITY.md">
        <img src="https://img.shields.io/badge/Report%20Security%20Concern-blue?style=for-the-badge" />
    </a>
    <a href="https://github.com/DevelopersToolbox/get-language-versions/issues">
        <img src="https://img.shields.io/badge/Get%20Support-blue?style=for-the-badge" />
    </a>
</p>

## Overview

This is a command line version of our github action [get-language-versions](https://github.com/ActionsToolbox/get-language-versions).

This script will fetch up-to-date data on the latest version(s) available on Github Actions for a given set of languages. It does this by first
identifying the latest release (if the version source is in GitHub), and then extracting the information from the versions file of that latest release.

It will also compare this to the End-Of-Life (EOL) data for that language to ensure that you are not being given EOL versions (unless you specifically
as the tool to give them to you).

## Installation

```
pip install wolfsoftware.get-language-versions
```

## Supported Languages

- Go
- Node / NodeJS
- Perl
- Php
- Python
- Ruby
- Terraform

## Usage

```
usage: get-language-versions [-h] [-v] [-H] [-L] [-P] [-R] [-m MIN_VERSION] [-M MAX_VERSION] [-V MAX_VERSIONS] [-l {go,node,nodejs,perl,php,python,ruby,terraform}]

flags:
  -h, --help            Show this help message and exit.
  -v, --version         Show program's version number and exit.

optional flags:
  -H, --highest-only    Only return the highest version found. (default: False)
  -L, --list-languages  List the supported languages (default: False)
  -P, --include-pre-releases
                        Include pre-release versions (default: False)
  -R, --remove-patch-version
                        Strip the patch version from the returned versions. (default: False)

optional:
  -m MIN_VERSION, --min-version MIN_VERSION
                        The minimum version to start from (default: EOL)
  -M MAX_VERSION, --max-version MAX_VERSION
                        The maximum version to include (default: LATEST)
  -V MAX_VERSIONS, --max-versions MAX_VERSIONS
                        The maximum number of versions to return (default: 0)

required:
  -l {go,node,nodejs,perl,php,python,ruby,terraform}, --language {go,node,nodejs,perl,php,python,ruby,terraform}
                        The language to check. (default: None)
```

<br />
<p align="right"><a href="https://wolfsoftware.com/"><img src="https://img.shields.io/badge/Created%20by%20Wolf%20on%20behalf%20of%20Wolf%20Software-blue?style=for-the-badge" /></a></p>
