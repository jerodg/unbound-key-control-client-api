#!/usr/bin/env python3.9
"""Copyright (C) 2021 Jerod Gawne <https://github.com/jerodg/>

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
import asyncio
from os.path import basename
from sys import stdout
from typing import Union

from base_client_api import BaseClientApi, Results

from unbound_keycontrol_client_api import logger


class UkcClient(BaseClientApi):
    """UKC Client"""

    def __init__(self, cfg: Union[str, dict]):
        """Initializes Class

        Args:
            cfg (Union[str, dict]): As a str it should contain a full path
                pointing to a configuration file (json/toml). See
                config.* in the examples folder for reference."""
        BaseClientApi.__init__(self, cfg=cfg)
        self.cfg: Union[str, dict]

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await BaseClientApi.__aexit__(self, exc_type, exc_val, exc_tb)

    @logger.catch
    async def make_call(self):
        pass


if __name__ == '__main__':
    print(__doc__)
