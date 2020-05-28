# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .control_activity import ControlActivity


class ForEachActivity(ControlActivity):
    """This activity is used for iterating over a collection and execute given
    activities.

    All required parameters must be populated in order to send to Azure.

    :param additional_properties: Unmatched properties from the message are
     deserialized this collection
    :type additional_properties: dict[str, object]
    :param name: Required. Activity name.
    :type name: str
    :param description: Activity description.
    :type description: str
    :param depends_on: Activity depends on condition.
    :type depends_on: list[~azure.mgmt.datafactory.models.ActivityDependency]
    :param user_properties: Activity user properties.
    :type user_properties: list[~azure.mgmt.datafactory.models.UserProperty]
    :param type: Required. Constant filled by server.
    :type type: str
    :param is_sequential: Should the loop be executed in sequence or in
     parallel (max 50)
    :type is_sequential: bool
    :param batch_count: Batch count to be used for controlling the number of
     parallel execution (when isSequential is set to false).
    :type batch_count: int
    :param items: Required. Collection to iterate.
    :type items: ~azure.mgmt.datafactory.models.Expression
    :param activities: Required. List of activities to execute .
    :type activities: list[~azure.mgmt.datafactory.models.Activity]
    """

    _validation = {
        'name': {'required': True},
        'type': {'required': True},
        'batch_count': {'maximum': 50},
        'items': {'required': True},
        'activities': {'required': True},
    }

    _attribute_map = {
        'additional_properties': {'key': '', 'type': '{object}'},
        'name': {'key': 'name', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'depends_on': {'key': 'dependsOn', 'type': '[ActivityDependency]'},
        'user_properties': {'key': 'userProperties', 'type': '[UserProperty]'},
        'type': {'key': 'type', 'type': 'str'},
        'is_sequential': {'key': 'typeProperties.isSequential', 'type': 'bool'},
        'batch_count': {'key': 'typeProperties.batchCount', 'type': 'int'},
        'items': {'key': 'typeProperties.items', 'type': 'Expression'},
        'activities': {'key': 'typeProperties.activities', 'type': '[Activity]'},
    }

    def __init__(self, **kwargs):
        super(ForEachActivity, self).__init__(**kwargs)
        self.is_sequential = kwargs.get('is_sequential', None)
        self.batch_count = kwargs.get('batch_count', None)
        self.items = kwargs.get('items', None)
        self.activities = kwargs.get('activities', None)
        self.type = 'ForEach'