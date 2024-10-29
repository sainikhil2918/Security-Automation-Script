# Security Automation Script
A Python-based script for basic log analysis and alert filtering, designed to improve security monitoring by detecting and prioritizing key alerts in log files.
## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Customization](#customization)
- [Sample Output](#sample-output)

## Introduction

The Security Automation Script is a tool designed to help security analysts quickly filter and prioritize logs for incident response. It automatically loads log files, filters entries based on predefined patterns (such as failed login attempts or critical security alerts), and prioritizes alerts that require immediate attention, like unauthorized access or malware detections.

## Features

- **Load Log Files**: Reads logs from specified files for analysis.
- **Filter Specific Events**: Identifies important events, such as failed logins and critical alerts.
- **Prioritize Alerts**: Highlights high-severity alerts, such as malware detection or unauthorized access attempts.
- **Customizable Patterns**: Easily modify filtering criteria to detect additional types of events.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/sainikhil2918/Security-Automation-Script.git
   cd Security-Automation-Script
2. **Create and Activate a Virtual Environment**:

   macOS/Linux:
      python3 -m venv env
      source env/bin/activate

   Windows:
      python -m venv env
      .\env\Scripts\activate
   
3.**Install Dependencie**:
      pip install -r requirements.txt

## Usage

1. **Place Log Files in `sample_logs` Folder**: 
   - Ensure the log file(s) you want to analyze are in the `sample_logs` folder within the project directory. The default log file name is `example_log.txt`, but you can modify the script to accept different filenames.

2. **Run the Script**:
   - Execute the following command in the terminal to start the script:
     ```bash
     python3 log_analysis_script.py
     ```
   - This command will load the log entries, filter them based on pre-defined criteria (e.g., failed login attempts, critical alerts), and then prioritize alerts that require immediate attention.

3. **Output Explanation**:
   - The script will display two main sections in the output:
     - **Filtered Logs**: Contains log entries that match general filtering criteria, such as failed logins or alert keywords.
     - **Prioritized Alerts**: Highlights only critical alerts, such as unauthorized access attempts or malware detections.

**Example Output**:
Filtered Logs:
2024-10-29 09:15:45 - WARNING - Failed login attempt for user 'john.doe' from IP 10.0.0.45
2024-10-29 10:22:00 - CRITICAL - Unauthorized access attempt detected from IP 192.168.0.10
2024-10-29 12:01:10 - ALERT - Multiple failed login attempts detected from IP 203.0.113.15

Prioritized Alerts:
2024-10-29 10:22:00 - CRITICAL - Unauthorized access attempt detected from IP 192.168.0.10
4. **Modifying Log File Input**:
By default, the script reads example_log.txt in the sample_logs folder. To analyze a different log file, 
edit the filename in the script's load_logs() function, or modify the script to accept filenames as command-line arguments.

## Customization
# In filter_logs()
failed_login_pattern = re.compile(r"failed login", re.IGNORECASE)
## Sample Output
Filtered Logs:
2024-10-29 09:15:45 - WARNING - Failed login attempt for user 'john.doe' from IP 10.0.0.45






## How to do Project Setup in Virtual environment

### Prerequisites
- **Python 3.x**: Download from [python.org](https://www.python.org/downloads/)

### Setting Up the Project

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/sainikhil2918/Security-Automation-Script.git
   cd Security-Automation-Script
2. **Create and Activate a Virtual Environment**:
python3 -m venv env
# Activate the environment
# On Windows
.\env\Scripts\activate
# On macOS/Linux
source env/bin/activate
**3.Install Dependencies**:
pip install -r requirements.txt

### Running the Script
python3 log_analysis_script.py


