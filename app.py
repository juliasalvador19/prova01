import pandas as pd
import streamlit as st


@st.cache_data
def load_database():
    df = pd.read_excel('data/accidents.xlsx')
    df['ocorrencia_ano'] = df['ocorrencia_dia'].dt.year
    df['ocorrencia_mes'] = df['ocorrencia_dia'].dt.month
    df['aeronave_ano_fabricacao'] = df['aeronave_ano_fabricacao'].astype(str)
    df['ocorrencia_ano'] = df['ocorrencia_ano'].astype(str)
    return df

st.session_state['df'] = load_database()

st.session_state['dimensao'] = ['ocorrencia_classificacao', 'ocorrencia_tipo', 'ocorrencia_cidade', 'ocorrencia_uf', 'aeronave_equipamento', 'aeronave_fabricante', 'aeronave_modelo', 'aeronave_quantidade_motores', 'aeronave_segmento_aviacao', 'aeronave_nivel_dano']
st.session_state['dimensao_tempo'] = ['ocorrencia_ano', 'ocorrencia_mes', 'aeronave_ano_fabricacao']
st.session_state['medida'] = ['aeronave_peso_maximo_decolagem', 'aeronave_valor', 'quantidade_fatalidades']
st.session_state['agregador'] = ['sum', 'mean', 'count', 'min', 'max']

st.title('Gestão de Conhecimento')

pg = st.navigation(
    {
        "Introdução": [
            st.Page(page='introducao/tabela.py', title='Tabela', icon=':material/house:'),
            st.Page(page='introducao/cubo.py', title='Cubo', icon=':material/help:'),
            st.Page(page='introducao/dashboard.py', title='Dashboard', icon=':material/help:'),
            st.Page(page='introducao/visualizacao.py', title='Visualização', icon=':material/help:'),
        ],
    }
)

pg.run()


