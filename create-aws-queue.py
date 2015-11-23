# This script created a queue
#
# Author - Paul Doyle Nov 2015
#
#
import boto.sqs
import boto.sqs.queue
from boto.sqs.message import Message
from boto.sqs.connection import SQSConnection
from boto.exception import SQSError
import sys

#C13455028
#getting keys from web
import boto
import urllib2
from StringIO import StringIO

req = urllib2.Request('http://ec2-52-30-7-5.eu-west-1.compute.amazonaws.com:81/key')
response = urllib2.urlopen(req)
the_page = response.read()

key1, key2 = the_page.split(':')

print ("user key: ", key1)
print ("pass key: ", key2)


# Get the keys from a specific url and then use them to connect to AWS Service
access_key_id = key1
secret_access_key = key2

# Set up a connection to the AWS service.
conn = boto.sqs.connect_to_region("eu-west-1", aws_access_key_id=access_key_id, aws_secret_access_key=secret_access_key)

#Add a new to list

name = sys.argv[1]
new_queue = conn.create_queue(name)
