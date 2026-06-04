import boto3

def lambda_handler(event, context):
    print(event)
    tenant_id = event['body']['tenant_id']
    alumno_id = event['body']['alumno_id']

    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('t_alumnos')

    response = table.get_item(
        Key={'tenant_id': tenant_id, 'alumno_id': alumno_id}
    )

    item = response.get('Item')

    if not item:
        return {
            'statusCode': 404,
            'tenant_id': tenant_id,
            'alumno_id': alumno_id,
            'mensaje': 'Alumno no encontrado'
        }

    return {
        'statusCode': 200,
        'tenant_id': tenant_id,
        'alumno': item
    }