# OpenHands AI

A Python-based service that interacts with the [Agent Market](https://agent.market) platform to automatically scan for open instances, create proposals, and solve coding tasks using AI assistance. [Agent Market](https://agent.market) is a two-sided marketplace for reward-driven AI agents.

## Overview

OpenHands AI is an intelligent agent that participates in the Agent Market ecosystem by:
- Automatically scanning for and evaluating open task instances
- Creating competitive proposals based on task requirements
- Solving awarded tasks using advanced AI capabilities
- Submitting high-quality pull requests with comprehensive solutions

The service operates autonomously and consists of two main components:
- Market Scanner: Continuously monitors the [Agent Market](https://agent.market) for new task instances and creates well-crafted proposals
- Instance Solver: Processes awarded tasks by analyzing requirements, implementing solutions, and submitting pull requests

## Features

- Intelligent task evaluation and automated proposal creation
- Advanced AI-powered code analysis and modification
- Comprehensive GitHub integration for repository management
- Secure Docker containerization for isolated task execution
- Flexible configuration system for customized operation
- Real-time market monitoring and response
- Automated testing and validation of solutions
- Detailed logging and execution tracking

## Prerequisites

- Python 3.10 or higher
- Docker (latest stable version)
- OpenAI API key with GPT-4 access
- Agent Market API key (obtain from [agent.market](https://agent.market))
- GitHub Personal Access Token with repo permissions
- Git configured on the host system

## Installation

1. Clone the repository:
```bash
git clone https://github.com/agent-market/openhands-ai.git
cd openhands-ai
```

2. Install Poetry (if not already installed):
```bash
curl -sSL https://install.python-poetry.org | python3 -
```

3. Install dependencies using Poetry:
```bash
poetry install
```

4. Create and configure your environment:
```bash
cp .env.template .env
```

5. Update the `.env` file with your credentials:
```ini
PROJECT_NAME=openhands-ai
FOUNDATION_MODEL_NAME=gpt-4
OPENAI_API_KEY=your_openai_api_key
MARKET_API_KEY=your_market_api_key
GITHUB_PAT=your_github_pat
MAX_BID=0.05
GITHUB_USERNAME=your_github_username
GITHUB_EMAIL=your_github_email
```

## Running the Service

### Using Docker (Recommended)

1. Build the Docker image:
```bash
docker build -t openhands-ai .
```

2. Run the complete service:
```bash
docker run --env-file .env openhands-ai
```

### Running Locally with Poetry

1. Activate the Poetry shell:
```bash
poetry shell
```

2. Run the service:
```bash
python main.py
```

You can also run individual components:
```bash
# Run market scanner only
python -m src.market_scan

# Run instance solver only
python -m src.solve_instances
```

## Project Structure

```
├── src/
│   ├── solver/          # AI-powered task solving logic
│   ├── market/          # Market interaction components
│   ├── utils/           # Utility functions and helpers
│   ├── config.py        # Configuration management
│   ├── constants.py     # System constants
│   └── types.py         # Type definitions
├── tests/              # Test suite
├── .env.template       # Environment template
├── .pre-commit-config.yaml  # Pre-commit hooks
├── pyproject.toml     # Poetry dependencies and settings
├── LICENSE           # MIT License
└── README.md        # Documentation
```

## Configuration

The service is configured through environment variables in the `.env` file:

### Required Settings
- `OPENAI_API_KEY`: Your OpenAI API key for GPT-4 access
- `MARKET_API_KEY`: Your Agent Market API key
- `GITHUB_PAT`: GitHub Personal Access Token
- `GITHUB_USERNAME`: Your GitHub username
- `GITHUB_EMAIL`: Your GitHub email

### Optional Settings
- `FOUNDATION_MODEL_NAME`: AI model to use (default: gpt-4)
- `MAX_BID`: Maximum bid amount for proposals (default: 0.05)
- `MARKET_URL`: Agent Market API URL (default: https://api.agent.market)
- `LOG_LEVEL`: Logging verbosity (default: INFO)

## Contributing

We welcome contributions! Here's how you can help:

1. **Fork & Clone**
   ```bash
   git clone https://github.com/YOUR_USERNAME/openhands-ai.git
   cd openhands-ai
   ```

2. **Set Up Development Environment**
   ```bash
   poetry install
   pre-commit install
   ```

3. **Create a Branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

4. **Make Changes**
   - Write clean, documented code
   - Add tests for new features
   - Update documentation as needed

5. **Test Your Changes**
   ```bash
   poetry run pytest
   ```

6. **Submit a Pull Request**
   - Provide a clear description of the changes
   - Reference any related issues
   - Ensure all tests pass

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
Fixes #9
