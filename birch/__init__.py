#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
# Part of Birch. See LICENSE file for full copyright and licensing details.

'''
This is the main package of Birch service.
'''

__author__ = "Richard Cooper"
__copyright__ = "Copyright 2018, XELAJ technologies"
__credits__ = ["Richard Cooper"]
__license__ = "GNU GPLv3"
__version__ = "1.0.3-alpha"
__maintainer__ = "XELAJ technologies"
__email__ = "rcooper.xelaj@protonmail.com"
__status__ = "Development"

import sys

from . import api
from . import cli
from . import utils
from .configurator import configurator

args = cli.args()
cfg = configurator(args.cfg_path)
name = __name__.capitalize()

if not args.debug:
    args.debug = cfg['MAIN'].getboolean('debug')

def main():
    if not args.hide_logo:
        utils.show_logo(cfg['MAIN']['name'])

    if not args.debug:
        import logging
        l = logging.getLogger('werkzeug')
        l.setLevel(logging.ERROR)

    utils.log(name,'INFO',name+' is active! running on '+
                              cfg['SERVER']['host']+':'+cfg['SERVER']['port'])


    api.app.run(host=cfg['SERVER']['host'],
                port=int(cfg['SERVER']['port']),
                debug=args.debug)
