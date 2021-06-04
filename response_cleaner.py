"""
Takes a given response and finds data points of interest
"""
import json
import datetime
from dateutil.tz import tzlocal # <-- pip install python-dateutil

# Sample response with 2 records
sample_response = {
    'Records': [
        {'SequenceNumber': '49618748789182276128861544561506956099513080195949002754',
         'ApproximateArrivalTimestamp': datetime.datetime(2021, 6, 3, 10, 34, 37, 252000, tzinfo=tzlocal()),
          'Data': b"{'location_id': '1', 'depth': '300', 'status': 'OK'}", 'PartitionKey': '1'},
        {'SequenceNumber': '49618748789182276128861544651461917411218053311705907202',
         'ApproximateArrivalTimestamp': datetime.datetime(2021, 6, 3, 10, 42, 5, 660000, tzinfo=tzlocal()),
          'Data': b"{'location_id': '1', 'depth': '300', 'status': 'OK'}", 'PartitionKey': '1'}
          ],
 'NextShardIterator': 'AAAAAAAAAAHYXSdA2t285XWbOFDkb1DcTjWy75wfpdEi4240XpFEQEga+OA13leGVGbbxt8bE2uwMzHZRk/gDpPX8oC67y6qX7ft59ApVbI1k3J5otfi9e+3C3Rvau7l9zrcPbXkc6RCul0VvEKipIqf9LRPgivzT8BQsRywSR2EZwUXyNSjxdZsAmM/AZCoqhxl5J1einjaRjGJjDPzI3RzJLdjyNdW9uz3NQVyrTUZ9c5GyZrZQQ==',
  'MillisBehindLatest': 80510000, 
  'ResponseMetadata': {
      'RequestId': 'd245342e-f440-1cc2-8b76-edc0d7c5cc58',
      'HTTPStatusCode': 200, 'HTTPHeaders': {
                    'x-amzn-requestid': 'd245342e-f440-1cc2-8b76-edc0d7c5cc58',
                     'x-amz-id-2': 'NrNYuQ4xrP6QX3y/TNxESE8iBHDpqBkGfyOf+OcnVFAy1pgr68D1C3vY1X57zNlt5OhvVIk9xdWQ04uFryAowQf+dlrT3egF',
                     'date': 'Fri, 04 Jun 2021 07:35:10 GMT', 'content-type': 'application/x-amz-json-1.1', 'content-length': '765'},
                      'RetryAttempts': 0
                      }
    }

# If response has record(s), we need to loop to read each of the them.
for i in sample_response['Records']:
    print(i['Data'].decode('ascii')) # Decode the binary string

