#!/home/mbrooks/.local/share/virtualenvs/mbrooks-hpmZt1LH/bin/python

import click
import os

import myhacks as myh

@click.command()
@click.argument('server', required=True)
@click.argument('topic', required=True)
def run_kafkaConsume(server, topic):
    '''Launches a kafka client to start consuming a given topic.'''

    base_cmd = f'docker run spotify/kafka /opt/kafka_2.12-1.1.0/bin/kafka-console-consumer.sh '
    options = f'--bootstrap-server {server} --topic {topic}'
    cmd = base_cmd + options

    myh.run(cmd, stdout=True)


if __name__ == '__main__':
    run_kafkaConsume()
