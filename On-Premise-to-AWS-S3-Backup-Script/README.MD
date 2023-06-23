# Local Machine to AWS S3 Backup Script
The S3 Backup Script is a Python script that automates the process of creating backups of a specified file and uploading them to an Amazon S3 bucket at regular intervals. It utilizes the Boto3 library to interact with the Amazon S3 service and the Schedule library to schedule the backup job.

## Prerequisites
- Python 3.x
- Boto3 library (pip install boto3)
- Schedule library (pip install schedule)
- S3 Bucket (Create via AWS Console)
- IAM User, Privileges, Policies for S3 Bucket (Create via AWS Console)

## Usage
The script will start creating backups at the specified intervals and upload them to the Amazon S3 bucket. It will automatically stop when the maximum number of backups for the day is reached.

## Customization

- Adjust the backup frequency: In the backup_job function, you can modify the schedule using the schedule.every(...) statement. For example, to change the backup frequency to every 2 hours, you can use schedule.every(2).hours.do(backup_job).
- Modify the backup file format: In the backup_job function, you can update the filename format of the tar archive and the key name for the S3 object by modifying the respective variables (tar_file_path and s3_key).
- Change the backup limit: In the max_backups variable, you can adjust the maximum number of backups allowed per day.
- Customize IAM user credentials: If you prefer not to use environment variables or the AWS CLI configuration for authentication, you can specify the Access Key ID and Secret Access Key directly in the script using the aws_access_key_id and aws_secret_access_key parameters when creating the S3 client object (s3 = boto3.client("s3", aws_access_key_id="YOUR_ACCESS_KEY_ID", aws_secret_access_key="YOUR_SECRET_ACCESS_KEY")).