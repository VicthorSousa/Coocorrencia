import streamlit as st
import pandas as pd

pd.options.display.float_format = '{:.0f}'.format

df = pd.read_csv('cupons_janeiro_filial.csv', on_bad_lines='skip', sep=';')
produto_lista = df['Produto'].sort_values(ignore_index=False).unique()

st.title('Análise de Produtos - Coocorrência')
option = st.selectbox(label='Selecione o produto', options=produto_lista, index=None,placeholder='Selecione o produto...')
#nome_produto = st.markdown(sorted(option))



qnt_total = df['CUPNUM'].nunique()                      
df1 = df.loc[(df['Produto']==option), ['CUPNUM','CODPRD', 'CODBAR', 'Produto', 'Qnt Venda', 'Total']]
cupons_lista = df1['CUPNUM'].tolist()
new_df = df.loc[df['CUPNUM'].isin(cupons_lista)]
quantidade = new_df['CUPNUM'].nunique()
new_df1 = new_df.groupby('Produto').nunique().sort_values('Qnt Venda')
new_df1.rename(columns={'CUPNUM': 'Qnt Cupons'})
new_df2 = new_df1.sort_values(('CUPNUM'), ascending=False).head(500)
new_df2['Total'] = new_df['CUPNUM'].nunique()
new_df2['Percentual'] = (new_df2['CUPNUM'] / new_df2['Total'] * 100).round(2).astype(str) + '%'
new_df2.drop(['Qnt Venda', 'Total', 'CODPRD', 'CODBAR', 'CUPNUM'], axis=1, inplace=True)

st.text(f'Analise de {quantidade} cupons.')
st.dataframe(new_df2, use_container_width=True)
