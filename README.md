# Mina_Tool_Box

## Note on Final Product

This Telegram bot serves as a PoC and demonstrates the core functionalities planned for the project. The final product will be a fully-fledged native mobile application, offering enhanced privacy features, a richer user interface, and a more comprehensive set of functionalities tailored to the needs of validators and delegators in the Mina Protocol ecosystem.

## Overview

The Mina_Tool_Box is a Telegram bot designed for validators and delegators within the Mina Protocol blockchain ecosystem. It provides insights, notifications, and data analysis about validator performance, delegation changes, commission rates, and more. This bot serves as a proof of concept (PoC); the final product will be developed as a separate native mobile app for enhanced functionality and user experience.

## Features

### Implemented Features

1. **Validator Address Tracking:** 
    - Users can register validator addresses to monitor.

2. **Validator Performance Metrics:**
   - Uptime/Availability: Report on validator node uptime and any downtime incidents.
   - Block Production: Information on the number of blocks produced by the validator.
   - Expected vs. Actual Blocks: Comparison metrics to show performance.

3. **Commission Changes:**
   - Notify when a validator changes their commission rates.
   - Historical commission rate changes for comparison.

4. **Delegation Updates:**
   - Alerts on new delegations and undelegations.
   - Notifications for large delegation changes that could impact the stability of the validator or the returns for other delegators.

5. **Private Balance Check:** 
   - A simplified encryption method is used for checking account balances or rewards privately.
   - Provide updates on the balance of both the validator and the delegator’s accounts.
   - Alert users when rewards are distributed.

### Planned Features for Final Mobile App

1. **Enhanced Private Balance Check:** 
   - Implementing a more advanced privacy-preserving method utilizing zero-knowledge proofs.
   - 
2. **Ranking and Statistics:**
   - Provide information on the ranking of validators by stake, performance, and other metrics.
   - Give validators an understanding of their position in the overall network.

3.  **Voting Power:**
   - Report on the changes in voting power of the validator.

4.  **Slashing Alerts:**
   - Notify validators of any potential slashing events or risks.

5.  **Network and Protocol Updates:**
   - Inform about any upcoming protocol updates, governance proposals, and their outcomes.
   - Notify about changes in network parameters that might affect validators and delegators.

6.  **Price Tracking:**
   - Include the current price of the native token and any significant price movements.

7.  **Staking Rewards Calculator:**
    - Provide estimations of daily, weekly, or monthly rewards based on the current staking amount.

8.  **Downtime Alerts:**
    - Instant alerts for validators if their node appears to be offline or missing blocks.

9.  **Security Alerts:**
    - Inform validators about any security threats or updates needed to secure their node.

10. **Custom Threshold Notifications:**
    - Allow users to set custom thresholds for balance changes or reward amounts to receive notifications.

11. **Automated Health Checks:**
    - Periodic reports on the health and status of the validator node.

12. **Governance Participation:**
    - Encourage and remind validators and delegators to participate in governance decisions.
## Architecture
```
Mina_Tool_Box/
│
├── bot/                   # Telegram bot related modules
│   ├── __init__.py        # Makes bot a Python module
│   ├── bot.py             # Main bot functionalities
│   └── handlers.py        # Command handlers for the bot
│
├── database/              # Database related operations
│   ├── __init__.py        # Makes database a Python module
│   ├── database.py        # Database connection and operations
│   └── models.py          # Database models/schema
│
├── api/                   # External API interactions
│   ├── __init__.py        # Makes api a Python module
│   ├── mina_api.py        # Interactions with the MinaExplorer API
│   └── encryption.py      # Encryption utilities for private queries
│
├── utils/                 # Utility functions and shared components
│   ├── __init__.py        # Makes utils a Python module
|   ├── common.py          # Storage utility functions that could be used across different modules
│   └── visualization.py   # Data visualization utilities
│
├── scheduler/             # Scheduler for periodic tasks
│   ├── __init__.py        # Makes scheduler a Python module
│   └── scheduler.py       # Scheduling related functions
│
├── tests/                 # Unit tests and integration tests
│   ├── __init__.py        # Makes tests a Python module
│   ├── test_bot.py        # Tests for bot functionalities
│   ├── test_database.py   # Tests for database operations
│   └── test_api.py        # Tests for API interactions
│
├── config.py              # Configuration settings
├── main.py                # Entry point of the application
└── requirements.txt       # List of dependencies
```
### Modules

**bot/:** Contains all the Telegram bot-related code. This includes the main bot script and the command handlers.
**database/:** Manages all interactions with the database. It includes the connection setup and the database schema or models.
**api/:** Handles all external API calls, specifically to the MinaExplorer API, and includes any encryption logic for private queries.
**utils/:** A place for shared utility scripts like data visualization tools.
**scheduler/:** Contains code related to scheduling tasks, such as checking validator statuses or updates.
**tests/:** Includes all unit and integration tests for the different modules.
**config.py:** A central configuration file where all settings like API keys, database URIs, and other configurations are stored.
**main.py:** The entry point to the application which ties together the different modules.
**requirements.txt:** Lists all the Python package dependencies for the project

### Database

- PostgreSQL is used for persistent storage of user preferences and cached data.

### External APIs

- MinaExplorer API for fetching blockchain-related data.
- Additional APIs for price tracking and other external data sources.

### Security

- Encryption techniques are used for private data queries as a placeholder for future ZKP implementation.

## Setup and Configuration

### Prerequisites

- Python 3.6+
- PostgreSQL
- Telegram Bot Token

### Installation

1. Clone the repository and install the required Python packages.
2. Set up the PostgreSQL database and apply the initial schema from `database.py`.
3. Configure your Telegram bot token and database connection string in `config.py`.

### Running the Bot

Execute `python bot.py` to start the bot. It will run as a background service and respond to user commands on Telegram.

## Testing

- Unit tests are provided in `test.py` for testing the core functionalities.
- Integration tests to simulate user interaction with the bot and validate end-to-end workflows.

---