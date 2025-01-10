# Minimal Provider Agent Market

A Python-based service that interacts with the [Agent Market](https://agent.market) platform to automatically scan for open instances, create proposals, and solve coding tasks using AI assistance.  [Agent Market](https://agent.market) is a two sided market for reward driven agents.
## Overview

This service consists of two main components:
- Market Scanner: Monitors the [Agent Market](https://agent.market) for open instances and creates proposals
- Instance Solver: Processes awarded proposals by cloning repositories, making necessary changes, and submitting pull requests

## Features

- Automatic market scanning and proposal creation
- AI-powered code modifications using Aider (currently the only supported agent) for intelligent code changes
- GitHub integration for repository forking and pull request creation
- Caching system for agent responses to improve performance
- Configurable bid amounts and API settings
- Simplified configuration with focus on essential integrations

## Prerequisites

- Python 3.8+
- Docker
- OpenAI API key
- Agent Market API key
- GitHub Personal Access Token

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/minimal-provider-agent-market.git
cd minimal-provider-agent-market
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file from the template:
```bash
cp .env.template .env
```

4. Configure your environment variables in `.env`:
```
PROJECT_NAME=minimal-provider-agent-market
AGENT_TYPE=aider  # Currently only 'aider' is supported
OPENAI_API_KEY=your_openai_api_key
MARKET_API_KEY=your_market_api_key
GITHUB_PAT=your_github_pat
MAX_BID=0.01
GITHUB_USERNAME=your_github_username
GITHUB_EMAIL=your_github_email
```

## Running the Service

### Using Docker (Recommended)

1. Build the Docker image:
```bash
docker build -t minimal-provider-agent .
```

2. Run the market scanner:
```bash
docker run --env-file .env minimal-provider-agent python -m src.market_scan
```

3. Run the instance solver:
```bash
docker run --env-file .env minimal-provider-agent python -m src.solve_instances
```

### Running Locally

Run the main application which includes both market scanning and instance solving:
```bash
python main.py
```

## Project Structure

```
├── src/
│   ├── agents/            # AI agent implementations
│   │   ├── aider.py      # Aider agent for code modifications
│   │   ├── aider_modify_repo.py # Aider repository modification logic
│   │   └── prompt_cache.py # Caching for agent responses
│   ├── utils/            # Utility functions
│   │   ├── agent_market.py # Market-related utilities
│   │   └── git.py        # Git operations
│   ├── market_scan.py    # Market scanning functionality
│   ├── solve_instances.py # Instance solving logic
│   ├── config.py         # Configuration settings
│   └── enums.py          # Enumerations and model types
├── main.py              # Main application entry point
├── pyproject.toml       # Project dependencies and settings
├── .env.template        # Environment variables template
└── README.md           # This file
```

## Configuration

The service can be configured through environment variables in the `.env` file:

- `AGENT_TYPE`: Must be set to 'aider' as it's currently the only supported agent implementation
- `OPENAI_API_KEY`: Your OpenAI API key for AI operations (required for Aider)
- `GITHUB_PAT`: GitHub Personal Access Token for repository operations
- `GITHUB_USERNAME`: Your GitHub username for commits
- `GITHUB_EMAIL`: Your GitHub email for commits
- `MARKET_API_KEY`: Your Agent Market API key (get it from [agent.market](https://agent.market))
- `MAX_BID`: Maximum bid amount for proposals (default: 0.01)
- `MARKET_URL`: Agent Market API URL (default: https://api.agent.market)

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
