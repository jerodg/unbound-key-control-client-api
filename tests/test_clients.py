#!/usr/bin/env python3.9
"""Unbound KeyControl Client API -> Tests -> Clients
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
from pydantic import ValidationError
from rich import print

from unbound_key_control_client_api.models.clients import (ClientCreateOne, ClientRefreshActivationCode, ClientsListAll,
                                                           RefreshedCertificateClient)
from unbound_key_control_client_api.ukc_client import UkcClient

logger.enable('base_client_api')


@pytest.mark.asyncio
async def test_clients_list_all():
    ts = time.perf_counter()
    bprint('Test: Clients List All', 'top')

    async with UkcClient(cfg=f'{getenv("CFG_HOME")}/unbound_snd.toml') as ukc:
        m = ClientsListAll(limit=25, skip=3, partitionId='sandbox')
        print(m.parameters)
        results = await ukc.make_request(models=m)

        assert type(results) is Results
        assert results.success is not None
        assert not results.failure

        tprint(results, top=5)

    bprint(f'Completed in {(time.perf_counter() - ts):f} seconds.', 'bottom')


@pytest.mark.asyncio
async def test_client_create_one():
    ts = time.perf_counter()
    bprint('Test: Client Create One', 'top')

    async with UkcClient(cfg=f'{getenv("CFG_HOME")}/unbound_snd.toml') as ukc:
        results = await ukc.make_request(models=ClientCreateOne(name=f'test_client_api',
                                                                checkIp=False,
                                                                allowNat=False,
                                                                expiration=333333,
                                                                activationCodeValidity=333333,
                                                                isTemplate=False,
                                                                activationCodeLength=33,
                                                                ipRange='0.0.0.0/0',
                                                                certificateExpiration=333333))

        assert type(results) is Results
        assert results.success is not None
        assert not results.failure

        tprint(results)

    bprint(f'Completed in {(time.perf_counter() - ts):f} seconds.', 'bottom')


@pytest.mark.asyncio
async def test_client_create_one_verify_validation():
    ts = time.perf_counter()
    bprint('Test: Client Create One -> Verify Validation', 'top')

    # todo: add positive test before negative
    async with UkcClient(cfg=f'{getenv("CFG_HOME")}/unbound_snd.toml') as ukc:
        try:
            await ukc.make_request(models=ClientCreateOne(name=f'test_client_api',
                                                          checkIp=False,
                                                          allowNat=False,
                                                          expiration=3333333333,
                                                          activationCodeValidity=333333,
                                                          isTemplate=False,
                                                          activationCodeLength=33,
                                                          ipRange='0.0.0.0/0',
                                                          certificateExpiration=333333))
        except ValidationError as ve:
            bprint(str(ve))
            # The expected success criteria for this test is for this error to be raised.

    bprint(f'Completed in {(time.perf_counter() - ts):f} seconds.', 'bottom')


@pytest.mark.asyncio
async def test_client_refresh_activation_code():
    ts = time.perf_counter()
    bprint('Test: Client Refresh Activation Code', 'top')

    async with UkcClient(cfg=f'{getenv("CFG_HOME")}/unbound_snd.toml') as ukc:
        m = ClientRefreshActivationCode(
                clientId='test_client_api',
                body=RefreshedCertificateClient(
                        certificateExpiration=3333,
                        activationCodeValidity=3333,
                        activationCodeLength=15,
                        ipRange='0.0.0.0/8'))

        print(m)
        print(m.parameters)
        print(m.json_body)

        results = await ukc.make_request(models=m)

        assert type(results) is Results
        assert results.success is not None
        assert not results.failure

        tprint(results)

    bprint(f'Completed in {(time.perf_counter() - ts):f} seconds.', 'bottom')
