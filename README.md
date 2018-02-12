# Kafka Twitter Producer

## An example of a simple Kafka Producer written in python

A simple example of a Kafka Producer designed to populate a Kafka Topic (btc_twitter_stream) with tweets about Bitcoin.

### Script Prep

First obtain a set of twitter API keys from [here](http://dev.twitter.com) and place them in the twitter credentials section of the script.

### Environment Prep

First install a python3 environment and pip on all nodes in the cluster that will be running this script

Find instructions on how to do this on centOS [here](https://njanmo.github.io/useful/2018/02/08/hdp-sandbox.html#3)

Then install the external libraries required to run this script:

```
python3 -m pip install -r requirements.txt
```

### Running the script

We assume you have Apache Kafka/Zookeeper installed; if topic is not already created:

First create a Kafka topic: (change replication-factor and partitions to your preference)

```
bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic btc_twitter_stream
```

Once the topic is created run:

```
python /path/to/twitter_producer.py
```

### Troubleshooting

In order to check what topics you have running run:

```
bin/kafka-topics.sh --list --zookeeper localhost:2181
```

In order to check that data is actually landing in Kafka:

```
bin/kafka-console-consumer.sh --zookeeper localhost:2181 --topic btc_twitter_stream --from-beginning
```

Kafka Client port is configured to Hortonworks Ambari default:

```
producer = KafkaProducer(bootstrap_servers=['localhost:6667'])
```

If utilising a standalone Kafka instance replace with:

```
producer = KafkaProducer(bootstrap_servers=['localhost:9092'])
```
