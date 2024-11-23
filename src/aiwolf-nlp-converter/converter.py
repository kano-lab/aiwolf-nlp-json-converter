from aiwolf_nlp_common.protocol import CommunicationProtocol


class Converter:
    @classmethod
    def get_json_dict(received_str: str) -> dict:
        protocol: CommunicationProtocol = CommunicationProtocol.initialize_from_json(
            received_str=received_str
        )

        before_json_dict = dict()
        before_json_dict["request"] = protocol.request
        before_json_dict["gameInfo"]
