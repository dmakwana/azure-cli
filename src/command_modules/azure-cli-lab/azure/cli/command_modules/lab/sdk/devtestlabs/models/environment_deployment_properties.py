# coding=utf-8
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# coding: utf-8
# pylint: skip-file
from msrest.serialization import Model


class EnvironmentDeploymentProperties(Model):
    """Properties of an environment deployment.

    :param arm_template_id: The Azure Resource Manager template's identifier.
    :type arm_template_id: str
    :param parameters: The parameters of the Azure Resource Manager template.
    :type parameters: list of :class:`ArmTemplateParameterProperties
     <azure.mgmt.devtestlabs.models.ArmTemplateParameterProperties>`
    """

    _attribute_map = {
        'arm_template_id': {'key': 'armTemplateId', 'type': 'str'},
        'parameters': {'key': 'parameters', 'type': '[ArmTemplateParameterProperties]'},
    }

    def __init__(self, arm_template_id=None, parameters=None):
        self.arm_template_id = arm_template_id
        self.parameters = parameters
