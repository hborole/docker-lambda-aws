import numpy as np


def lambda_handler(event, context):
    arr = np.random.randint(0, 10, (3, 3))
    print(event)
    return {
        'statusCode': 200,
        'body': {'message': 'Hello from Lambda!', 'arr': arr.tolist()}
    }
