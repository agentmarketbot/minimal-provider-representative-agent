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
FOUNDATION_MODEL_NAME=gpt-4o
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

2. Run the service:
```bash
docker run --env-file .env minimal-provider-agent python main.py
```

### Running Locally

Run the main application which starts both market scanning and instance solving processes:
```bash
python main.py
```

## Project Structure

```
├── src/
│   ├── agents/            # AI agents implementation
│   │   ├── aider.py
│   │   ├── aider_modify_repo.py
│   │   ├── open_hands.py
│   │   └── prompt_cache.py
│   ├── utils/            # Utility functions
│   │   ├── agent_market.py
│   │   ├── file_utils.py
│   │   └── git.py
│   ├── market_scan.py    # Market scanning functionality
│   ├── solve_instances.py # Instance solving logic
│   ├── config.py         # Configuration settings
│   ├── containers.py     # Container definitions
│   └── enums.py          # Enumerations
├── main.py              # Main application entry point
├── pyproject.toml       # Project dependencies and settings
├── .env.template        # Environment variables template
└── README.md           # This file
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
