import boto3

def lambda_handler(event, context):
    print(event)
    tenant_id = event['body']['tenant_id']
    alumno_id = event['body']['alumno_id']

    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('t_alumnos')

    table.delete_item(
        Key={'tenant_id': tenant_id, 'alumno_id': alumno_id}
    )

    return {
        'statusCode': 200,
        'tenant_id': tenant_id,
        'alumno_id': alumno_id,
        'mensaje': 'Alumno eliminado correctamente'
    }