#!/usr/bin/env python
import pika

class Sender():

    def send_msg(self, msg):
        connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        channel = connection.channel()
        channel.queue_declare(queue='twitter_feed')
        channel.basic_publish(exchange='',
                        routing_key='twitter_feed',
                        body=msg)
        connection.close()
