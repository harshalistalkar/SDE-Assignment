
To run the project, you'll need to follow these steps:

1. Setting Up the Log Ingestion System:
1. Create Log Files: First, create the log files where the logs will be stored. You can create these files manually or let the system create them as logs are ingested.1.
For example:
touch log1.log log2.log log3.log

2. Run the Log Ingestion System: Run the provided Python script for the Log Ingestion System ('log_ingestion.py').
 This script will continuously listen for log entries and write them to the appropriate log files.

python log_ingestion.py

This script will start running and will be ready to receive log entries.

2. Running the Query Interface:
1. Modify and Extend the Query Interface Script: Take the provided Python script for the Query Interface (query_interface.py) and modify it according to your advanced feature requirements.
   You might need to add functionality for searching within date ranges, regex matching, combining filters, real-time updates, and role-based access control.

2. Run the Query Interface Script: After modifying the script, run it in your terminal or command prompt:

 python query_interface.py

* Additional Considerations:
Environment Setup: Make sure you have Python installed on your system and that you have the necessary permissions to create and modify files.
Libraries: Ensure that you have any required libraries installed, such as json for handling JSON data.
Error Handling: Implement error handling in both scripts to handle potential errors gracefully.
Testing: Test the system thoroughly to ensure it behaves as expected and meets your requirements.

By following these steps, you should be able to run the project and interact with both the Log Ingestion System and the Query Interface.
