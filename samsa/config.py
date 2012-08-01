__license__ = """
Copyright 2012 DISQUS

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
from samsa.metrics import BaseMetricReporter

def build(target, kwargs=None, validate=True):
    """Update target with kwargs and return the resulting dict.

    default values exist in `base`.
    """

    config = dict(base)
    config.update(target)

    for k in kwargs or []:
        if validate and k not in config:
            raise AttributeError("%s not in config." % k)
        config[k] = kwargs[k]

    return config


base = {
    'metrics': BaseMetricReporter.instance()
}

consumer = {
    # controls the socket timeout for network requests
    'socket_timeout_ms': 30000 ,

    # controls the socket receive buffer for network requests
    'socket_buffersize': 64 * 1024 ,

    # controls the number of bytes of messages to attempt to fetch in one request to the Kafka server
    'fetch_size': 300 * 1024 ,

    # This parameter avoids repeatedly polling a broker node which has no new data. We will backoff every time we get an empty set from the broker for this time period
    'backoff_increment_ms': 1000 ,

    # the high level consumer buffers the messages fetched from the server internally in blocking queues. This parameter controls the size of those queues
    'queuedchunks_max': 100 ,

    # if set to true, the consumer periodically commits to zookeeper the latest consumed offset of each partition.
    'autocommit_enable': True ,

    # is the frequency that the consumed offsets are committed to zookeeper.
    'autocommit_interval_ms': 10000 ,

    # smallest: automatically reset the offset to the smallest offset available on the broker.
    # largest : automatically reset the offset to the largest offset available on the broker.
    # anything else: throw an exception to the consumer.
    'autooffset_reset': 'smallest',

    # By default, this value is -1 and a consumer blocks indefinitely if no new message is available for consumption. By setting the value to a positive integer, a timeout exception is thrown to the consumer if no message is available for consumption after the specified timeout value.
    'consumer_timeout_ms': -1 ,

    # max number of retries during rebalance
    'rebalance_retries_max': 4 ,
}
