#!/usr/bin/env python3.9
"""Unbound KeyControl Client API -> Models -> Roles
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
from dataclasses import dataclass, field
from typing import List, Optional, Union

from base_client_api.models import Record


@dataclass
class RolePermission(Record):
    objectGroup: Optional[str] = None
    operations: Optional[List[str]] = None


@dataclass
class Role(Record):
    name: Optional[str] = None
    partition: Optional[str] = None
    createdAt: Optional[str] = None
    updatedAt: Optional[str] = None
    managedObjectPermissions: Optional[List[RolePermission]] = None


@dataclass
class RoleListResponse(Record):
    totalItems: Optional[int] = None  # Only returned when ListAllRoles.limit is used
    limit: Optional[int] = None  # Only returned when ListAllRoles.limit is used
    skip: Optional[int] = None  # Only returned when ListAllRoles.skip is used
    items: Optional[List[Role]] = None  # Only returned when any above are used

    @property
    def data_key(self) -> Union[str, None]:
        """Data Key

        This is the key used in the return dict that holds the primary data

        Returns:
            (Union[str, None])"""
        if self.limit or self.skip:
            return 'items'
        else:
            return None


@dataclass
class ListAllRoles(Record):
    """GET /api/v1/roles
       - Return a list of all roles in a partition."""
    partitionId: str = None
    limit: int = None
    skip: int = None
    detailed: bool = None

    @property
    def endpoint(self) -> str:
        """Endpoint

        The suffix end of the URI

        Returns:
            (str)"""
        return '/roles'

    @property
    def data_key(self) -> Union[str, None]:
        """Data Key

        This is the key used in the return dict that holds the primary data

        Returns:
            (Union[str, None])"""
        if self.limit or self.skip:
            return 'items'
        else:
            return None

    @property
    def method(self) -> str:
        """Method

        The HTTP verb to be used

        Returns:
            (str)"""
        return 'GET'

    @property
    def params(self) -> Union[dict, None]:
        """URL Parameters

        If you need to pass parameters in the URL

        Returns:
            (Union[dict, None])"""
        return self.dict(cleanup=...)

    @property
    def headers(self) -> Union[dict, None]:
        """URL Parameters

        If you need to pass parameters in the URL

        Returns:
            (Union[dict, None])"""
        return {'Accept': 'application/json'}


@dataclass
class ListOneRole(ListAllRoles):

    def dict(self, cleanup: Optional[bool] = True, dct: Optional[dict] = None, sort_order: Optional[str] = 'asc') -> dict:
        """
        Args:
            cleanup (Optional[bool]):
            dct (Optional[dict]):
            sort_order (Optional[str]): ASC | DESC

        Returns:
            dict (dict):"""
        dct = super().dict()
        del dct['limit']
        del dct['skip']

        return dct


@dataclass
class NewRole(Role):
    role: Role = field(default_factory=Role)
    partitionId: str = None

    def dict(self, cleanup: Optional[bool] = True, dct: Optional[dict] = None, sort_order: Optional[str] = 'asc') -> dict:
        """
        Args:
            cleanup (Optional[bool]):
            dct (Optional[dict]):
            sort_order (Optional[str]): ASC | DESC

        Returns:
            dict (dict):"""
        dct = super().dict()
        if dct['partition']:
            dct['partitionId'] = dct['partition']
            del dct['partition']

        return dct

    @property
    def endpoint(self) -> str:
        """Endpoint

        The suffix end of the URI

        Returns:
            (str)"""
        return '/roles/'

    @property
    def method(self) -> str:
        """Method

        The HTTP verb to be used

        Returns:
            (str)"""
        return 'POST'


@dataclass
class UpdatedRole(NewRole):
    """Update a role."""

    def dict(self, cleanup: Optional[bool] = True, dct: Optional[dict] = None, sort_order: Optional[str] = 'asc') -> dict:
        """
        Args:
            cleanup (Optional[bool]):
            dct (Optional[dict]):
            sort_order (Optional[str]): ASC | DESC

        Returns:
            dict (dict):"""
        dct = super().dict()
        if dct['partition']:
            dct['partitionId'] = dct['partition']
            del dct['partition']

        del dct['name']
        del dct['createdAt']
        del dct['updateAt']

        return dct

    @property
    def endpoint(self) -> str:
        """Endpoint

        The suffix end of the URI

        Returns:
            (str)"""
        return f'/roles/{self.role.name}'

    @property
    def method(self) -> str:
        """Method

        The HTTP verb to be used

        Returns:
            (str)"""
        return 'PUT'
