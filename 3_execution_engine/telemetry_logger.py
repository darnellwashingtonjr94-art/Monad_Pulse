import logging
import sys

def setup_telemetry_logger(name="MonadPulseEngine"):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    handler = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(name)s: %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger
