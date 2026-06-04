import boto3
from boto3.dynamodb.conditions import Key

def lambda_handler(event, context):
    print(event)
    tenant_id = event['body']['tenant_id']
    alumno_id = event['body']['alumno_id']
    datos = event['body']['datos']  # dict con campos a actualizar

    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('t_alumnos')

    # Construir expresión de actualización dinámicamente
    update_expr = "SET " + ", ".join(f"#{k} = :{k}" for k in datos)
    expr_names  = {f"#{k}": k for k in datos}
    expr_values = {f":{k}": v for k, v in datos.items()}

    response = table.update_item(
        Key={'tenant_id': tenant_id, 'alumno_id': alumno_id},
        UpdateExpression=update_expr,
        ExpressionAttributeNames=expr_names,
        ExpressionAttributeValues=expr_values,
        ReturnValues="ALL_NEW"
    )

    return {
        'statusCode': 200,
        'tenant_id': tenant_id,
        'alumno_id': alumno_id,
        'alumno': response['Attributes']
    }