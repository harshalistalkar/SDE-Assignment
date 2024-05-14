import json
import os

def search_logs(criteria):
    logs = []
    for file in os.listdir('.'):
        if file.endswith('.log'):
            with open(file, 'r') as f:
                for line in f:
                    log_data = json.loads(line.strip())
                    match = True
                    for key, value in criteria.items():
                        if key not in log_data or log_data[key] != value:
                            match = False
                            break
                    if match:
                        logs.append(log_data)
    return logs

if __name__ == "__main__":
    print("Welcome to the Log Query Interface!")
    print("Enter search criteria:")
    level = input("Log Level (info, error, success): ")
    log_string = input("Log String: ")
    source = input("Log Source: ")

    criteria = {}
    if level:
        criteria['level'] = level
    if log_string:
        criteria['log_string'] = log_string
    if source:
        criteria['metadata'] = {'source': source}

    result = search_logs(criteria)
    print("Matching logs:")
    for log_entry in result:
        print(log_entry)
