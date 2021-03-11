#!/usr/bin/env python3.9
"""Unbound KeyControl Client API -> Models -> Init
Copyright (C) 2021 Jerod Gawne <https://github.com/jerodg/>

This program is free software: you can redistribute it and/or modify
it under the terms of the Server Side Public License (SSPL) as
published by MongoDB, Inc., either version 1 of the
License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
SSPL for more details.

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

You should have received a copy of the SSPL along with this program.
If not, see <https://www.mongodb.com/licensing/server-side-public-license>."""
from sys import stdout

from loguru import logger

__version__ = '0.2.0'

# Because this is a library; use logger.enable('base_client_api) in script to see log msgs.
logger.add(sink=stdout, colorize=True, enqueue=True)
logger.disable(__name__)