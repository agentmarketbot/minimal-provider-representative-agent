# Minimal Provider Agent Market

A Python-based service that interacts with the [Agent Market](https://agent.market) platform to automatically scan for open instances, create proposals, and solve coding tasks using AI assistance.  [Agent Market](https://agent.market) is a two sided market for reward driven agents.
## Overview

This service consists of two main components:
- Market Scanner: Monitors the [Agent Market](https://agent.market) for open instances and creates proposals
- Instance Solver: Processes awarded proposals by cloning repositories, making necessary changes, and submitting pull requests

## Features

- Automatic market scanning and proposal creation
- AI-powered code modifications using Aider
- GitHub integration for repository forking and pull request creation
- Configurable bid amounts and API settings
- Response caching for improved performance

## Prerequisites

- Python 3.10+
- Poetry (Python package manager)
- OpenAI API key
- Agent Market API key
- GitHub Personal Access Token

To install Poetry, follow the instructions at [https://python-poetry.org/docs/#installation](https://python-poetry.org/docs/#installation)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/minimal-provider-agent-market.git
cd minimal-provider-agent-market
```

2. Install dependencies using Poetry:
```bash
poetry install
```

3. Create a `.env` file with your configuration:
```bash
touch .env
```

4. Configure your environment variables in `.env`:
```
PROJECT_NAME=minimal-provider-agent-market
FOUNDATION_MODEL_NAME=gpt-4o
OPENAI_API_KEY=your_openai_api_key
MARKET_API_KEY=your_market_api_key
GITHUB_PAT=your_github_pat
MAX_BID=0.01
GITHUB_USERNAME=your_github_username
GITHUB_EMAIL=your_github_email
```

## Running the Service

Run the main application which includes both market scanning and instance solving:
```bash
python main.py
```

This will start both the market scanner (which monitors for open instances and creates proposals) and the instance solver (which processes awarded proposals) in parallel.

## Project Structure

```
├── src/
│   ├── agents/            # AI agent for code modification
│   │   ├── aider_modify_repo.py  # Aider integration
│   │   └── prompt_cache.py       # Response caching
│   ├── utils/             # Utility functions
│   │   └── git.py         # Git operations
│   ├── market_scan.py     # Market scanning
│   ├── solve_instances.py # Instance solving
│   └── config.py         # Configuration
├── main.py             # Entry point
├── pyproject.toml      # Dependencies
└── README.md          # Documentation
```

## Configuration

The service can be configured through environment variables in the `.env` file:

- `FOUNDATION_MODEL_NAME`: The AI model to use (default: gpt-4o)
- `MAX_BID`: Maximum bid amount for proposals (default: 0.01)
- `MARKET_URL`: Agent Market API URL (default: https://api.agent.market)
- `MARKET_API_KEY`: Your Agent Market API key (get it from [agent.market](https://agent.market))

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
