#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2022 gr-ais author.
#
# SPDX-License-Identifier: GPL-3.0-or-later
#

from gnuradio import gr
import pmt
import pyais.decode as pyais_decode
import array
import json

class pyais_json(gr.sync_block):
    """
    docstring for block pyais_json
    """
    def __init__(self, logtofile=False, filename='/tmp/ais.log', console_output=True):
        gr.sync_block.__init__(self,
            name="pyais_json",
            in_sig=None,
            out_sig=None)

        self.portName = 'nmea_in'
        self.message_port_register_in(pmt.intern(self.portName))
        self.set_msg_handler(pmt.intern('nmea_in'), self.handle_msg)
        # if an attribute with the same name as a parameter is found,
        # a callback is registered (properties work, too).
        self.console_output = console_output
        self.filename = filename
        self.logtofile = logtofile
        self.first = True
        self.cnt = 0
        self.recs=[]
    def handle_msg(self, msg):
        if msg is not None:
            PMT_msg = pmt.to_python(msg)
            byte_array_msg = array.array('B', PMT_msg[1])
            byte_msg = bytes(byte_array_msg)
            aisjson = {f'ais_record_{self.cnt}':json.loads(pyais_decode(byte_msg).to_json())}
            self.recs.append(aisjson)
            if self.console_output == True:
                print(json.dumps(aisjson,indent=2))
            if self.logtofile==True:
                if self.first==True:
                    with open(self.filename,'w') as fobj:
                        json.dump(self.recs,fobj)
            self.cnt+=1
