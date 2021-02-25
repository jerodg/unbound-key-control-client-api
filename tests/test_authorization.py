#!/usr/bin/env python3.9
"""UKC->Tests->Authorization Copyright (C) 2021 Jerod Gawne <https://github.com/jerodg/>

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
import time
from os import getenv

import pytest

from base_client_api import bprint, Results, tprint
from unbound_keycontrol_client_api import UkcClient


@pytest.mark.asyncio
async def test_login():
    ts = time.perf_counter()

    bprint('Test: Login')
    async with UkcClient(cfg=f'{getenv("CFG_HOME")}/unbound_snd.toml') as ukc:
        results = await ukc.authenticate()

        # assert type(results) is Results
        # assert len(results.success) == 1
        # assert not results.failure
        # assert results.success['UserId']

        tprint(results)

    bprint(f'-> Completed in {(time.perf_counter() - ts):f} seconds.')
