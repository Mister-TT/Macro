#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
sys.path.append("")

from loguru import _Logger, _Core
from macro.config.config import Config


def get_logger(**log_config):
    config = Config.log_config
    config.update(log_config)
    logger = _Logger(_Core(), None, 0, False, False,
                     False, False, True, None, {})
    logger.configure(**config)
    return logger


if __name__ == '__main__':
    logger = get_logger()

