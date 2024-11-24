from aiwolf_nlp_common.protocol import CommunicationProtocol
from aiwolf_nlp_json_converter.gameInfo import gameInfoConverter

def test_get_game_info_dict(initialize_str, initialize_json) -> None:
    protocol = CommunicationProtocol.initialize_from_json(received_str=initialize_str)
    test_result = gameInfoConverter.get_game_info_dict(protocol=protocol)

    assert type(test_result) is not None
    assert type(test_result) is dict
    assert test_result["day"] == initialize_json["info"]["day"]