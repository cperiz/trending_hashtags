#!/usr/bin/env python
import pika
from lib.plotter import PlotHist

class Receiver():

    def __init__(self):

        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue='hash_feed')
        self.channel.basic_consume(self.callback,
                              queue='hash_feed',
                              no_ack=True)
        self.plot_hist = PlotHist('b')

    def callback(self, ch, method, properties, body):
        print(" [x] Received %r" % body)
        if len(body) > 0:
            body = body.decode('utf-8')
            tup_list = [r.split("|::|") for r in body.split("|||")]
            #: decode unicode and int
            tup_list = [(i[0], int(i[1])) for i in tup_list]
            self.plot_hist.plot(tup_list=tup_list)


if __name__ == '__main__':

    r = Receiver()
    print(' [*] Waiting for tags. To exit press CTRL+C')
    r.channel.start_consuming()
