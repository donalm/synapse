# -*- coding: utf-8 -*-
""" This package includes all the federation specific logic.
"""

from .replication import ReplicationLayer, ReplicationHandler
from .transport import TransportLayer


def initialize_http_federation(server_name, http_client, http_server):
    transport = TransportLayer(server_name, http_client, http_server)
    return ReplicationLayer(server_name, transport)