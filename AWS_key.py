
import boto
import urllib2
from StringIO import StringIO

req = urllib2.Request('http://ec2-52-30-7-5.eu-west-1.compute.amazonaws.com:81/key')
response = urllib2.urlopen(req)
the_page = response.read()

key1, key2 = the_page.split(':')

print ("Boto version: ", boto.Version)
print ("user key: ", key1)
print ("pass key: ", key2)
