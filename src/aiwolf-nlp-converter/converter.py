from aiwolf_nlp_common.protocol import CommunicationProtocol
from gameInfo import gameInfoConverter
from gameSetting import gameSettingConverter


class Converter:
    @classmethod
    def get_json_dict(received_str: str) -> dict:
        protocol: CommunicationProtocol = CommunicationProtocol.initialize_from_json(
            received_str=received_str
        )

        before_json_dict = dict()
        before_json_dict["request"] = protocol.request
        before_json_dict["gameInfo"] = gameInfoConverter.get_game_info_dict(
            protocol=protocol
        )
        before_json_dict["gameSetting"] = gameSettingConverter.get_game_setting_dict(
            protocol=protocol
        )
