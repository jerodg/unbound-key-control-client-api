#!/usr/bin/env python3.9
"""Unbound KeyControl Client API -> Models -> Partition
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
from dataclasses import field

TYPES = ['RSA', 'ECC', 'AES', 'TDES', 'DES', 'HMAC', 'SIV', 'XTS', 'PRF', 'PWD',
         'LIMA', 'EDDSA', 'TOTSSeed']
EXPORT_TYPES = ['IN_PLAIN', 'WRAPPED', 'WRAPPED_WITH_TRUSTED', 'NON_EXPORTABLE']

#
# @dataclass
# class PartitionPolicyRule(Record):
#     type: str = field
#     minSize: Optional[int] = None
#     curves: List[str] = None
#     operations: List[str] = None
#     paddings: List[str] = None
#     hashes: List[str] = None
#     modes: List[str] = None
#     macs: List[str] = None
#     exportType: Optional[str] = None
#     trusted: Optional[bool] = None
#     local: Optional[bool] = None
#
#     def __post_init__(self):
#         self.type = self.type.upper()
#         if self.type not in TYPES:
#             raise InvalidOptionError(var=self.type, options=TYPES)
#
#         if self.exportType:
#             self.exportType = self.exportType.upper()
#
#             if self.exportType not in EXPORT_TYPES:
#                 raise InvalidOptionError(var=self.exportType, options=EXPORT_TYPES)
#
#
# @dataclass
# class Partition(Record):
#     checkClientIp: Optional[bool] = None
#     name: Optional[str] = None
#     allowNat: Optional[bool] = None
#     allowUserOnlyCryptoOperations: Optional[bool] = None
#     clientRetriesLimit: Optional[int] = None
#     clientRetriesTimeout: Optional[int] = None
#     creationDate: Optional[str] = None
#     getjWTLimit: Optional[int] = None
#     lastUpdate: Optional[str] = None
#     passwordComplexity: Optional[bool] = None
#     passwordLength: Optional[int] = None
#     quorumOperations: Optional[str] = None
#     quorumSize: Optional[int] = None
#     quorumTimeout: Optional[int] = None
#     supportCertificatePropagation: Optional[bool] = None
#     supportPartitionInheritance: Optional[bool] = None
#     userRetriesLimit: Optional[int] = None
#     fipsRequirements: Optional[str] = None
#     policy: Optional[PartitionPolicyRule] = None
#     allowKeystores: Optional[bool] = None
#     jWTExpiration: Optional[int] = None
