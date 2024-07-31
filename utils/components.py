import streamlit as st
from streamlit_echarts import st_echarts
from datetime import datetime, timedelta

def component_hide_sidebar():
    st.markdown(""" 
    <style>
        section[data-testid="stSidebar"][aria-expanded="true"]{
                display: none;
                }
    </style>
    """, unsafe_allow_html=True)

def component_effect_underline():
    st.markdown("""
    <style>
        .full-width-line-white {
            width: 100%;
            border-bottom: 1px solid #ffffff;
            margin-bottom: 0.5em;
        }
        .full-width-line-black {
            width: 100%;
            border-bottom: 1px solid #000000;
            margin-bottom: 0.5em;
        }
    </style>
    """, unsafe_allow_html=True)

def component_plotDataframe(df, name):
    st.markdown(f"<h5 style='text-align: center; background-color: #ffb131; padding: 0.1em;'>{name}</h5>", unsafe_allow_html=True)
    keywords = ['VER DETALHES', 'VER CANDIDATOS', 'DISPARAR WPP', 'PERFIL ARTISTA'] # usado para procurar colunas que contenham links
    columns_with_link = [col_name for col_name in df.columns if any(keyword in col_name.upper() for keyword in keywords)]
    
    if columns_with_link:
        column_config = {
            col: st.column_config.LinkColumn(
                col, display_text="[Saiba mais]"
            ) for col in columns_with_link
        }
        st.dataframe(df, use_container_width=True, column_config=column_config, hide_index=True)
    else:
        st.dataframe(df, hide_index=True, use_container_width=True)

def component_filterMultiselect(df, column, text):
    options = df[column].unique().tolist()

    selected_options = st.multiselect(text, options, default=options)
    return selected_options