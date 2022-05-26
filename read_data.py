from datetime import datetime
import time
import boto3
from dateutil.tz import tzlocal


def read_stream(stream_name, shard_id):
    """
    Reads data from a Kinesis Data Stream.

    Parameters
    ----------
    stream_name: str
    shard_id: str
    """
    # Connect to a stream
    kinesis = boto3.client('kinesis')

    # Get current shard-iterator
    shard_iterator = kinesis.get_shard_iterator(
        StreamName=stream_name,
        ShardId=shard_id,
        ShardIteratorType='TRIM_HORIZON',
    )
    print(shard_iterator)

    # Get records, whilst looping through iterators
    shard_iter = shard_iterator['ShardIterator']

    for i in range(100):
        resp = kinesis.get_records(ShardIterator=shard_iter)
        next_shard_iterator = resp['NextShardIterator']
        print(f"Last 5 chars of Current Shard Iterator: {shard_iter[-5:]}")
        print(f"Last 5 chars of New Shard Iterator: {next_shard_iterator[-5:]}")
        print(resp)
        # If records exist, read data
        if len(resp['Records']) >= 1:
            for i in resp['Records']:
                print(i['Data'].decode('ascii'))
        
        # Make NextShardIterator received from response the new one to use
        shard_iter = next_shard_iterator
        print(f"Last 5 chars of Shard Iter for next loop: {shard_iter[-5:]}")

        # Wait a few seconds before running the loop again
        time.sleep(30)

# run the function
read_stream("stream_name", "shard_id")