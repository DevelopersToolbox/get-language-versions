"""
This module defines constants and configurations used throughout the application.

It includes version boundaries, supported languages, and URLs for fetching version
information and end-of-life data for various programming languages and tools.
"""

from packaging import version as semver


# Maximum and minimum version boundaries
MAX_VERSION: semver.Version = semver.parse('99999')
MIN_VERSION: semver.Version = semver.parse('0')

# List of supported programming languages
SUPPORTED_LANGUAGES: list = ['go', 'node', 'nodejs', 'perl', 'php', 'python', 'ruby', 'terraform']

# URLs for fetching version information and end-of-life data
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
