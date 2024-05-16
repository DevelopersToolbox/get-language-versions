"""This is the summary line.

This is the further elaboration of the docstring. Within this section,
you can elaborate further on details as appropriate for the situation.
Notice that the summary and the elaboration is separated by a blank new
line.
"""

from packaging import version as semver

import colorama

colorama.init()

SUCCESS: str = colorama.Fore.GREEN
WARN: str = colorama.Fore.YELLOW
ERROR: str = colorama.Fore.RED
INFO: str = colorama.Fore.CYAN
BOLD: str = colorama.Style.BRIGHT
SYSTEM: str = colorama.Fore.LIGHTBLACK_EX
RESET: str = colorama.Style.RESET_ALL

MAX_VERSION: semver.Version = semver.parse('99999')
MIN_VERSION: semver.Version = semver.parse('0')

SUPPORTED_LANGUAGES: list = ['go', 'node', 'nodejs', 'perl', 'php', 'python', 'ruby', 'terraform']

URLS: dict[str, dict[str, str]] = {
    "go": {
        "releases_url": 'https://github.com/actions/go-versions/releases/latest/',
        "head_branch": 'main',
        "versions_url": 'https://raw.githubusercontent.com/actions/go-versions/LATEST_TAG/versions-manifest.json',
        "eol_url": 'https://endoflife.date/api/go.json'
    },
    "node": {
        "releases_url": 'https://github.com/actions/node-versions/releases/latest/',
        "head_branch": 'main',
        "versions_url": 'https://raw.githubusercontent.com/actions/node-versions/LATEST_TAG/versions-manifest.json',
        "eol_url": 'https://endoflife.date/api/nodejs.json'
    },
    "nodejs": {
        "releases_url": 'https://github.com/actions/node-versions/releases/latest/',
        "head_branch": 'main',
        "versions_url": 'https://raw.githubusercontent.com/actions/node-versions/LATEST_TAG/versions-manifest.json',
        "eol_url": 'https://endoflife.date/api/nodejs.json'
    },
    "perl": {
        "releases_url": 'https://github.com/shogo82148/actions-setup-perl/releases/latest/',
        "head_branch": 'main',
        "versions_url": 'https://raw.githubusercontent.com/shogo82148/actions-setup-perl/LATEST_TAG/versions/linux.json',
        "eol_url": 'https://endoflife.date/api/perl.json'
    },
    "php": {
        "versions_url": 'https://phpreleases.com/api/releases/',
        "eol_url": 'https://endoflife.date/api/php.json'
    },
    "python": {
        "releases_url": 'https://github.com/actions/python-versions/releases/latest/',
        "head_branch": 'main',
        "versions_url": 'https://raw.githubusercontent.com/actions/python-versions/LATEST_TAG/versions-manifest.json',
        "eol_url": 'https://endoflife.date/api/python.json'
    },
    "ruby": {
        "releases_url": 'https://github.com/ruby/setup-ruby/releases/latest/',
        "head_branch": 'master',
        "versions_url": 'https://raw.githubusercontent.com/ruby/setup-ruby/LATEST_TAG/ruby-builder-versions.json',
        "eol_url": 'https://endoflife.date/api/ruby.json'
    },
    "terraform": {
        "versions_url": 'https://releases.hashicorp.com/terraform/',
        "eol_url": 'https://endoflife.date/api/terraform.json'
    }
}
