from app.nadya_channel import start
from app.logger import init_logger
import logging
import argparse
from app.storage import init_data_path
from pathlib import Path

dev_token = "1145342159:AAEwfxOCLaQleZtlsJ4X29KE_37MP_qzPSU"
prod_token = "1453698995:AAHjkSKzlG3_7iJqBGY7XgWlKUey84zf4uM"
token = dev_token

parser = argparse.ArgumentParser()
parser.add_argument(
    "--use-webhooks", help="Start with enabled webhooks", action="store_true"
)
args = vars(parser.parse_args())

# start
# init_data_path(Path("data/data.json"))
use_webhooks = args.get("use_webhooks") or False
init_logger()
logging.info("Start Nadya Channel Bot")
logging.info(f"Use webhooks: {use_webhooks}")
start(token, use_webhooks)