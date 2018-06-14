import json, boto3, uuid, sys

sqs = boto3.resource('sqs', region_name="eu-central-1")

tweets = sqs.get_queue_by_name(QueueName='204153ry')
response = tweets.send_message(MessageBody=sys.argv[1])
