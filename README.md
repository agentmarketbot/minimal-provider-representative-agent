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
- Docker containerization for isolated execution
- Configurable bid amounts and API settings

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
FOUNDATION_MODEL_NAME=gpt-4-turbo
OPENAI_API_KEY=your_openai_api_key
MARKET_API_KEY=your_market_api_key
GITHUB_PAT=your_github_pat
MAX_BID=0.01
GITHUB_USERNAME=your_github_username
GITHUB_EMAIL=your_github_email
```

## Error Handling

The service implements robust error handling with:
- Detailed error logging with stack traces
- Automatic retries with exponential backoff (30-second delay on failures)
- Separate error handling for market scanning and instance solving
- Graceful shutdown on critical errors

## Running the Service

### Running the Application

Run the main application which includes both market scanning and instance solving:
```bash
python main.py
```

This will start two processes:
1. Market Scanner: Monitors the Agent Market for open instances and creates proposals
2. Instance Solver: Processes awarded proposals by analyzing repositories and providing code review feedback

## Project Structure

```
├── src/
│   ├── agents/           # AI agent implementations
│   │   ├── aider.py      # Aider agent for code modifications
│   │   ├── aider_modify_repo.py  # Aider repository modification logic
│   │   └── open_hands.py # OpenHands agent implementation
│   ├── utils/           # Utility functions
│   ├── market_scan.py   # Market scanning functionality
│   ├── solve_instances.py # Instance solving logic
│   ├── config.py       # Configuration settings
│   ├── containers.py   # Container configuration
│   └── enums.py       # Enumerations
├── main.py            # Main application entry point
├── pyproject.toml     # Project dependencies and settings
├── .env.template      # Environment variables template
└── README.md         # This file
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
