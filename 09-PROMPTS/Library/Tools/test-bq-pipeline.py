# /// script
# dependencies = [
#   "google-cloud-bigquery",
# ]
# ///
import sys
import json
from datetime import datetime, timezone
from google.cloud import bigquery

PROJECT_ID = "fluted-century-466523-k4"
DATASET_ID = "snf_analytics"
TABLE_ID = "app_events"

def send_mock_event():
    print(f"Connecting to BigQuery project: {PROJECT_ID}...")
    client = bigquery.Client(project=PROJECT_ID)
    
    table_ref = f"{PROJECT_ID}.{DATASET_ID}.{TABLE_ID}"
    
    # Mock event data
    event = {
        "event_timestamp": datetime.now(timezone.utc).isoformat(),
        "session_id": "test_session_12345",
        "event_type": "phq9_submit",
        "event_data": json.dumps({
            "score": 14,
            "severity": "Moderate",
            "answers": [1, 2, 2, 1, 0, 3, 2, 1, 2]
        }),
        "device_info": "Antigravity Local Test Pipeline"
    }
    
    print(f"Inserting row: {event}")
    errors = client.insert_rows_json(table_ref, [event])
    
    if errors == []:
        print("Success! Row successfully inserted into BigQuery.")
        sys.exit(0)
    else:
        print(f"Errors occurred during insert: {errors}")
        sys.exit(1)

if __name__ == "__main__":
    send_mock_event()
