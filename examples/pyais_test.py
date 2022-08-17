#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Test application for gr-PyAIS JSON Parser
# Author: muaddib
# GNU Radio version: 3.10.3.0

from gnuradio import ais
from gnuradio import blocks
import pmt
from gnuradio import gr
from gnuradio.filter import firdes
from gnuradio.fft import window
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation




class pyais_test(gr.top_block):

    def __init__(self):
        gr.top_block.__init__(self, "Test application for gr-PyAIS JSON Parser", catch_exceptions=True)

        ##################################################
        # Variables
        ##################################################
        self.NMEA = NMEA = "!AIVDM,1,1,,B,177KQJ5000G?tO`K>RA1wUbN0TKH,0*5C"
        self.NMEA_bytes = NMEA_bytes = [ord(i) for i in NMEA]

        ##################################################
        # Blocks
        ##################################################
        self.pyais_parser_pyais_json_0 = ais.json_parser('/tmp/ais_log.json', True)
        self.blocks_message_strobe_0 = blocks.message_strobe( pmt.cons(pmt.PMT_NIL,pmt.init_u8vector(len(NMEA_bytes),(NMEA_bytes))), 1000)


        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.blocks_message_strobe_0, 'strobe'), (self.pyais_parser_pyais_json_0, 'nmea_in'))


    def get_NMEA(self):
        return self.NMEA

    def set_NMEA(self, NMEA):
        self.NMEA = NMEA
        self.set_NMEA_bytes([ord(i) for i in self.NMEA])

    def get_NMEA_bytes(self):
        return self.NMEA_bytes

    def set_NMEA_bytes(self, NMEA_bytes):
        self.NMEA_bytes = NMEA_bytes
        self.blocks_message_strobe_0.set_msg( pmt.cons(pmt.PMT_NIL,pmt.init_u8vector(len(self.NMEA_bytes),(self.NMEA_bytes))))




def main(top_block_cls=pyais_test, options=None):
    tb = top_block_cls()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        sys.exit(0)

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    tb.start()

    try:
        input('Press Enter to quit: ')
    except EOFError:
        pass
    tb.stop()
    tb.wait()


if __name__ == '__main__':
    main()
