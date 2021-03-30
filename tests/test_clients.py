#!/usr/bin/env python3.8
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
from devtools import debug
from pydantic import ValidationError

from unbound_key_control_client_api.models.clients import (ClientCreateOne, ClientGetDetails, ClientRefreshActivationCode,
                                                           ClientsListAll, RefreshedCertificateClient)
from unbound_key_control_client_api.ukc_client import UkcClient


# logger.enable('base_client_api')  # debug


@pytest.mark.asyncio
async def test_clients_list_all():
    ts = time.perf_counter()
    bprint('Test: Clients List All', 'top')

    async with UkcClient(cfg=f'{getenv("CFG_HOME")}/unbound_snd.toml') as ukc:
        model = ClientsListAll(limit=25, skip=3, partition_id='sandbox')

        debug(model)
        debug(model.parameters)
        debug(model.json())
        debug(model.dict())

        results = await ukc.make_request(models=model)

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
        model = ClientCreateOne(name=f'test_client_api',
                                check_ip=False,
                                allow_nat=False,
                                expiration=333333,
                                activation_code_validity=333333,
                                is_template=False,
                                activation_code_length=33,
                                ip_range='0.0.0.0/0',
                                certificate_expiration=333333)
        debug(model)
        debug(model.parameters)
        debug(model.json())
        debug(model.dict())

        results = await ukc.make_request(models=model)

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
            model = ClientCreateOne(name=f'test_client_api',
                                    check_ip=False,
                                    allow_nat=False,
                                    expiration=3333333333,
                                    activation_code_validity=333333,
                                    is_template=False,
                                    activation_code_length=33,
                                    ip_range='0.0.0.0/0',
                                    certificate_expiration=333333)

        except ValidationError as ve:
            bprint(str(ve))  # The expected success criteria for this test is for this error to be raised.

    bprint(f'Completed in {(time.perf_counter() - ts):f} seconds.', 'bottom')


@pytest.mark.asyncio
async def test_client_refresh_activation_code():
    ts = time.perf_counter()
    bprint('Test: Client Refresh Activation Code', 'top')

    async with UkcClient(cfg=f'{getenv("CFG_HOME")}/unbound_snd.toml') as ukc:
        model = ClientRefreshActivationCode(
                client_id='test_client_api',
                body=RefreshedCertificateClient(
                        certificate_expiration=3333,
                        activation_code_validity=3333,
                        activation_code_length=15,
                        ip_range='0.0.0.0/8'))

        debug(model)
        debug(model.endpoint)
        debug(model.parameters)
        debug(model.json())
        debug(model.dict())

        results = await ukc.make_request(models=model)

        assert type(results) is Results
        assert results.success is not None
        assert not results.failure

        tprint(results)

    bprint(f'Completed in {(time.perf_counter() - ts):f} seconds.', 'bottom')


@pytest.mark.asyncio
async def test_client_get_details():
    ts = time.perf_counter()
    bprint('Test: Client Get Details', 'top')

    async with UkcClient(cfg=f'{getenv("CFG_HOME")}/unbound_snd.toml') as ukc:
        model = ClientGetDetails(client_id='je1234-eclient')

        debug(model)
        debug(model.parameters)
        debug(model.json())
        debug(model.dict())

        results = await ukc.make_request(models=model)

        assert type(results) is Results
        assert results.success is not None
        assert not results.failure

        tprint(results)

    bprint(f'Completed in {(time.perf_counter() - ts):f} seconds.', 'bottom')
