# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Removed
- Removed raaid agent implementation and related configurations as it was no longer being used
- Removed ANTHROPIC_API_KEY from environment variables
- Removed gpt-4o model references, replaced with gpt-4

### Changed
- Updated foundation model name from gpt-4o to gpt-4 in configurations
- Updated documentation to reflect current agent options