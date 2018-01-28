# Kafka Twitter Producer

## An example of a simple Kafka Producer written in python

### Environment Prep

First install a python environment and pip on all nodes in the cluster that will be running this script

Then install the external libraries required to run this script

```
pip install -r requirements.txt
```

### Running the script

We assume you have Apache Kafka installed; if topic is not already created:

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
