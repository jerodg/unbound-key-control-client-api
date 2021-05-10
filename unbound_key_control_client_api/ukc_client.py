#!/usr/bin/env python3.9
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
from typing import NoReturn, Optional, Union

from base_client_api.base_client import BaseClientApi


class UkcClient(BaseClientApi):
    """UKC Client"""

    def __init__(self, cfg: Optional[Union[str, dict]] = None, env_prefix: Optional[str] = 'UKC_'):
        """Initializes Class

        Args:
            cfg (Union[str, dict]): As a str it should contain a full path
                pointing to a configuration file (json/toml). See
                config.* in the examples folder for reference."""
        # print('env_prefix_ukc', env_prefix)
        super().__init__(cfg=cfg, env_prefix=env_prefix)
        # self.HDR =
        # self.load_custom_config()

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type: None, exc_val: None, exc_tb: None) -> NoReturn:
        await super().__aexit__(exc_type, exc_val, exc_tb)

    # def load_custom_config(self) -> NoReturn:
    #     """Load Custom Configuration Data
    #
    #     Returns:
    #         (NoReturn)"""
    #     if usr := getenv(f'{self.env_prefix}Auth_Username'):
    #         self.cfg['Auth']['Username'] = usr
    #
    #     if pswd := getenv(f'{self.env_prefix}Auth_Password'):
    #         self.cfg['Auth']['Password'] = pswd
    #
    #     if uri := getenv('UKC_URI_BASE'):
    #         self.cfg['URI']['Base'] = uri
    #
    #     return


if __name__ == '__main__':
    print(__doc__)
