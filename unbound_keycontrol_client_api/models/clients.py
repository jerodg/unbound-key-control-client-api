#!/usr/bin/env python3.9
"""Unbound KeyControl Client API -> Models -> Clients
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
from typing import Union

from base_client_api.models import Record
from pydantic import validator
from pydantic.dataclasses import dataclass


@dataclass
class NewClient(Record):
    """POST /api/v1/clients
       - Creates a new client and returns the activation code."""
    name: str
    partitionId: str = None
    checkIp: bool = None
    allowNat: bool = None
    expiration: int = None  # minutes
    activationCodeValidity: int = None  # minutes
    isTemplate: bool = None
    activationCodeLength: int = None  # digits
    ipRange: str = None  # CIDR 0.0.0.0/0
    certificateExpiration: int = None  # minutes

    @validator('expiration', 'activationCodeValidity', 'activationCodeLength', 'certificateExpiration')
    def check_int_length(self, value) -> int:
        """Check Integer Length

        Ensures the integer provided does not exceed the 32bit limit (2,147,483,647) as set by the API

        Args:
            value (int):

        Returns:
            value (int):"""
        if value > 2147483647:
            raise ValueError('This field must be <= 2,147,483,647')

        return value

    @property
    def endpoint(self) -> str:
        """Endpoint

        The suffix end of the URI

        Returns:
            (str)"""
        return '/clients'

    @property
    def method(self) -> str:
        """Method

        The HTTP verb to be used

        Returns:
            (str)"""
        return 'POST'

    @property
    def params(self) -> Union[dict, None]:
        """URL Parameters

        If you need to pass parameters in the URL

        Returns:
            (Union[dict, None])"""
        if self.partitionId:
            return {'partitionId': self.partitionId}

        return None

    @property
    def headers(self) -> Union[dict, None]:
        """Headers

        If you need to pass non-default headers

        Returns:
            (Union[dict, None])"""
        return {'Accept': 'application/json', 'Content-Type': 'application/json'}


@dataclass
class ListAllClients(Record):
    """GET /api/v1/clients
       - Return a list of all clients."""

    partitionId: str = None
    limit: int = None
    skip: int = None
    detailed: bool = True
    template: str = None
