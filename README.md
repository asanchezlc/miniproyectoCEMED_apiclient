# API Interaction Project

This project is designed to interact with a PHP-based REST API (which interacts with 2 databases).

3 types of interactions are allowed:
   - Download data between (date - delta_minutes, date + delta_minutes) [**db_date_minutes.py file**].
   - Download data between (start_date, end_date) [**db_date_range.py file**].
   - Download data between (last_recording - minutes, last_recording) [**db_last_minutes.py file**].

# CEMED

Main aspects learned from CEMED course is the use of "request" in python.

## Project Structure

- `src/`: Contains all Python scripts.
  - `APIRestClient.py`: Defines the APIRestClient class for handling API interactions.
  - `config.py`: Manages configuration settings and environment variables.
  - `db_date_minutes.py`: Script to download data between (date - delta_minutes, date + delta_minutes)
  - `db_date_range.py`: Script to download data between (start_date, end_date).
  - `db_last_minutes`: Script to download data between (last_recording - minutes, last_recording).
- `requirements.txt`: Lists all Python dependencies needed for the project.

## Setup Instructions

### Prerequisites

- Python 3.x
- pip (Python package installer)
- Access to a PHP server running the corresponding backend code.

### Environment Setup

1. **Clone the repository**:
   Use Git to clone the repository to your local machine.
   ```bash
   git clone [repository-url]
   cd [project-directory]

2. Create a virtual environment and activate it:
    Create a Python virtual environment in which to install the packages.
   ```bash
    # For Unix/macOS
    python3 -m venv .venv
    source .venv/bin/activate

    # For Windows
    python -m venv .venv
    .venv\Scripts\activate

3. Install required Python packages:
   ```bash
   pip install -r requirements.txt