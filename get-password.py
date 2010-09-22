#! /usr/bin/python

import gobject, gnomekeyring, pprint

from optparse import OptionParser
parser = OptionParser(add_help_option=False)
parser.add_option("-u", "--user", dest="user",
                  help="The user name", metavar="USER")
parser.add_option("-s", "--server", dest="server",
                  help="The server", metavar="SERVER")
parser.add_option("-c", "--protocol", dest="protocol",
                  help="The protocol", metavar="PROTOCOL")
parser.add_option("-?", "--help", action="help", help="show this help message and exit")

(options, args) = parser.parse_args()

gobject.set_application_name("keyring-utils")

keys = gnomekeyring.find_network_password_sync(user=options.user,
                                              server=options.server,
                                              protocol=options.protocol)
pprint.pprint(keys)
