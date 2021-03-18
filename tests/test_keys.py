#!/usr/bin/env python3.9
"""Unbound KeyControl Client API -> Tests -> Keys
Copyright © 2019-2021 Jerod Gawne <https://github.com/jerodg/>

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
from base_client_api.models.results import Results
from base_client_api.utils import bprint, tprint
from loguru import logger

from unbound_key_control_client_api.models.keys import KeyDeleteOne, KeyFormat, KeyGenerateOne, KeyProperties, KeysListAll, NewKey
from unbound_key_control_client_api.ukc_client import UkcClient

logger.enable('base_client_api')


@pytest.mark.asyncio
async def test_keys_list_all():
    ts = time.perf_counter()
    bprint('Test: Keys List All', 'top')

    async with UkcClient(cfg=f'{getenv("CFG_HOME")}/unbound_snd.toml') as ukc:
        m = KeysListAll(partition_id='sandbox',
                        limit=25,
                        skip=3,
                        id=None,
                        type=None,
                        export_type=None,
                        trusted=None,
                        groups=None,
                        state=None,
                        is_enabled=True,
                        show_destroyed=False)

        # print(m.parameters)  # debug

        results = await ukc.make_request(models=m)

        assert type(results) is Results
        assert results.success is not None
        assert not results.failure

        tprint(results, top=5)

    bprint(f'Completed in {(time.perf_counter() - ts):f} seconds.', 'bottom')


@pytest.mark.asyncio
async def test_key_generate_one():
    ts = time.perf_counter()
    bprint('Test: Key Generate One', 'top')

    async with UkcClient(cfg=f'{getenv("CFG_HOME")}/unbound_snd.toml') as ukc:
        m = KeyGenerateOne(user_id='',
                           partition_id='sandbox',
                           body=NewKey(key_id='test_client_key',
                                       key_id_encoding=None,
                                       key_properties=KeyProperties(description='test_client_key',
                                                                    supported_operations=['SIGN', 'DERIVE', 'ENCRYPT', 'DECRYPT'],
                                                                    trusted=True,
                                                                    key_rotation_interval=333,
                                                                    export_type='WRAPPED_WITH_TRUSTED',
                                                                    groups=['default', 'g.general.read']),
                                       key_store_properties=None,
                                       # KeyStoreProperties(keyStoreName=None,
                                       #                                       keyStoreObjectId=None,
                                       #                                       byok=None)
                                       activate=True,
                                       activation_date=None,
                                       deactivation_date=None,
                                       key_format=KeyFormat(type='ECC',
                                                            size='521',
                                                            curve='P521',
                                                            offline_key_params=None
                                                            # OfflineKeyParams(backup=None,
                                                            #                                   paillier_key=None,
                                                            #                                   paillier_keys=None)
                                                            )))

        # debug
        # print(m.parameters)
        # print(m.json_body)

        results = await ukc.make_request(models=m)

        assert type(results) is Results
        assert results.success is not None
        assert not results.failure

        tprint(results)

    bprint(f'Completed in {(time.perf_counter() - ts):f} seconds.', 'bottom')


@pytest.mark.asyncio
async def test_key_delete_one():
    ts = time.perf_counter()
    bprint('Test: Key Delete One', 'top')

    async with UkcClient(cfg=f'{getenv("CFG_HOME")}/unbound_snd.toml') as ukc:
        m = KeyDeleteOne(partition_id='sandbox',
                         key_id='test_client_key',
                         full_delete=True)

        # debug
        # print(m.parameters)
        # print(m.endpoint)

        results = await ukc.make_request(models=m)

        assert type(results) is Results
        assert results.success is not None
        assert not results.failure

        tprint(results)

    bprint(f'Completed in {(time.perf_counter() - ts):f} seconds.', 'bottom')
