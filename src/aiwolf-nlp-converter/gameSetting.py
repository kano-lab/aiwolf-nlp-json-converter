from aiwolf_nlp_common.protocol import CommunicationProtocol

class gameSettingConverter:
    @classmethod
    def get_game_setting_dict(cls, protocol: CommunicationProtocol) -> dict:
        game_setting:dict = dict()

        game_setting["enableNoAttack"] = protocol.setting.is_enable_no_attack
        game_setting["enableNoExecution"] = protocol.setting.is_enable_no_attack
        game_setting["enableNoAttack"] = protocol.setting.is_enable_no_attack