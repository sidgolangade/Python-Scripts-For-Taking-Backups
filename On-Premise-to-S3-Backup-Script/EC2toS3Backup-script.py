import boto3
import tarfile
import schedule
import time
import datetime
import os

# Create an S3 access object
s3 = boto3.client("s3")

# Specify the file paths
local_file_path = "/Users/siddhantgolangade/Documents/VScode-Directory/FolderForBackup/DummyFile.txt"
s3_bucket = "sg-s3-bucket-1"
backup_count = 0

def backup_job():
    global backup_count
    
    # Check if the maximum backup limit for the day is reached
    if backup_count >= 3:
        return
    
    # Compress the file using tar and gzip
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    tar_file_path = f"{local_file_path}_{timestamp}.tar.gz"
    with tarfile.open(tar_file_path, "w:gz") as tar_file:
        tar_file.add(local_file_path, arcname="memo.txt")
    
    # Upload the tar file to S3
    s3_key = f"backup_{timestamp}.tar.gz"
    s3.upload_file(
        Filename=tar_file_path,
        Bucket=s3_bucket,
        Key=s3_key
    )
    
    # Remove the temporary tar file
    os.remove(tar_file_path)
    
    # Increment the backup count
    backup_count += 1

# Schedule the backup job
schedule.every(1).minutes.do(backup_job)

# Keep track of backup iterations
backup_count = 0
max_backups = 3

# Run the scheduler
while True:
    schedule.run_pending()
    time.sleep(1)
    
    if backup_count >= max_backups:
        print(f"Maximum backups per day ({max_backups}) reached. Exiting for today.")
        break