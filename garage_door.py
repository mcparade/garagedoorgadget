#
# Copyright 2019 Amazon.com, Inc. or its affiliates.  All Rights Reserved.
# These materials are licensed under the Amazon Software License in connection with the Alexa Gadgets Program.
# The Agreement is available at https://aws.amazon.com/asl/.
# See the Agreement for the specific terms and conditions of the Agreement.
# Capitalized terms not defined in this file have the meanings given to them in the Agreement.
#

import RPi.GPIO as GPIO
import json
import logging
import sys
import threading
import time

from agt import AlexaGadget

logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logger = logging.getLogger(__name__)

in1 = 23

GPIO.setmode(GPIO.BCM)
GPIO.setup(in1, GPIO.OUT)
GPIO.output(in1, GPIO.HIGH)

class GarageDoor(AlexaGadget):
    """
    An Alexa Gadget that cycles through colors using RGB LED and
    reports the color to the skill upon button press
    """

    def __init__(self):
        super().__init__()

    def on_custom_garagedoor_opengarage(self, directive):
        logger.info('Received open garage directive')
        GPIO.output(in1, GPIO.LOW)
        time.sleep(2)
        GPIO.output(in1, GPIO.HIGH)

    def on_custom_garagedoor_closegarage(self, directive):
        logger.info('Received close garage directive')
        GPIO.output(in1, GPIO.LOW)
        time.sleep(2)
        GPIO.output(in1, GPIO.HIGH)

if __name__ == '__main__':
    try:
        GarageDoor().main()
    finally:
        logger.debug('Clean up')
        IO.cleanup()
