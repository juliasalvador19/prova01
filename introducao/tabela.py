import streamlit as st

st.title('Tabela')
st.dataframe(
    st.session_state['df'],
    hide_index=True,
    use_container_width=True,
    column_config={
        'aeronave_valor': st.column_config.NumberColumn(format='R$ %.2f'),
        'ocorrencia_classificacao': st.column_config.Column(label='Classificação da Ocorrência'),
        'ocorrencia_tipo': st.column_config.Column(label='Tipo da Ocorrência'),
        'ocorrencia_dia': st.column_config.Column(label='Dia da Ocorrência'),
        'ocorrencia_cidade': st.column_config.Column(label='Cidade da Ocorrência'),
        'ocorrencia_uf': st.column_config.Column(label='UF da Ocorrência'),
        'aeronave_equipamento': st.column_config.Column(label='Equipamento da Aeronave'),
        'aeronave_fabricante': st.column_config.Column(label='Fabricante da Aeronave'),
        'aeronave_modelo': st.column_config.Column(label='Modelo da Aeronave'),
        'aeronave_quantidade_motores': st.column_config.Column(label='Quantidade Motores da Aeronave'),
        'aeronave_peso_maximo_decolagem': st.column_config.Column(label='Peso Máximo de Decolagem da Aeronave'),
        'aeronave_valor': st.column_config.Column(label='Valor da Aeronave'),
        'aeronave_ano_fabricacao': st.column_config.Column(label='Ano de Fabricação da Aeronave'),
        'aeronave_segmento_aviacao': st.column_config.Column(label='Segmento de Aviação da Aeronave'),
        'aeronave_nivel_dano': st.column_config.Column(label='Nível de Dano da Aeronave'),
        'quantidade_fatalidades': st.column_config.Column(label='Quantidade de Fatalidades da Ocorrência'),
        'ocorrencia_ano': st.column_config.Column(label='Ano da Ocorrência'),
        'ocorrencia_mes': st.column_config.Column(label='Mês da Ocorrência')
    }
)
