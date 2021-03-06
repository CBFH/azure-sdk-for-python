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

from msrest.serialization import Model


class ConnectionUpdateParameters(Model):
    """The parameters supplied to the update connection operation.

    :param name: Gets or sets the name of the connection.
    :type name: str
    :param description: Gets or sets the description of the connection.
    :type description: str
    :param field_definition_values: Gets or sets the field definition values
     of the connection.
    :type field_definition_values: dict[str, str]
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'description': {'key': 'properties.description', 'type': 'str'},
        'field_definition_values': {'key': 'properties.fieldDefinitionValues', 'type': '{str}'},
    }

    def __init__(self, *, name: str=None, description: str=None, field_definition_values=None, **kwargs) -> None:
        super(ConnectionUpdateParameters, self).__init__(**kwargs)
        self.name = name
        self.description = description
        self.field_definition_values = field_definition_values
