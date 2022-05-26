"""
This script assumes that the Data Stream has already been created.
"""
from datetime import datetime
import argparse
import time
import calendar
import json
# from authentication import SESSION
import boto3



def send_stream_data(stream_name):
    """
    Sends data from a Kinesis Data Stream.

    Parameters
    ----------
    stream_name: str
    """
    # Connect to a stream
    kinesis = boto3.client('kinesis')

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


# run the function
send_stream_data("stream_name")
