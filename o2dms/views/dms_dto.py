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

from flask_restx import Namespace, fields


class DmsDTO:

    api = Namespace("O2DMS",
                    description='DMS related operations.')

    dms_get = api.model(
        "Get DMS information",
        {
            'deploymentManagerId': fields.String(
                required=True,
                description='Deployment manager ID'),
            'name': fields.String,
            'description': fields.String,
            'supportedLocations': fields.String,
            'capabilities': fields.String,
            'capacity': fields.String,
        }
    )


class DmsLcmNfDeploymentDescriptorDTO:

    api = Namespace("O2DMS_LCM_NfDeploymentDescriptor",
                    description='DMS LCM NfDeploymentDescritpor operations.')

    dmslcm_NfDeploymentDescriptor_get = api.model(
        "Get NfDeploymentDescriptor information",
        {
            'id': fields.String(
                required=True,
                description='NfDeploymentDescriptor ID'),
            'name': fields.String,
            'description': fields.String,
            'inputParams': fields.String,
            'outputParams': fields.String
        }
    )