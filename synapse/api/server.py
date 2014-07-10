# -*- coding: utf-8 -*-

from synapse.api.events import EventFactory
from synapse.federation import ReplicationHandler


class SynapseHomeServer(ReplicationHandler):

    def __init__(self, http_server, server_name, replication_layer):
        self.server_name = server_name
        self.http_server = http_server
        self.replication_layer = replication_layer
        self.replication_layer.set_callback(self)

        self.event_factory = EventFactory()
        self.event_factory.register_paths(self.http_server)

    def on_receive_pdu(self, pdu):
        pdu_type = pdu.pdu_type
        print "#%s (receive) *** %s" % (pdu.context, pdu_type)

    def on_state_change(self, pdu):
        print "#%s (state) %s *** %s" % (pdu.context, pdu.state_key,
                                        pdu.pdu_type)


