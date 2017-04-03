# coding=utf-8
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# coding: utf-8
# pylint: skip-file
from msrest.serialization import Model


class ArtifactInstallProperties(Model):
    """Properties of an artifact.

    :param artifact_id: The artifact's identifier.
    :type artifact_id: str
    :param parameters: The parameters of the artifact.
    :type parameters: list of :class:`ArtifactParameterProperties
     <azure.mgmt.devtestlabs.models.ArtifactParameterProperties>`
    :param status: The status of the artifact.
    :type status: str
    :param deployment_status_message: The status message from the deployment.
    :type deployment_status_message: str
    :param vm_extension_status_message: The status message from the virtual
     machine extension.
    :type vm_extension_status_message: str
    :param install_time: The time that the artifact starts to install on the
     virtual machine.
    :type install_time: datetime
    """

    _attribute_map = {
        'artifact_id': {'key': 'artifactId', 'type': 'str'},
        'parameters': {'key': 'parameters', 'type': '[ArtifactParameterProperties]'},
        'status': {'key': 'status', 'type': 'str'},
        'deployment_status_message': {'key': 'deploymentStatusMessage', 'type': 'str'},
        'vm_extension_status_message': {'key': 'vmExtensionStatusMessage', 'type': 'str'},
        'install_time': {'key': 'installTime', 'type': 'iso-8601'},
    }

    def __init__(self, artifact_id=None, parameters=None, status=None, deployment_status_message=None, vm_extension_status_message=None, install_time=None):
        self.artifact_id = artifact_id
        self.parameters = parameters
        self.status = status
        self.deployment_status_message = deployment_status_message
        self.vm_extension_status_message = vm_extension_status_message
        self.install_time = install_time
