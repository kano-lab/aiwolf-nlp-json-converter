from aiwolf_nlp_common.protocol import CommunicationProtocol
from aiwolf_nlp_common.protocol.info.list import VoteInfo, VoteList, AttackVoteList
from aiwolf_nlp_common.protocol.info.result import DivineResult, MediumResult
from aiwolf_nlp_common.protocol.info.map import AgentRole, RoleMap


class gameInfoConverter:
    @classmethod
    def get_game_info_dict(cls, protocol: CommunicationProtocol) -> dict:
        game_info: dict = dict()

        if protocol.is_info_empty():
            return None

        game_info["agent"] = protocol.info.agent
        game_info["attackVoteList"] = cls.get_vote_list_info(
            vote_list=protocol.info.attack_vote_list
        )
        game_info["attackedAgent"] = protocol.info.attacked_agent
        game_info["day"] = protocol.info.day
        game_info["divineResult"] = cls.get_judgement_result(
            judgement_result=protocol.info.divine_result
        )
        game_info["executedAgent"] = protocol.info.executed_agent
        game_info["lastDeadAgentList"] = cls.get_lastDeadAgentList(
            attacked_agent=protocol.info.attacked_agent
        )
        game_info["roleMap"] = protocol.info.executed_agent

    def get_vote_list_info(vote_list: VoteList | AttackVoteList) -> list[dict]:
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
        judgement_result: DivineResult | MediumResult,
    ) -> dict | None:
        result: dict = dict()

        if judgement_result.is_empty():
            return None

        result["agent"] = judgement_result.agent
        result["day"] = judgement_result.day
        result["result"] = judgement_result.result
        result["target"] = judgement_result.target

        return result

    def get_lastDeadAgentList(attacked_agent: str | None) -> list:
        result: list = []

        if attacked_agent is not None:
            result.append(attacked_agent)

        return result

    def get_role_map(role_map: RoleMap) -> dict:
        result: dict = dict()

        role_map_element: AgentRole
        for role_map_element in role_map:
            result[role_map_element.agent] = role_map_element.role

        return result
