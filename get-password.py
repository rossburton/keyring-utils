#! /usr/bin/python

import gobject, gnomekeyring

from optparse import OptionParser
parser = OptionParser(add_help_option=False)
parser.add_option("-u", "--user", dest="username",
                  help="The user name", metavar="USER")
parser.add_option("-h", "--host", dest="hostname",
                  help="The host name", metavar="HOST")
parser.add_option("-?", "--help", action="help", help="show this help message and exit")

(options, args) = parser.parse_args()

gobject.set_application_name("offlineimap")

keys = gnomekeyring.find_network_password_sync(user=options.username,
                                              server=options.hostname,
                                              protocol="imap")
print keys[0]["password"]
