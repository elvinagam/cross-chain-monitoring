# Libraries
import streamlit as st
import pandas as pd

# Data Sources
# @st.cache(ttl=1000, allow_output_mutation=True)
def get_data(query):
    if query == 'Transactions Overview':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/579714e6-986e-421a-85dd-c32a8b41b25c/data/latest')
        # return pd.concat(
        #     [arbitrum, avalanche, axelar, bsc, cosmos, ethereum, flow, gnosis, near, optimism, osmosis, polygon, solana]
        #         ).sort_values('Blockchain').reset_index(drop=True)
    return None