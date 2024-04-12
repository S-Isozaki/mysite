from django.core import mail
from django.test import TestCase

class MailSendTest(TestCase):
    def test_sendmail(self):
        mail.send_mail(subject="test", message="arrived", from_email="csuscnkr@gmail.com", recipient_list=["i.satoshi1987@gmail.com"],)
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, "test")
        self.assertEqual(mail.outbox[0].body, "arrived")