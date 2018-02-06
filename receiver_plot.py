#!/usr/bin/env python
import pika
from lib.plotter import PlotHist

class Receiver():

    def __init__(self):

        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue='twitter_feed')
        self.channel.basic_consume(self.callback,
                              queue='twitter_feed',
                              no_ack=True)
        self.plot_hist = PlotHist()

    def callback(self, ch, method, properties, body):
        print(" [x] Received %r" % body)
        if len(body) > 0:
            body = body.decode('utf-8')
            hash_tup_list = [r.split("|::|") for r in body.split("|||")]
            #: decode unicode and int
            hash_tup_list = [(i[0], int(i[1])) for i in hash_tup_list]
            self.plot_hist.plot(tup_list=hash_tup_list)


if __name__ == '__main__':

    r = Receiver()
    print(' [*] Waiting for tags. To exit press CTRL+C')
    r.channel.start_consuming()
