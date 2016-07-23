#!/usr/bin/env python3

from errbot import BotPlugin, botcmd
import telnetlib


class Weatherinfo(BotPlugin):
    """grab short weather informations around the globe
    """


    @botcmd(split_args_with=None)
    def weather(self, msg, args):
        """(!weather berlin) grab weather information for cities an regions
        """
        host = 'graph.no'
        port = 79
        timeout = 1
        city = args[0]

        tn = telnetlib.Telnet(host, port, timeout)
        tn.write(str('o:' + city + '\n').encode('ascii'))
        ret = tn.read_all()
        if b'yr.no is having technical problems' not in ret:
            return ret.decode('utf-8')
        else:
            return 'could not find city/region or something went wrong'