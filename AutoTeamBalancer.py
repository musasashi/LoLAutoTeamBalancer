# IMPORT
import itertools
import json
from enum import Enum
import sys


def load_setting_by_json(setting_dir):
    with open(setting_dir + "/OptimizationParams.json", "r") as f:
        jf = json.load(f)
        lane_weight = jf["lane_weight"]
        rank_score = jf["rank_score"]

    with open(setting_dir + "/PlayerStats.json", "r") as f:
        jf = json.load(f)
        player_stats = jf["player_stats"]

    return (lane_weight, rank_score, player_stats)


class Lanes(Enum):
    top = 0
    jug = 1
    mid = 2
    adc = 3
    sup = 4


class Player:
    def __init__(self, name, player_stats, rank_score):
        self.name = name

        try:
            player_stat = player_stats[name]
        except KeyError as e:
            print(f"Player.jsonに記載された'{name}'が見つかりませんでした。")
            print("Player.jsonで定義された名称から選択してください。")
            sys.exit()
        self.rank = [
            player_stat["top"],
            player_stat["jug"],
            player_stat["mid"],
            player_stat["adc"],
            player_stat["sup"],
        ]
        self.score = [
            rank_score[player_stat["top"]],
            rank_score[player_stat["jug"]],
            rank_score[player_stat["mid"]],
            rank_score[player_stat["adc"]],
            rank_score[player_stat["sup"]],
        ]

    def rank_to_score(rank, rank_score):
        return rank_score[rank]


def get_players(members, stats, rank_score):
    players = []
    for i in range(10):
        try:
            if members.count(members[i]) > 1:
                print(f"入力されたプレイヤー名'{members[i]}'が重複しています。")
                raise Exception
            new_player = Player(
                name=members[i], player_stats=stats, rank_score=rank_score
            )
            players.append(new_player)
        except IndexError as e:
            print("Memberの数が足りません。")
            print("Memberの数は10人である必要があります。")
            sys.exit()
    return players


def assessment_permutation(permutation, players, lane_weight):
    team1 = []  # permutation[0]~permutation[4]のplayerはteam1
    team2 = []  # permutation[5]~permutation[9]のplayerはteam2
    team1_score_sum = 0
    team2_score_sum = 0
    lane_diff_sum = 0
    # 組み合わせの0～4をteam1, 5～9をteam2とする
    for i in range(5):
        team1.append(players[permutation[i]])
        team2.append(players[permutation[i + 5]])
    # 各レーンの誤差の総和を求める
    for lane in Lanes:
        team1_score_sum += team1[lane.value].score[lane.value] * lane_weight[lane.name]
        team2_score_sum += team2[lane.value].score[lane.value] * lane_weight[lane.name]
        lane_diff = (
            team1[lane.value].score[lane.value] - team2[lane.value].score[lane.value]
        )
        lane_diff_sum += abs(lane_diff) * lane_weight[lane.name]
    team_diff = abs(team1_score_sum - team2_score_sum) * lane_weight["team"]
    return team_diff + lane_diff_sum


def disp_permutation_summury(permutation, players):
    ret_str = ""
    ret_str += "LANE              TEAM1                             TEAM2" + "\n"
    # ret_str += "---------------------------------------------------------------" + "\n"
    for lane in Lanes:
        p1 = players[permutation[0 + lane.value]]
        p2 = players[permutation[5 + lane.value]]
        ret_str += f"{lane.name} : "
        p1_name_rank = p1.name + "[" + p1.rank[lane.value] + "]"
        p2_name_rank = p2.name + "[" + p2.rank[lane.value] + "]"
        ret_str += p1_name_rank.center(30) + " vs " + p2_name_rank.center(30) + "\n"
    print(ret_str)
    return ret_str


def calc_best_permutation(members):
    (lane_weight, rank_score, player_stats) = load_setting_by_json("./")
    players = get_players(members, player_stats, rank_score)

    inp_list = list(range(10))
    permutations = list(itertools.permutations(inp_list))

    minimum_diff = float("inf")
    best_permutation = permutations[0]

    # print("10!~=363万通りの総当たり探索を開始します。")
    # print("この処理は使用CPUの性能によって30秒～2分程度の処理時間を要します。\n")

    for i, permutation in enumerate(permutations):
        diff = assessment_permutation(permutation, players, lane_weight)
        if diff < minimum_diff:
            minimum_diff = diff
            best_permutation = permutation

    ret_str = disp_permutation_summury(best_permutation, players)
    return ret_str


# --------------MAIN-----------------
if __name__ == "__main__":
    None
    # calc_best_permutation()
    (
        lane_weight,
        rank_score,
        members,
        player_stats,
    ) = load_setting_by_json("./")
    for ele in player_stats:
        print(ele)
