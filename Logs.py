import logging
from datetime import datetime
from abc import ABC as AbstractBaseClass
import smtplib

from EmailSender import send_email

EMAIL = 'spydir1209@gmail.com'
PORT = 465
PASSWORD = ''

class BaseLog(AbstractBaseClass):
    def __init__(self, IP, user, message, time):
        self.IP = IP
        self.user = user
        self.message = message
        self.time = time


class CriticalLog(BaseLog):
    def __init__(self, IP, user, message, time):
        super(CriticalLog, self).__init__(IP, user, message, time)
        send_email(EMAIL, IP, message)  # send critical changes to attacker


class InfoLog(BaseLog):
    def __init__(self, IP, user, message, time):
        super(InfoLog, self).__init__(IP, user, message, time)


class VerboseLog(BaseLog):
    def __init__(self, IP, user, message, time):
        super(VerboseLog, self).__init__(IP, user, message, time)
