from abc import ABC as AbstractBaseClass, abstractmethod
from EmailSender import send_email
from save_to_database import save_change


# user_id - 8 digit user identification number
# notification - Event type Enum
# relative_path - file's path
# time - datetime object when event occurred -
# delta - changes through the file - optional: only when modification is occurred

class BaseLog(AbstractBaseClass):
    def __init__(self, user_id, notification, time):
        self.user_id = user_id
        self.notification = notification
        self.time = time

    @abstractmethod
    def log(self):
        raise NotImplementedError()


class CriticalLog(BaseLog):
    def __init__(self, user_id, notification, time, message):
        self.message = message
        super(CriticalLog, self).__init__(user_id, notification, time)

    def log(self):
        full_message = f' {self.time} |{self.notification} |{self.message}'
        send_email(full_message)#send email about critical log


class InfoLog(BaseLog):
    def __init__(self, user_id, notification, relative_path, time, delta=None):
        self.relative_path = relative_path
        self.time = time
        self.delta = delta
        super(InfoLog, self).__init__(user_id, notification, time)

    def log(self):
        save_change(self.user_id, self.notification, self.relative_path, self.time, self.delta)#save to database