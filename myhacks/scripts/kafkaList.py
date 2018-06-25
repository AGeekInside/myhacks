#!/home/mbrooks/.local/share/virtualenvs/mbrooks-hpmZt1LH/bin/python

import click
import os

import myhacks as myh

@click.command()
@click.argument('server', required=False)
def run_kafkaList(server):
    '''Command to list topics on a kafka server.'''

    cmd = f'docker run spotify/kafka /opt/kafka_2.12-1.1.0/bin/kafka-topics.sh --zookeeper {server} --list'

    topic_list = myh.run(cmd, stdout=True)

    print(topic_list)

if __name__ == '__main__':
    run_kafkaList()
