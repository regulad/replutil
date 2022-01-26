from replutil import *
from time import sleep
import logging
from os import environ


def test_keepalive():
    with ReplKeepAlive(environ["UPTIME_ROBOT_TOKEN"]):
        pass
