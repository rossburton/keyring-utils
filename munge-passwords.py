#! /usr/bin/python

import gobject
import gnomekeyring as keyring

from optparse import OptionParser
parser = OptionParser(add_help_option=False)
parser.add_option("-o", "--old", dest="old",
                  help="The old password", metavar="PASSWORD")
parser.add_option("-n", "--new", dest="new",
                  help="The new password", metavar="PASSWORD")
parser.add_option("-?", "--help", action="help", help="show this help message and exit")

(options, args) = parser.parse_args()
if options.old is None or options.new is None:
    parser.error("You must provide old and new passwords")
    
gobject.set_application_name("keyring-utils")

for item_id in keyring.list_item_ids_sync("login"):
    item = keyring.item_get_info_sync("login", item_id)
    if item.get_secret() == options.old:
        print item.get_display_name()
        item.set_secret(options.new)
        keyring.item_set_info_sync("login", item_id, item)
