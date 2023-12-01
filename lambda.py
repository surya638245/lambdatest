import json

def lambda_handler(event, context):
    # Parse the event data
    event_data = json.loads(json.dumps(event))

    # Your logic here: Perform operations based on the event data
    # For example, you might process data, call other services, etc.

    # Print a message (this would appear in CloudWatch Logs)
    print("Hi Surya this code is run")

    # Return a response (optional)
    return {
        'statusCode': 200,
        'body': json.dumps('Lambda function executed successfully!')
    }
