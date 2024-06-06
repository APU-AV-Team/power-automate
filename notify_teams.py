import sys
import requests
import json

def notify_teams(webhook_url, report_file):
    with open(report_file, 'r') as f:
        changes = f.read()
    
    if changes:
        changes = changes.replace("\n", "<br>")
        payload = {
            "text": f"Changes detected in the Excel file:<br>{changes}"
        }
        requests.post(webhook_url, headers={"Content-Type": "application/json"}, data=json.dumps(payload))

if __name__ == "__main__":
    webhook_url = sys.argv[1]
    report_file = sys.argv[2]
    notify_teams(webhook_url, report_file)
