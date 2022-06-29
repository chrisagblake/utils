import boto3
import time
import logging

log = logging.getLogger(__name__)

def upload_file_s3(file, s3_bucket, s3_name):
    """
    upload a file to s3
    """
    s3 = boto3.client('s3')
    s3.upload_file(file, s3_bucket, s3_name)

def download_files_s3(local_dir, s3_bucket, s3_prefix, file_filter=None):
    """
    download files in a given folder from s3
    """

    # get the list of files to download
    s3 = boto3.client('s3')
    keys = []
    response = s3.list_objects(Bucket=s3_bucket, Prefix=s3_prefix)
    for obj in response['Contents']:
        keys.append(obj['Key'])

    # download the trained model and associated files
    for key in keys:
        log.info(f'downloading: {key}')
        name = key[key.rfind('/')+1:]
        if file_filter is None or name.find(file_filter) >= 0:
            s3.download_file(s3_bucket, key, f'{local_dir}/{name}')

def download_file_s3(s3_bucket, s3_filename, local_filename):
    """
    download a file from s3
    """
    s3 = boto3.client('s3')
    s3.download_file(s3_bucket, s3_filename, local_filename)

def launch_instance(ami, ins_type, use_spot):
    """
    Launch an EC2 instance
    """

    # launch an instance
    log.info('launching instance')
    ec2 = boto3.client('ec2')
    if use_spot:
        res = ec2.run_instances(
            ImageId = ami,
            InstanceType = ins_type,
            InstanceMarketOptions = {'MarketType': 'spot'},
            MaxCount = 1,
            MinCount = 1
        )
    else:
        res = ec2.run_instances(
            ImageId = ami,
            InstanceType = ins_type,
            MaxCount = 1,
            MinCount = 1
        )
    ins_id = res['Instances'][0]['InstanceId']
    log.info(f'id of launched instance: {ins_id}')

    # wait until it's ready
    ins = boto3.resource('ec2').Instance(ins_id)
    while True:
        time.sleep(10)
        state = ins.state['Name']
        if state == 'running':
            break
        else:
            log.info(f'waiting for instance to be ready, current state: {state}')
    ip = ins.public_ip_address
    log.info(f'ip of launched instance: {ip}')
    
    return ins_id, ip

def upload_files_instance(ip, files):
    """
    Upload files to an EC2 instance
    """
    for file in files:
        subprocess.call(['scp', '-o', 'StrictHostKeyChecking=no', file, f'ubuntu@{ip}:~/{file}'])

def run_cmd(ip, cmd):
    """
    run a command within a tmux session on an EC2 instance
    """
    subprocess.call(['ssh', f'ubuntu@{ip}', 'tmux', 'new-session', '-d', cmd])
