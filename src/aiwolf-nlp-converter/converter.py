from aiwolf_nlp_common.protocol import CommunicationProtocol
from aiwolf_nlp_common.protocol.info.list import VoteInfo, VoteList, AttackVoteList
from aiwolf_nlp_common.protocol.info.result import DivineResult, MediumResult


class Converter:
    @classmethod
    def get_json_dict(received_str: str) -> dict:
        protocol: CommunicationProtocol = CommunicationProtocol.initialize_from_json(
            received_str=received_str
        )

        before_json_dict = dict()
        before_json_dict["request"] = protocol.request
        before_json_dict["gameInfo"]

    def get_game_info_dict(self, protocol: CommunicationProtocol) -> dict:
        game_info: dict = dict()

        if protocol.is_info_empty():
            return None

        game_info["agent"] = protocol.info.agent
        game_info["attackVoteList"] = self.get_vote_list_info(
            vote_list=protocol.info.attack_vote_list
        )
        game_info["attackedAgent"] = protocol.info.attacked_agent
        game_info["day"] = protocol.info.day
        game_info["divineResult"] = self.get_judgement_result(
            judgement_result=protocol.info.divine_result
        )
        game_info["executedAgent"] = protocol.info.executed_agent

    def get_vote_list_info(self, vote_list: VoteList | AttackVoteList) -> list[dict]:
        result: list = list()

        attack_vote_element: VoteInfo
        for attack_vote_element in vote_list:
            current_vote_info: dict = dict()
            current_vote_info["agent"] = attack_vote_element.agent
            current_vote_info["day"] = attack_vote_element.day
            current_vote_info["target"] = attack_vote_element.target
            result.append(current_vote_info)

        return result

    def get_judgement_result(
        self, judgement_result: DivineResult | MediumResult
    ) -> dict | None:
        result: dict = dict()

        if judgement_result.is_empty():
            return None

        result["agent"] = judgement_result.agent
        result["day"] = judgement_result.day
        result["result"] = judgement_result.result
        result["target"] = judgement_result.target

        return result
