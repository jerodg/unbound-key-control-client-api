#!/usr/bin/env python3.9
"""Unbound KeyControl Client API -> Tests -> Roles
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
from pydantic import ValidationError
from rich import print

from unbound_key_control_client_api.models.roles import (NewRole, RoleCreateOne, RoleGetOne, RolePermission, RolesListAll,
                                                         RoleUpdateOne, UpdatedRole)
from unbound_key_control_client_api.ukc_client import UkcClient

logger.enable('base_client_api')


# todo: add automatic delete after successful creation
# todo: add utility that searches for all test objects and deletes them


@pytest.mark.asyncio
async def test_roles_list_all():
    ts = perf_counter()
    bprint('Test: Roles List All', 'top')

    async with UkcClient(cfg=f'{getenv("CFG_HOME")}/unbound_snd.toml') as ukc:
        m = RolesListAll(partitionId='sandbox',
                         limit=25,
                         skip=3)
        print(m)
        print(m.parameters)
        results = await ukc.make_request(models=m)

        assert type(results) is Results
        assert results.success is not None
        assert not results.failure

        tprint(results, top=5)

    bprint(f'Completed in {(perf_counter() - ts):f} seconds.', 'bottom')


@pytest.mark.asyncio
async def test_role_get_one():
    ts = perf_counter()
    bprint('Test: Role Get One', 'top')

    async with UkcClient(cfg=f'{getenv("CFG_HOME")}/unbound_snd.toml') as ukc:
        m = RoleGetOne(roleId='client-tests', partitionId='sandbox')
        print(m)
        print(m.parameters)
        results = await ukc.make_request(models=m)

        assert type(results) is Results
        assert results.success is not None
        assert not results.failure

        tprint(results, top=5)

    bprint(f'Completed in {(perf_counter() - ts):f} seconds.', 'bottom')


@pytest.mark.asyncio
async def test_role_create_one():
    ts = perf_counter()
    bprint('Test: Role Create One', 'top')

    async with UkcClient(cfg=f'{getenv("CFG_HOME")}/unbound_snd.toml') as ukc:
        m = RoleCreateOne(partitionId='sandbox',
                          body=NewRole(name='test-client-api-role',
                                       managedObjectsPermissions=[RolePermission(objectGroup='test-client-api',
                                                                                 operations=['ACTIVATE'])]))
        # todo: change this to a template
        print(m)
        print(m.parameters)
        print(m.json_body)
        results = await ukc.make_request(models=m)

        assert type(results) is Results
        assert results.success is not None
        assert not results.failure

        tprint(results, top=5)

    bprint(f'Completed in {(perf_counter() - ts):f} seconds.', 'bottom')


@pytest.mark.asyncio
async def test_role_create_one_verify_validation():
    ts = perf_counter()
    bprint('Test: Role Create One -> Verify Validation', 'top')

    async with UkcClient(cfg=f'{getenv("CFG_HOME")}/unbound_snd.toml') as ukc:
        try:
            m = RoleCreateOne(partitionId='sandbox',
                              body=NewRole(name='test-client-api',
                                           managedObjectsPermissions=[RolePermission(objectGroup='test-client-api',
                                                                                     operations=['ACTIVATE'])]))
            print('Success:\n', m)

            m = RoleCreateOne(partitionId='sandbox',
                              body=NewRole(name='test-client-api',
                                           managedObjectsPermissions=[RolePermission(objectGroup='test-client-api',
                                                                                     operations=['MC-TEST'])]))
        except ValidationError as ve:
            bprint(str(ve))
            # The expected success criteria for this test is for this error to be raised.

    bprint(f'Completed in {(perf_counter() - ts):f} seconds.', 'bottom')


@pytest.mark.asyncio
async def test_role_update_one():
    ts = perf_counter()
    bprint('Test: Role Update One', 'top')

    async with UkcClient(cfg=f'{getenv("CFG_HOME")}/unbound_snd.toml') as ukc:
        m = RoleUpdateOne(roleId='test-client-api',
                          partitionId='sandbox',
                          body=UpdatedRole(managedObjectsPermissions=[RolePermission(objectGroup='test-client-api',
                                                                                     operations=['ACTIVATE', 'SIGN', 'DELETE'])]))
        # todo: change this to a template
        print(m)
        print(m.parameters)
        print(m.json_body)
        results = await ukc.make_request(models=m)

        assert type(results) is Results
        assert results.success is not None
        assert not results.failure

        tprint(results, top=5)

    bprint(f'Completed in {(perf_counter() - ts):f} seconds.', 'bottom')
