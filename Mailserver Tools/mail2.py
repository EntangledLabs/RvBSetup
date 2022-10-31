import mailbee2

import argparse

parser = argparse.ArgumentParser(description = "Send mail to all of the bees")
parser.add_argument('mail_path')
parser.add_argument('-s', '--scheme', default=None, choices=[None, 'html', 'HTML'])
parser.add_argument('-a', '--attachment', default=None)

args = parser.parse_args()
mailbee2.mail_bees(args.mail_path, args.scheme, args.attachment)