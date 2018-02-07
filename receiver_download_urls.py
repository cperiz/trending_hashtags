#!/usr/bin/env python
import pika
from lib.download_news import DownloadNews

class Receiver():

    def __init__(self):

        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue='twitter_feed')
        self.channel.basic_consume(self.callback,
                              queue='twitter_feed',
                              no_ack=True)
        self.downloadnews = DownloadNews()

    def callback(self, ch, method, properties, body):
        print(" [x] Received %r" % body)
        if len(body) != 0:
            for tag in body.split(","):
                urls = self.downloadnews.run(tag=tag)
                print(urls) #:print list of urls
                print(tag + " Done.")


if __name__ == '__main__':

    r = Receiver()
    print(' [*] Waiting for tags. To exit press CTRL+C')
    r.channel.start_consuming()
