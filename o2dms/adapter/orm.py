# Copyright (C) 2021 Wind River Systems, Inc.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

from sqlalchemy import (
    Table,
    MetaData,
    Column,
    Integer,
    String,
    # Date,
    DateTime,
    # ForeignKey,
    # engine,
    # event,
)

from sqlalchemy.orm import mapper
from o2dms.domain import dms as dmsModel

from o2common.helper import o2logging
logger = o2logging.get_logger(__name__)

metadata = MetaData()

nfDeploymentDesc = Table(
    "nfDeploymentDesc",
    metadata,
    Column("updatetime", DateTime),
    Column("createtime", DateTime),
    Column("hash", String(255)),
    Column("version_number", Integer),

    Column("id", String(255), primary_key=True),
    Column("deploymentManagerId", String(255)),
    Column("name", String(255)),
    Column("description", String(255)),
    Column("supportedLocations", String(255)),
    Column("capabilities", String(255)),
    Column("capacity", String(255)),
    # Column("extensions", String(1024))
)


def start_o2dms_mappers(engine=None):
    logger.info("Starting O2 DMS mappers")

    mapper(dmsModel.NfDeploymentDesc, nfDeploymentDesc)

    if engine is not None:
        metadata.create_all(engine)