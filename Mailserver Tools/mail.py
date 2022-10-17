import mailbee

import argparse

parser = argparse.ArgumentParser(description = "Send mail to all of the bees")
parser.add_argument('mail_path')

args = parser.parse_args()
mailbee.mail_bees(args.mail_path)