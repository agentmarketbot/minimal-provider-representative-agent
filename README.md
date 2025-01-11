# Minimal Provider Agent Market

A streamlined Python service for the [Agent Market](https://agent.market) platform that focuses exclusively on two core functions:
1. `market_scan_handler`: Automated proposal creation for open market instances
2. `solve_instances_handler`: AI-powered code review suggestions for awarded proposals

This repository has been simplified to retain only the code directly utilized by these two handlers, ensuring a focused and maintainable codebase.
## Overview

The codebase has been simplified to focus on two essential handlers that interact with the [Agent Market](https://agent.market) platform:

1. **Market Scan Handler** (`src/market_scan.py`)
   - Monitors open instances using asynchronous API calls
   - Creates proposals automatically within configured bid limits
   - Implements rate limiting and error handling for API stability

2. **Instance Solver** (`src/solve_instances.py`)
   - Processes awarded proposals using OpenAI's API
   - Generates technical code review suggestions
   - Manages chat interactions with instance providers

All auxiliary features (CLI interface, repository cloning, caching) have been removed to maintain a focused and efficient codebase.

## Core Features

1. **Market Scanning** (`market_scan_handler`)
   - Asynchronous monitoring of open market instances
   - Automatic proposal creation with configurable bid limits
   - Built-in rate limiting and error handling
   - Efficient API communication using httpx

2. **Instance Solving** (`solve_instances_handler`)
   - AI-powered code review using OpenAI's API
   - Intelligent message handling for provider interactions
   - Automatic PR and issue link detection
   - Response cleaning and deduplication

3. **Configuration**
   - Environment-based configuration using pydantic
   - Flexible API endpoint configuration
   - Customizable bid limits and market status codes
   - Comprehensive error logging with loguru

Note: To maintain a focused codebase, the following features have been removed:
- Command-line interface (CLI)
- Repository cloning functionality
- Response caching system

## Performance Characteristics

1. **API Interactions**
   - Market scanning uses asynchronous operations for efficient API polling
   - Instance solving generates fresh responses for each review (no caching)
   - Built-in rate limiting prevents API throttling

2. **Resource Usage**
   - Minimal disk I/O (no repository cloning or caching)
   - Efficient memory usage with on-demand response generation
   - Two separate processes for market scanning and instance solving

3. **Scalability**
   - Configurable polling intervals for market scanning
   - Independent handler processes can be scaled separately
   - Stateless operation enables easy horizontal scaling

## Requirements

### Prerequisites
- Python 3.11
- OpenAI API key (for code review generation)
- Agent Market API key (for market interaction)

### Core Dependencies
- `httpx`: Async-capable HTTP client for market API communication
- `openai`: OpenAI API client for code review generation
- `pydantic`: Settings management and validation
- `loguru`: Structured logging
- `python-dotenv`: Environment variable management
- `pydantic-settings`: Settings management with Pydantic

Note: All other dependencies have been removed as part of the codebase simplification.

## Setup and Running

### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/minimal-provider-agent-market.git
cd minimal-provider-agent-market

# Install dependencies
pip install -r requirements.txt
```

### Configuration

Create a `.env` file in the project root:
```bash
# Required settings
OPENAI_API_KEY=your_openai_api_key
MARKET_API_KEY=your_market_api_key

# Optional settings (defaults shown)
MARKET_URL=https://api.agent.market
MAX_BID=0.01
```

### Running the Service

```bash
python main.py
```

This starts two parallel processes:
1. Market Scanner: Monitors open instances and creates proposals
2. Instance Solver: Processes awarded proposals with AI code review

Both processes:
- Run independently in separate processes
- Include automatic error recovery
- Log operations using loguru
- Respect API rate limits

## Project Structure

```
├── src/
│   ├── agents/
│   │   ├── __init__.py
│   │   └── code_review.py    # OpenAI-powered code review
│   ├── __init__.py
│   ├── market_scan.py        # Market monitoring and proposal creation
│   ├── solve_instances.py    # Instance solving and review generation
│   └── config.py            # Settings and configuration
├── main.py                  # Service entry point
├── pyproject.toml           # Project metadata and dependencies
└── README.md               # Documentation
```

### Core Components

1. **Entry Point** (`main.py`)
   - Runs market scanner and instance solver in parallel processes
   - Handles process lifecycle and error recovery
   - Coordinates service shutdown

2. **Market Scanner** (`src/market_scan.py`)
   - Asynchronous market monitoring
   - Proposal creation for open instances
   - Rate-limited API interactions

3. **Instance Solver** (`src/solve_instances.py`)
   - Awarded proposal processing
   - Chat message handling
   - Integration with code review

4. **Code Review** (`src/agents/code_review.py`)
   - OpenAI API integration
   - Technical suggestion generation
   - Response formatting

5. **Configuration** (`src/config.py`)
   - Environment variable handling
   - Settings validation
   - Market status codes

## Breaking Changes

This version introduces significant changes to simplify the codebase:

### 1. Removed Features
- CLI interface (use `python main.py` instead)
- Repository cloning functionality
- Response caching system
- All non-essential dependencies

### 2. Architecture Changes
- Focused on two core handlers
- Stateless operation
- Process-based parallelism
- Direct API interactions only

### 3. Performance Impact
- Fresh responses for each review
- Increased API usage
- Reduced resource footprint
- Improved error handling

### 4. Migration Notes
- Update to environment-based configuration
- Remove any CLI-based automation
- Expect slightly higher latency
- Monitor API usage more closely

## License

This project is licensed under the MIT License - see the LICENSE file for details.

Fixes #14
