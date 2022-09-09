#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Script sends a mail with a daily quote.
"""

__author__ = "Martin Pucovski"
__copyright__ = "Copyright 2022, Martin Pucovski"
__credits__ = ["Martin Pucovski"]
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Martin Pucovski"
__email__ = "martin@pucov.ski"
__status__ = "Production"

import configparser
import datetime
import logging
import smtplib
import secrets
from email.mime.text import MIMEText
import csv
import random
import os


# Create and configure logger
current_day = datetime.datetime.now().strftime("%Y%m%d")

logging.basicConfig(filename=fr"logs\{current_day}_log.log",
                    format='%(asctime)s %(levelname)s %(message)s',
                    filemode='a')

# Creating an object
logger = logging.getLogger()

# Setting the threshold of logger
logger.setLevel(logging.INFO)

logger.info("####################")
logger.info("Script started")

# read config.ini file
logger.info("Reading config")
config = configparser.ConfigParser()
config.read(r'config\config.ini')
config_default = config['DEFAULT']

# set variable values
quotes_file = os.path.join('data', config_default['quote_file_name'])
template_file = os.path.join('data', config_default['mail_template_file'])

def send_mail(mail_subject: str, mail_message: str) -> None:
    """
    Module to send mail message

    :param mail_message: text of the mail message
    :returns: None
    """
    sender = secrets.smtp_username
    receivers = [secrets.recipient]

    msg = MIMEText(mail_message)
    msg['Subject'] = mail_subject
    msg['From'] = sender
    msg['To'] = ",".join(receivers)

    server = smtplib.SMTP_SSL(secrets.smtp_server, secrets.smtp_port)
    server.login(secrets.smtp_username, secrets.smtp_password)
    server.sendmail(sender, receivers, msg.as_string())
    server.quit()


def get_quotes() -> list:
    """
    Read csv file with all the quotes.

    Return should be a 2-D list with following element order: quote, book, part, chapter

    :param mail_message: text of the mail message
    :returns: list
    """
    # read file with quotes
    with open(quotes_file, newline='', encoding="utf8") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        all_rows = []
        for one_row in csv_reader:
            all_rows.append(one_row)

    return all_rows


def main():
    """
    Main method
    """
    # get all quotes in 2-D list
    all_quotes = get_quotes()

    # get random index
    number_of_quotes = len(all_quotes)
    quote_index = random.randrange(1, number_of_quotes)

    # build mail message text
    with open(template_file, newline='', encoding="utf8") as mail_template:
        template = mail_template.read()
    mail_message = template.format(all_quotes[quote_index][0], all_quotes[quote_index][1], all_quotes[quote_index][2], all_quotes[quote_index][3])

    # send mail with
    send_mail(mail_subject=config_default['mail_subject'], mail_message=mail_message)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logger.error(str(e))
    finally:
        logger.info("Script ended")
        logger.info("####################")
