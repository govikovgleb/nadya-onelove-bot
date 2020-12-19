from app.nadya_channel import start
from app.logger import init_logger
import logging

dev_token = "1145342159:AAEwfxOCLaQleZtlsJ4X29KE_37MP_qzPSU"

init_logger()
logging.info("Start Nadya Channel Bot")
start(dev_token)