from .internal.peers import private_peer, group_peer, peer_hasher
from dialog_api import peers_pb2, messaging_pb2, miscellaneous_pb2, contacts_pb2

DEFAULT_OPTIMIZATIONS = [
    miscellaneous_pb2.UPDATEOPTIMIZATION_STRIP_ENTITIES,
    miscellaneous_pb2.UPDATEOPTIMIZATION_STRIP_ENTITIES_V2,
    miscellaneous_pb2.UPDATEOPTIMIZATION_STRIP_COUNTERS,
    miscellaneous_pb2.UPDATEOPTIMIZATION_COMPACT_USERS
]


class EntityManager(object):
    """Entity manager class.

    """
    def __init__(self, internal):
        self.internal = internal
        self.peers_to_outpeers = {}
        self.bootstrap()

    def bootstrap(self):
        """Finds outpeers for all list of contacts.

        """
        contacts = self.internal.contacts.GetContacts(contacts_pb2.RequestGetContacts(
            optimizations=DEFAULT_OPTIMIZATIONS
        ))
        for user in contacts.user_peers:
            self.adopt_peer(user)

    def adopt_peer(self, peer):
        """Finds outpeer for given peer and store it in internal peers_to_outpeers dict.

        :param peer: Peer object
        """
        if isinstance(peer, peers_pb2.UserOutPeer):
            outpeer = peers_pb2.OutPeer(type=peers_pb2.PEERTYPE_PRIVATE, id=peer.uid, access_hash=peer.access_hash)
            self.peers_to_outpeers[peer_hasher(private_peer(peer.uid))] = outpeer
        elif isinstance(peer, peers_pb2.GroupOutPeer):
            outpeer = peers_pb2.OutPeer(type=peers_pb2.PEERTYPE_GROUP, id=peer.group_id, access_hash=peer.access_hash)
            self.peers_to_outpeers[peer_hasher(group_peer(peer.group_id))] = outpeer
        else:
            raise RuntimeError("Unknown peer type")

    def get_outpeer(self, peer):
        """Returns outpeer for given peer.

        :param peer: Peer object
        :return: OutPeer object
        """
        if isinstance(peer, peers_pb2.OutPeer):
            return peer

        peer_hash = peer_hasher(peer)
        result = self.peers_to_outpeers.get(peer_hash)
        if result is None:
            req = messaging_pb2.RequestLoadDialogs(
                min_date=0,
                limit=1,
                peers_to_load=[peer],
                optimizations=DEFAULT_OPTIMIZATIONS
            )
            result = self.internal.messaging.LoadDialogs(req)
            for user in result.user_peers:
                self.adopt_peer(user)
            for group in result.group_peers:
                self.adopt_peer(group)
            return self.peers_to_outpeers.get(peer_hash)
        return result
