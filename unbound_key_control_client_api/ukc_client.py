#!/usr/bin/env python3.8
"""Unbound KeyControl Client API -> UKC Client
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
from os import getenv
from typing import List, NoReturn, Optional, Union

from base_client_api.base_client import BaseClientApi


class UkcClient(BaseClientApi):
    """UKC Client"""

    def __init__(self, cfg: Optional[Union[str, dict, List[Union[str, dict]]]] = None):
        """Initializes Class

        Args:
            cfg (Union[str, dict]): As a str it should contain a full path
                pointing to a configuration file (json/toml). See
                config.* in the examples folder for reference."""
        super().__init__(cfg=cfg)
        self.load_custom_config_data()

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type: None, exc_val: None, exc_tb: None) -> NoReturn:
        await super().__aexit__(exc_type, exc_val, exc_tb)

    def load_custom_config_data(self) -> NoReturn:
        """Load Custom Configuration Data

        Returns:
            (NoReturn)"""
        self.cfg['Auth']['Username'] = getenv('UKC_USER')
        self.cfg['Auth']['Password'] = getenv('UKC_PASS')

        if e := getenv('UKC_BASE'):
            self.cfg['URI']['Base'] = e

        return


if __name__ == '__main__':
    print(__doc__)
