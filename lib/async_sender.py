#!/usr/bin/env python
import pika

class Sender():

    def send_msg(self, msg, name):
        connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        channel = connection.channel()
        channel.queue_declare(queue=name)
        channel.basic_publish(exchange='',
                        routing_key=name,
                        body=msg)
        connection.close()
