#!/usr/bin/env python
import pika


def enqueue(req, IP):
    # credentials = pika.PlainCredentials('twan', 'root')
    # connection = pika.BlockingConnection(pika.ConnectionParameters(host=IP,port=port,credentials=credentials))

    connection = pika.BlockingConnection(pika.ConnectionParameters(host=IP))

    channel = connection.channel()

    channel.exchange_declare(exchange='topic_logs',
                             exchange_type='topic',
                             durable=True)
    routing_key = req.centerLocation

    channel.basic_publish(exchange='topic_logs',
                          routing_key=routing_key,
                          body=req.to_string(),
                          properties=pika.BasicProperties(
                            delivery_mode=2,
                          ))

    connection.close()
