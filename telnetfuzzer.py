#!/usr/bin/env python
#
# *****************************************************************
#               Username/Password Telnet Fuzzer
# *****************************************************************
#
# Author: Nick Aliferopoulos
# aliferopoulos@icloud.com
#

from telnetlib import *
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter

class TelnetFuzzer(object):

    def __init__(self, host, port=23):
        self.host = host
        self.port = port

    def fuzz(self):
        print("Starting Telnet fuzzing %s:%i" % (self.host, self.port))
        tn = Telnet()
        for buflen in range(10,20):
        	tn.open(self.host, self.port)
                buf = 'A' * buflen
                print("Buffer length: %i 0x%X" % (len(buf), len(buf)))
                tn.read_until('Username :')
                tn.write(buf + '\r\n')
		tn.read_until('Password :')
                tn.write(buf + '\r\n')
		tn.close()

def main():
    parser = ArgumentParser(description='Telnet Fuzzer', formatter_class=ArgumentDefaultsHelpFormatter)
    parser.add_argument('host', help = 'Target host')
    parser.add_argument('-p', '--port',  type = int, default=23, required = False, help = 'Target port')
    parser.add_argument('-v', '--version', action = 'version', version = '%(prog)s 1.0')
    args = parser.parse_args()

    tf = TelnetFuzzer(args.host, args.port)
    tf.fuzz()

if __name__ == '__main__':
    main()
