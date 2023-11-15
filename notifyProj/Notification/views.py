# receive_notifications.py in your_app/management/commands
import json
from django.http import JsonResponse
import pika
from django.core.management.base import BaseCommand
#from Notification.models import Notification  # Import your Django model
print('reciever ...')

def receive_rabbitmq_message(request):
    try:
        connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))
        channel = connection.channel()

        while True:
            method_frame, header_frame, body = channel.basic_get(queue='new_appointment_queue', auto_ack=True)
            latest_message = body.decode('utf-8') if body else None

            if latest_message:
                connection.close()
                #Notification.objects.create(notification_msg=latest_message)
                return JsonResponse({'message': latest_message})
            else:
                # If no message is available, wait for a short period before checking again
                connection.sleep(1)

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
    # print('command ...')
    # msgbody: any
    # help = 'Receive notifications from RabbitMQ and process them'
    # connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    # channel = connection.channel()
    # def callback(ch, method, properties, body):
    #         msgbody = body.decode('utf-8')
    #         #appointment_data = json.loads(body)
    #         # Process appointment_data, for example, save it to the database
    #         #Notification.objects.create(**appointment_data)
    #         print(f"{msgbody}")
    #         return JsonResponse({"status": "sucess"})

    # channel.queue_declare(queue='new_appointment_queue')
    # channel.basic_consume(queue='new_appointment_queue', on_message_callback=callback, auto_ack=True)

    # print('Waiting for notification messages. To exit press CTRL+C')
    # channel.start_consuming()

    

