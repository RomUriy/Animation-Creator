import json, boto3, uuid

sqs = boto3.resource('sqs', region_name="eu-central-1")

tweets = sqs.get_queue_by_name(QueueName='204153')

while True:
  for message in tweets.receive_messages():
    print('Message body: %s' % message.body)
    message.delete()
  time.sleep(1)