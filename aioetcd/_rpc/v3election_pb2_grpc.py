# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from . import v3election_pb2 as v3election__pb2


class ElectionStub(object):
    """The election service exposes client-side election facilities as a gRPC interface.
  """

    def __init__(self, channel):
        """Constructor.

    Args:
      channel: A grpc.Channel.
    """
        self.Campaign = channel.unary_unary(
            "/v3electionpb.Election/Campaign",
            request_serializer=v3election__pb2.CampaignRequest.SerializeToString,
            response_deserializer=v3election__pb2.CampaignResponse.FromString,
        )
        self.Proclaim = channel.unary_unary(
            "/v3electionpb.Election/Proclaim",
            request_serializer=v3election__pb2.ProclaimRequest.SerializeToString,
            response_deserializer=v3election__pb2.ProclaimResponse.FromString,
        )
        self.Leader = channel.unary_unary(
            "/v3electionpb.Election/Leader",
            request_serializer=v3election__pb2.LeaderRequest.SerializeToString,
            response_deserializer=v3election__pb2.LeaderResponse.FromString,
        )
        self.Observe = channel.unary_stream(
            "/v3electionpb.Election/Observe",
            request_serializer=v3election__pb2.LeaderRequest.SerializeToString,
            response_deserializer=v3election__pb2.LeaderResponse.FromString,
        )
        self.Resign = channel.unary_unary(
            "/v3electionpb.Election/Resign",
            request_serializer=v3election__pb2.ResignRequest.SerializeToString,
            response_deserializer=v3election__pb2.ResignResponse.FromString,
        )


class ElectionServicer(object):
    """The election service exposes client-side election facilities as a gRPC interface.
  """

    def Campaign(self, request, context):
        """Campaign waits to acquire leadership in an election, returning a LeaderKey
    representing the leadership if successful. The LeaderKey can then be used
    to issue new values on the election, transactionally guard API requests on
    leadership still being held, and resign from the election.
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def Proclaim(self, request, context):
        """Proclaim updates the leader's posted value with a new value.
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def Leader(self, request, context):
        """Leader returns the current election proclamation, if any.
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def Observe(self, request, context):
        """Observe streams election proclamations in-order as made by the election's
    elected leaders.
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def Resign(self, request, context):
        """Resign releases election leadership so other campaigners may acquire
    leadership on the election.
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_ElectionServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "Campaign": grpc.unary_unary_rpc_method_handler(
            servicer.Campaign,
            request_deserializer=v3election__pb2.CampaignRequest.FromString,
            response_serializer=v3election__pb2.CampaignResponse.SerializeToString,
        ),
        "Proclaim": grpc.unary_unary_rpc_method_handler(
            servicer.Proclaim,
            request_deserializer=v3election__pb2.ProclaimRequest.FromString,
            response_serializer=v3election__pb2.ProclaimResponse.SerializeToString,
        ),
        "Leader": grpc.unary_unary_rpc_method_handler(
            servicer.Leader,
            request_deserializer=v3election__pb2.LeaderRequest.FromString,
            response_serializer=v3election__pb2.LeaderResponse.SerializeToString,
        ),
        "Observe": grpc.unary_stream_rpc_method_handler(
            servicer.Observe,
            request_deserializer=v3election__pb2.LeaderRequest.FromString,
            response_serializer=v3election__pb2.LeaderResponse.SerializeToString,
        ),
        "Resign": grpc.unary_unary_rpc_method_handler(
            servicer.Resign,
            request_deserializer=v3election__pb2.ResignRequest.FromString,
            response_serializer=v3election__pb2.ResignResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "v3electionpb.Election", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))