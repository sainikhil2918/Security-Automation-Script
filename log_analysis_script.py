
import pandas as pd
import re
from datetime import datetime

def load_logs(file_path):
    """Reads log entries from a file."""
    with open(file_path, 'r') as file:
        logs = file.readlines()
    return logs

def filter_logs(logs):
    """Filters logs for specific patterns, such as failed logins or critical alerts."""
    filtered_logs = []
    
    # Define patterns to search for in logs
    failed_login_pattern = re.compile(r"failed login", re.IGNORECASE)
    critical_alert_pattern = re.compile(r"CRITICAL|ALERT", re.IGNORECASE)

    for log in logs:
        # Check if log matches any pattern
        if failed_login_pattern.search(log) or critical_alert_pattern.search(log):
            filtered_logs.append(log)
    
    return filtered_logs

def prioritize_alerts(filtered_logs):
    """Prioritizes critical logs for immediate attention."""
    prioritized_logs = []
    
    # Define pattern for critical or high-priority alerts
    critical_pattern = re.compile(r"CRITICAL|malware|unauthorized access", re.IGNORECASE)

    for log in filtered_logs:
        # Check if log matches critical pattern
        if critical_pattern.search(log):
            prioritized_logs.append(log)
    
    return prioritized_logs

if __name__ == "__main__":
    # Load logs from the sample file
    logs = load_logs('sample_logs/example_log.txt')
    
    # Filter logs for important events
    filtered_logs = filter_logs(logs)
    
    # Prioritize high-severity alerts
    prioritized_logs = prioritize_alerts(filtered_logs)
    
    # Display the results
    print("Filtered Logs:")
    for log in filtered_logs:
        print(log.strip())
    
    print("\nPrioritized Alerts:")
    for log in prioritized_logs:
        print(log.strip())


