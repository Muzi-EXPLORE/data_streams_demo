# data_streams_demo
Repo with 2 scripts used to demo Kinesis data streams  
Can be usefull as a demo to show how streams work.

## Send Data
'send_data.py' runs a loop used to generate and send data to a stream.
New data is sent every 15 seconds

## Read Data
'read_data.py' runs a loop used to consume/read data from a stream.
Runs a loop that fetches data every 30 seconds

## Response Cleaner
'response_cleaner.py' shows what a typical response would look like and how to clean or read data from it.


## Step 1 - SETUP
### Create your python virtual environment
```
python -m venv env
```

### Activate your environment (Linux/Mac)
```
source env/bin/activate
```

### Activate your environment (Windows)
```
env/Scripts/activate.bat
```

### Check if you virtual environment has been activated (Windows)
```
which python
```
If the output is `c:/users/python`, the environment hasn't been activated.  
If it's along the lines `/c/Users/Admin/Documents/AWS/aws_vouchers/\Users\Admin\Documents\AWS\aws_vouchers\env/Scripts/python`,  it means it's been activated.  
You're also going to see the name of the enviroment in your prompt `(env) Username@PCName ~/...`  

### Check if you virtual environment has been activated (Linux/Mac)
```
which python3
```
If the output is `/usr/bin/python3`, the environment hasn't been activated.  
If it's along the lines `usr/scripts/project_folder/env_name/bin/python` it means it's been activated.  
You're also going to see the name of the enviroment in your prompt `(env) Username@PCName: ~/...`  

### Install Dependencies
```
pip install -r requirements.txt
```

### Deactivate virtual environment (Run when done)
```
deactivate
```

## Step 2 - Create Stream on Kinesis
Use the AWS Management Console or the AWS CLI
```
aws kinesis create-stream \
    --stream-name blazingfast \
    --shard-count 1
```

### Send data to stream
Modify the stream name inside send_data.py  
Run the script


### Read data from your stream
Modify the stream name and shard id inside read_data.py  
Run the script

### Cleaning responses from Kinesis
response_cleaner.py
