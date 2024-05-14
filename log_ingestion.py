import json
import os
from datetime import datetime

def log_to_file(log_data):
    log_file = log_data['metadata']['source']
    with open(log_file, 'a') as f:
        log_entry = json.dumps(log_data)
        f.write(log_entry + '\n')

def log(log_string, level='info', source='default.log'):
    timestamp = datetime.utcnow().isoformat() + 'Z'
    log_data = {
        'level': level,
        'log_string': log_string,
        'timestamp': timestamp,
        'metadata': {
            'source': source
        }
    }
    log_to_file(log_data)

if __name__ == "__main__":
    while True:
        source = input("Enter the log source (e.g., log1.log): ")
        log_string = input("Enter the log message: ")
        level = input("Enter the log level (info, error, success): ")
        log(log_string, level=level, source=source)
        print("Log entry recorded.")
