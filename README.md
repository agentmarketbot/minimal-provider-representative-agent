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

Note: This is a simplified version that focuses on core market scanning and instance solving functionality. The following features have been removed to streamline the codebase:

1. **CLI Interface Removed**: The application now runs as a service only, removing the command-line interface to simplify usage and maintenance.
2. **Repository Cloning Removed**: Direct repository operations have been removed, focusing on API-based interactions.
3. **Caching Mechanism Removed**: Responses are now generated on-demand for better consistency, though with slightly higher latency.

## Performance Considerations

- Without caching, each instance review requires a new API call
- The application uses asynchronous operations for market scanning
- Rate limiting is implemented to prevent API throttling

## Prerequisites

- Python 3.10+
- OpenAI API key (for AI-powered code review)
- Agent Market API key

### Core Dependencies

- `httpx`: For API communication with Agent Market
- `openai`: For AI-powered code review
- `loguru`: For structured logging
- `pydantic`: For settings management and validation

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
│   ├── agents/           # AI agent implementation
│   │   └── code_review.py     # Code review using OpenAI API
│   ├── market_scan.py    # Market scanning and proposal creation
│   ├── solve_instances.py# Instance solving and code review logic
│   ├── config.py         # Environment and application settings
│   └── enums.py         # Removed - status codes moved to config.py
├── main.py             # Service entry point (runs both handlers)
├── pyproject.toml      # Project dependencies and settings
└── README.md          # Documentation
```

Core Components:
1. `market_scan.py`: Handles market monitoring and proposal creation
   - Scans for open instances
   - Creates proposals for new instances
   - Uses rate limiting for API stability

2. `solve_instances.py`: Manages instance solving workflow
   - Processes awarded proposals
   - Integrates with OpenAI for code review
   - Handles chat interactions with providers

3. `code_review.py`: Provides AI-powered code review
   - Simplified integration with OpenAI API
   - Generates focused technical suggestions
   - Streamlined for efficient code review generation

## Configuration

The service uses the following environment variables:

Required:
- `OPENAI_API_KEY`: Your OpenAI API key for code review functionality
- `MARKET_API_KEY`: Your Agent Market API key (get it from [agent.market](https://agent.market))

Optional:
- `MAX_BID`: Maximum bid amount for proposals (default: 0.01)
- `MARKET_URL`: Agent Market API URL (default: https://api.agent.market)

The service uses two main handlers:
1. `market_scan_handler`: Monitors the market and creates proposals
2. `solve_instances_handler`: Processes awarded proposals with AI assistance

## Breaking Changes and Migration Guide

### Removed Features

1. **CLI Interface**
   - Impact: Command-line operations are no longer available
   - Migration: Use the service mode by running `python main.py`
   - Rationale: Simplifies codebase and reduces maintenance overhead

2. **Repository Cloning**
   - Impact: Direct repository operations have been removed
   - Migration: Code review now operates via API interactions only
   - Rationale: Reduces complexity and potential security risks

3. **Caching Mechanism**
   - Impact: Each request generates fresh responses
   - Migration: No action needed; responses are now generated on-demand
   - Rationale: Ensures consistency and reduces state management complexity

### Performance Impact

- **Response Time**: Slightly increased due to removal of caching
- **Resource Usage**: Reduced due to removal of repository cloning
- **API Usage**: Increased due to on-demand response generation
- **Reliability**: Improved through simplified architecture

## License

This project is licensed under the MIT License - see the LICENSE file for details.

Fixes #14
