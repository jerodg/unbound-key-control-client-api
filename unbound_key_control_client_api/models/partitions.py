#!/usr/bin/env python3.9
"""Unbound KeyControl Client API -> Models -> Partitions
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
from typing import Optional

from base_client_api.models.record import Record


class PartitionsListAll(Record):
    """Partitions List All

    GET /api/v1/partitions

    Return a list of all partitions"""
    limit: Optional[int] = None
    skip: Optional[int] = None

    @property
    def endpoint(self) -> str:
        """Endpoint

        The suffix end of the URI

        Returns:
            (str)"""
        return '/partitions'

    @property
    def method(self) -> Optional[str]:
        """Method

        The HTTP verb to be used
         - Must be a valid HTTP verb as listed above in METHODS

        Returns:
            (str)"""
        return 'GET'


if __name__ == '__main__':
    print(__doc__)
