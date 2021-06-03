from datetime import datetime
import time
import calendar
import json
import boto3

# Connect to a stream
kinesis = boto3.client('kinesis')
stream_name = '' # <-- Stream name goes here

# Creaste data to write to stream
for x in range(1000):
    data = f"Number: {x}"
    timestamp = datetime.timestamp(datetime.now())
    payload = {
        'timestamp': str(timestamp),
        'the_data': data
    }

    # Write to stream
    resp = kinesis.put_record(
                StreamName=stream_name,
                Data=json.dumps(payload),
                PartitionKey='1'
    )

    # Print resp
    print(resp)

    # Sleep
    time.sleep(15)
