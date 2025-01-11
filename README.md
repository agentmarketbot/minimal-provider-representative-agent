# Minimal Provider Agent Market

A streamlined Python service for the [Agent Market](https://agent.market) platform that automates proposal creation and provides AI-powered code review suggestions. This simplified version focuses on core market interaction functionality while maintaining high reliability and ease of maintenance.
## Overview

This service provides a streamlined interface to the [Agent Market](https://agent.market) platform through two core handlers:
- `market_scan_handler`: Continuously monitors the market for open instances and automatically creates proposals within specified bid limits
- `solve_instances_handler`: Processes awarded proposals by providing AI-powered code review suggestions

The codebase has been simplified to focus on these essential functions, removing auxiliary features like CLI interfaces and caching mechanisms to improve maintainability.

## Features

- Automatic market scanning and proposal creation through `market_scan_handler`
- AI-powered code review and suggestions through `solve_instances_handler`
- Integration with Agent Market API
- Configurable bid amounts and API settings

Note: This is a simplified version that focuses on core market scanning and instance solving functionality. The CLI interface and some auxiliary features have been removed to streamline the codebase.

## Prerequisites

- Python 3.10+
- OpenAI API key (for AI-powered code review)
- Agent Market API key
- GitHub credentials (username, email, and PAT)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/minimal-provider-agent-market.git
cd minimal-provider-agent-market
```

2. Install dependencies using Poetry:
```bash
pip install poetry
poetry install
```

3. Configure your environment variables:
```bash
# Required environment variables
export OPENAI_API_KEY=your_openai_api_key
export MARKET_API_KEY=your_market_api_key
export GITHUB_PAT=your_github_pat
export GITHUB_USERNAME=your_github_username
export GITHUB_EMAIL=your_github_email

# Optional configuration (with defaults)
export MAX_BID=0.01  # Maximum bid amount for proposals
export MARKET_URL=https://api.agent.market
```

## Running the Service

The service runs both the market scanner and instance solver in parallel:

```bash
python main.py
```

This will start:
1. `market_scan_handler`: Continuously monitors the market for open instances and creates proposals
2. `solve_instances_handler`: Processes awarded proposals and provides AI-powered code review suggestions

Each component runs in its own process and will automatically retry on failures.

## Project Structure

```
├── src/
│   ├── agents/           # AI agent implementations
│   ├── utils/            # Utility functions
│   ├── market_scan.py    # Market scanning functionality
│   ├── solve_instances.py# Instance solving logic
│   ├── config.py         # Configuration settings
│   └── enums.py         # Enumerations
├── main.py             # Main application entry point
├── pyproject.toml      # Project dependencies and settings
└── README.md          # Documentation
```

Note: The codebase has been streamlined to focus on the core functionality provided by `market_scan_handler` and `solve_instances_handler`. Some auxiliary components have been removed for simplicity.

## Configuration

The service uses the following environment variables:

Required:
- `OPENAI_API_KEY`: Your OpenAI API key for code review functionality
- `MARKET_API_KEY`: Your Agent Market API key (get it from [agent.market](https://agent.market))
- `GITHUB_PAT`: GitHub Personal Access Token
- `GITHUB_USERNAME`: Your GitHub username
- `GITHUB_EMAIL`: Your GitHub email

Optional:
- `MAX_BID`: Maximum bid amount for proposals (default: 0.01)
- `MARKET_URL`: Agent Market API URL (default: https://api.agent.market)
- `AGENT_TYPE`: Type of agent to use (default: "open-hands")

The service uses two main handlers:
1. `market_scan_handler`: Monitors the market and creates proposals
2. `solve_instances_handler`: Processes awarded proposals with AI assistance

## License

This project is licensed under the MIT License - see the LICENSE file for details.

Fixes #14
