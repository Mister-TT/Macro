#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
sys.path.append(".")

from macro.logs.logger import get_logger

# 单例
__all__ = ['logger']

logger = get_logger()
