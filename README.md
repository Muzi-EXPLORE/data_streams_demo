# data_streams_demo
Repo with 2 scripts used to demo Kinesis data streams  
Can be usefull as a demo to show how streams work.
Can also be incorporated onto train 8.3 under the part 4 of the Practical Exercise

## Send Data
'send_data.py' runs a loop used to generate and send data to a stream.
New data is sent every 15 seconds

## Read Data
'read_data.py' runs a loop used to consume/read data from a stream.
Runs a loop that fetches data every 30 seconds

## Response Cleaner
'response_cleaner.py' shows what a typical response would look like and how to clean or read data from it.