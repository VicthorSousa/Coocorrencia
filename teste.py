import streamlit as st
import pandas as pd

pd.options.display.float_format = '{:.0f}'.format

st.set_page_config(page_title='Análise de Coocorrência', page_icon=':bar_chart:')

df1 = pd.read_csv('cupons_janeiro_matriz.csv', on_bad_lines='skip', sep=';')
df2 = pd.read_csv('cupons_fevereiro_matriz.csv', on_bad_lines='skip', sep=';')
df = pd.concat([df1, df2])

produto_lista = df['DESCRI'].sort_values().unique()

st.title(':bar_chart: Análise de Produtos - Coocorrência - Loja Avenida')
option = st.selectbox(label='Selecione o produto', options=produto_lista, placeholder='Selecione o produto...')
#nome_produto = st.markdown(sorted(option))



qnt_total = df['NUMCUP'].nunique()                      
df3 = df.loc[(df['DESCRI']==option), ['NUMCUP','DESCRI', 'QTDPRD']]
cupons_lista = df3['NUMCUP'].tolist()
new_df = df.loc[df['NUMCUP'].isin(cupons_lista)]
quantidade = new_df['NUMCUP'].nunique()
new_df1 = new_df.groupby('DESCRI').nunique().sort_values('QTDPRD')
new_df1.rename(columns={'NUMCUP': 'Qnt Cupons'})
new_df2 = new_df1.sort_values(('NUMCUP'), ascending=False).head(500)
new_df2['Total'] = new_df['NUMCUP'].nunique()
new_df2['Percentual'] = (new_df2['NUMCUP'] / new_df2['Total'] * 100).round(2).astype(str) + '%'
new_df2.drop(['NUMCUP', 'QTDPRD', 'Total'], axis=1, inplace=True)

st.text(f'Analise de {quantidade} cupons emitidos do produto selecionado')
st.text(f'de um total de {qnt_total} cupons.')
st.text('Dados referentes a venda de 1B2024')
st.dataframe(new_df2, use_container_width=True)