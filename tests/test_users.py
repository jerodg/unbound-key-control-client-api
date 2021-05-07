#!/usr/bin/env python3.8
"""Unbound KeyControl Client API -> Tests -> Users
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
from time import perf_counter

import pytest
from base_client_api.models.results import Results
from base_client_api.utils import bprint, tprint
from loguru import logger

from unbound_key_control_client_api.models.users import NewUser, UserCreateOne, UsersListAll
from unbound_key_control_client_api.ukc_client import UkcClient

logger.enable('base_client_api')


@pytest.mark.asyncio
async def test_users_list_all():
    ts = perf_counter()
    bprint('Test: Users List All', 'top')

    async with UkcClient(cfg=f'{getenv("CFG_HOME")}/unbound_test.toml') as ukc:
        m = UsersListAll(partition_id='sandbox',
                         limit=25,
                         skip=3)

        # debug
        # print(m)
        # print(m.parameters)

        results = await ukc.make_request(models=m)

        assert type(results) is Results
        assert results.success is not None
        assert not results.failure

        tprint(results, top=5)

    bprint(f'Completed in {(perf_counter() - ts):f} seconds.', 'bottom')


@pytest.mark.asyncio
async def test_user_create_one():
    ts = perf_counter()
    bprint('Test: User Create One', 'top')

    async with UkcClient(cfg=f'{getenv("CFG_HOME")}/unbound_test.toml') as ukc:
        m = UserCreateOne(partition_id='sandbox',
                          body=NewUser(password='MySuperAwesomeP@ssw0rd',
                                       name='test-client-api-user',
                                       role='test-client-api-role',
                                       # aliases=UserAliases(),  # API isn't accepting this currently
                                       auth_type='STANDARD'))

        # debug
        # print(m)
        # print(m.parameters)
        # print(m.json_body)
        # m.json(exclude={'some_field'})

        results = await ukc.make_request(models=m)

        assert type(results) is Results
        assert results.success is not None
        assert not results.failure

        tprint(results)

    bprint(f'Completed in {(perf_counter() - ts):f} seconds.', 'bottom')
