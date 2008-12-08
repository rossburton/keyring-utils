#! /usr/bin/python

import sys, gobject, gnomekeyring
from optparse import OptionParser

gobject.set_application_name("keyring-utils")

parser = OptionParser(add_help_option=False)
parser.add_option("-u", "--user", dest="user",
                  help="The user name", metavar="USER")
parser.add_option("-d", "--domain", dest="domain",
                  help="The domain", metavar="DOMAIN")
parser.add_option("-s", "--server", dest="server",
                  help="The server", metavar="SERVER")
parser.add_option("-o", "--object", dest="object",
                  help="The remote object", metavar="OBJECT")
parser.add_option("-c", "--protocol", dest="protocol",
                  help="The protocol", metavar="PROTOCOL")
parser.add_option("-a", "--authtype", dest="authtype",
                  help="The authentication type", metavar="TYPE")
parser.add_option("-p", "--port", dest="port", type="int",
                  help="The port", metavar="PORT")
parser.add_option("-w", "--password", dest="password",
                  help="The password", metavar="PASSWORD")
parser.add_option("-?", "--help", action="help", help="show this help message and exit")

parser.set_defaults(user=None,
                    domain=None,
                    server=None,
                    object=None,
                    protocol=None,
                    authtype=None,
                    port=0,
                    password=None)
(options, args) = parser.parse_args()

# This is the only required argument
if options.password is None:
    parser.print_help()
    sys.exit(1)

gnomekeyring.set_network_password_sync(
    user=options.user,
    domain=options.domain,
    server=options.server,
    object=options.object,
    protocol=options.protocol,
    authtype=options.authtype,
    port=options.port,
    password=options.password)
