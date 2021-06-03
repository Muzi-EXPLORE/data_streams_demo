from datetime import datetime
import time
import boto3

# Connect to a stream
kinesis = boto3.client('kinesis')
stream_name = '' # <-- Stream name goes here
shard_id = "" # <--- Shard ID goes here


# Get current shard-iterator
shard_iterator = kinesis.get_shard_iterator(
    StreamName=stream_name,
    ShardId=shard_id,
    ShardIteratorType='TRIM_HORIZON',
)
print(shard_iterator)


# Get records, whilst looping through iterators
shard_iter = shard_iterator['ShardIterator']
for i in range (100):
    resp = kinesis.get_records(ShardIterator=shard_iter)
    next_shard_iterator = resp['NextShardIterator']
    print(f"Last 5 chars of Current Shard Iterator: {shard_iter[-5:]}")
    print(f"Last 5 chars of New Shard Iterator: {next_shard_iterator[-5:]}")
    print(resp)
    shard_iter = next_shard_iterator
    print(f"Last 5 chars of Shard Iter for next loop: {shard_iter[-5:]}")
    time.sleep(30)
