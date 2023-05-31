import streamlit as st
import AutoTeamBalancer

(
    lane_weight,
    rank_score,
    player_stats,
) = AutoTeamBalancer.load_setting_by_json("./")

members = st.multiselect("Select member!", options=player_stats)
try:
    progress_bar = st.progress(len(members) * 10, text=str(len(members)) + " / 10")
except:
    st.error("The number of members exceeded 10!")

if len(members) == 10:
    start_calc_button = st.button("Start Calculation")
else:
    start_calc_button = st.button("Start Calculation", disabled=True)

if start_calc_button == True:
    summury = AutoTeamBalancer.calc_best_permutation(members)
    st.code(summury)
