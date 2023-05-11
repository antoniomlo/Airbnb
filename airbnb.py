# Importando as bibliotecas necessárias
import streamlit as st
import pandas as pd
import plotly.express as px

# Define o título e ícone da página
st.set_page_config(
    page_title="Análise do Airbnb - Lisboa", page_icon=":chart_with_upwards_trend:", layout="wide"
)

# Define o cabeçalho na sidebar
st.sidebar.markdown(
    "<div align='center'><img src='https://github.com/antoniomlo/Data_Science/blob/main/img/amlo-1.png?raw=true' width='100'></div>",
    unsafe_allow_html=True,
)
st.sidebar.title(" ")
st.sidebar.title(" ")
st.sidebar.title("""😁 Olá, seja bem-vindo(a)""")
st.sidebar.write(
    """Caso tenha alguma dúvida ou sugestão sobre a análise, fique a vontade para entrar em contato comigo! """
)
st.sidebar.subheader(
    """🚀 [Portfólio](https://www.figma.com/proto/BlN1MI7h6WY9FadR1yufiu/Portf%C3%B3lio?page-id=0%3A1&type=design&node-id=314-165&viewport=-15%2C627%2C0.12&scaling=scale-down&starting-point-node-id=314%3A165&hotspot-hints=0)"""
)
st.sidebar.subheader("""✉️ Contato""")
st.sidebar.markdown(
    """
<a href="mailto:antoniomlm26@gmail.com" target="_blank"><img width=35 src="https://i.redd.it/izqwm1g21b751.png"/></a>
<a href="https://www.linkedin.com/in/antoniomlo/" target="_blank"><img width=50 src="https://static.vecteezy.com/system/resources/previews/018/930/587/original/linkedin-logo-linkedin-icon-transparent-free-png.png"/></a>
""",
    unsafe_allow_html=True,
)


st.image(
    "https://github.com/antoniomlo/Data_Science/blob/main/img/LinkedIn%20cover%20-%201.png?raw=true"
)
st.title("Análise dos Dados do Airbnb - Lisboa")
st.markdown("*por [Antonio Melo](https://www.linkedin.com/in/antoniomlo/)*")


st.markdown(
    """
O Airbnb é uma plataforma inovadora que está transformando a forma como as pessoas viajam e se hospedam. Fundada há 14 anos, em 2008, a empresa já se tornou a maior rede de hospedagem do mundo, superando muitas redes hoteleiras tradicionais, sem possuir nenhum hotel próprio.

Atualmente, o Airbnb está presente em mais de **220 países**, com mais de **7 milhões de anúncios de acomodações** em sua plataforma, incluindo casas, apartamentos, quartos e até mesmo castelos e iglus. A empresa tem sido responsável por mudar a forma como as pessoas viajam, tornando a interação entre hóspede e anfitrião mais próxima e pessoal, e oferecendo opções de hospedagem que muitas vezes são mais acessíveis e autênticas do que as opções tradicionais de hotéis.

Além disso, o Airbnb tem sido um grande impulsionador da economia local, ajudando proprietários de imóveis e pequenos empreendedores a ganhar dinheiro extra ao alugar suas acomodações para viajantes. Com dados disponíveis através do portal Inside Airbnb, é possível explorar insights e informações valiosas sobre o mercado de hospedagem em diversas cidades do mundo, incluindo Lisboa. Esses dados podem ser utilizados para desenvolver projetos de Data Science, identificar tendências e padrões de consumo, e auxiliar na tomada de decisões estratégicas para proprietários de imóveis e empresas do setor de turismo. 

Para acessar os dados disponíveis no portal Inside Airbnb, basta visitar o link *[Inside Airbnb](http://insideairbnb.com/get-the-data.html)*.
"""
)

st.write(
   """Neste notebook, explorarei os dados do Airbnb em Lisboa para descobrir informações valiosas e insights que podem ajudar a entender melhor o mercado 
         de hospedagem da cidade. Com técnicas de análise de dados e visualização, iremos descobrir tendências, padrões e oportunidades para quem está interessado 
         em investir ou utilizar os serviços do Airbnb em Lisboa."""
)

# Importando o arquivo csv que iremos colocar no DataFrame e substituindo os valores NaN por string vazia
df = pd.read_csv(
    "http://data.insideairbnb.com/portugal/lisbon/lisbon/2023-03-19/visualisations/listings.csv",
    encoding="utf-8",
    na_values=["NaN", "N/A"],
).fillna("")

st.title("Obtenção dos Dados")
st.markdown(
    """
            Compreender dados é essencial para tomar decisões mais informadas em diversas áreas. E a boa notícia é que há ferramentas que podem ajudar na análise desses 
            dados de forma clara e objetiva, como as bibliotecas de análise de dados e gráficos em Python. Essas bibliotecas permitem criar visualizações que ajudam a 
            identificar padrões, tendências e relações entre variáveis. E o melhor é que você não precisa ser um especialista em programação para utilizá-las.
            """
)
st.markdown(
    "Basta importar as bibliotecas adequadas e seguir algumas boas práticas para garantir gráficos legíveis e informativos."
)

cor1 = ["#FF5A5F"]
colors = {
    "Entire home/apt": "#FF5A5F",
    "Private room": "#262730",
    "Shared room": "#262730",
    "Hotel room": "#802D2F",
}

# Mostrando o código
with st.expander("Expandir Código"):
    st.code(
        """
      # Importando as bibliotecas necessárias
        import streamlit as st
        import pandas as pd
        import plotly.express as px

        # Importando o arquivo csv que iremos colocar no DataFrame e substituindo os valores NaN por string vazia
        df = pd.read_csv("http://data.insideairbnb.com/portugal/lisbon/lisbon/2023-03-19/visualisations/listings.csv", na_values=["NaN", "N/A"]).fillna("")
    """
    )

st.title("Análise dos Dados")
st.markdown(
    """
            Neste tópico, vamos analisar os dados do Airbnb em Lisboa para encontrar insights e informações valiosas sobre o mercado de hospedagem na cidade. Vamos utilizar técnicas de análise de dados 
            e visualização para descobrir tendências e padrões que possam ajudar na tomada de decisões estratégicas, seja para investidores ou empresas do setor de turismo.
            """
)

data_dict = {
    "id": "Número de ID do imóvel",
    "name": "Nome da propriedade anunciada",
    "host_id": "Número de ID do proprietário",
    "host_name": "Nome do proprietário",
    "neighbourhood_group": "Nome da Cidade",
    "neighbourhood": "Nome do Bairro",
    "latitude": "Coordenada da latitude da propriedade",
    "longitude": "Coordenada da longitude da propriedade",
    "room_type": "Tipo de quarto",
    "price": "Preço do aluguel",
    "minimum_nights": "Mínimo de noites para reserva",
    "number_of_reviews": "Número de feedbacks da propriedade",
    "last_review": "Data do último feedback",
    "reviews_per_month": "Número de feedbacks por mês",
    "calculated_host_listings_count": "Quantidade de imóveis do mesmo proprietário",
    "availability_365": "Número de dias de disponibilidade dentro de 365 dias",
}
st.header("Dicionário das variáveis")
st.write("Aqui irei disponibilizar um dicionário das variáveis presentes no dataset.")
with st.expander("Expandir Dicionário"):
    st.write(data_dict)

st.header("Visualização")
st.write(
    "Para iniciar, irei analisar os dados brutos para obter os insights necessários."
)

tab1, tab2, tab3 = st.tabs(["Tabela", "Informações", "Gráficos"])
with tab1:
    st.subheader("Tabela")
    st.write("Essa é uma pré visualização dos dados presentes em nosso dataset.")
    st.dataframe(df.head(10))

with tab2:
    st.subheader("Informações Gerais")

    # Identificando o volume de dados do DataFrame
    rows = "{:,}".format(df.shape[0]).replace(",", ".")
    st.markdown(f"O dataset possui **{rows} linhas** e **{df.shape[1]} colunas**.")

    # Verificando os tipos de variáveis presentes
    st.write("Tipos de variáveis presentes no dataset:")

    col1, col2 = st.columns([3, 2])
    col1.write(df.dtypes)
    t = df.dtypes.value_counts()
    l = len(t)
    i = df.select_dtypes(include=["int"]).shape[1]
    f = df.select_dtypes(include=["float"]).shape[1]
    o = df.select_dtypes(include=["object"]).shape[1]

    col2.metric(label="", value=l, delta="tipos de variáveis", delta_color="off")
    col2.metric(label="", value=i, delta="variáveis do tipo inteiro", delta_color="off")
    col2.metric(label="", value=f, delta="variáveis do tipo float", delta_color="off")
    col2.metric(label="", value=o, delta="variáveis do tipo objeto", delta_color="off")

with tab3:
    st.write(
        "Nessa seção é possível ver como se encontra a distribuição dos valores no dataset."
    )
    num_cols = df.select_dtypes(include=["int64", "float64"]).columns.tolist()
    coluna_selecionada = st.selectbox("Selecione a coluna", num_cols)
    col1, col2 = st.columns([3, 1.5])

    # Plota o histograma da coluna selecionada
    fig = px.histogram(df, x=coluna_selecionada, nbins=15, color_discrete_sequence=cor1)
    fig.update_yaxes(title="Contagem")
    fig.update_layout(title=coluna_selecionada, bargap=0.1)
    col1.plotly_chart(fig)

    fig2 = px.box(
        df,
        y=coluna_selecionada,
        color_discrete_sequence=cor1,
        points="all",
        width=250,
        height=465,
    )
    fig2.update_traces(jitter=0, pointpos=-2)
    fig2.update_layout(yaxis_title="Valor")
    col2.plotly_chart(fig2)
    st.markdown(
        """Quando o valor filtrado é *minimum_nights* é possível ver que há alguns valores acima de 365 dias, o que está afetando drascticamente
     a distribuilção dos valores e também o boxplot. Na coluna *price* temos a mesma situação, com alguns valores de diárias muito altas."""
    )

st.markdown(
    """Com essa visualização, é possível notar na aba **Gráficos** que diversas colunas, como *minimum_nights e price* por exemplo,
possuem alguns ***outliers***, que são valores fora da curva e atrapalham um pouco a visualização e torna a análise menos precisa. 
Visando ter uma análise mais assertiva, antes de iniciar irei remover esses valores fora da curva."""
)

st.write(
    """Vale ressaltar que no começo os valores nulos foram substituídos por strings vazias então o dataset não possui mais valores desse
 tipo. Então, o próximo passo será fazer o tratamento dos outliers e começar a análise em si."""
)

st.title("Tratamento dos Dados")
st.markdown(
    """
            Para esta étapa, irei utilizar a função *drop* para remover as propriedades que tem os valores de *minimum_nights* maiores que    **14 noites**, tendo em vista que é uma pesquisa
            para ajudar viajantes que estão indo para conhecer a cidade. Além disso, irei remover todos os imóveis com valores acima de **€600 euros** 
            por noite na coluna *price*, visando tornar a pesquisa mais objetiva, e filtrar o dataset somente para a cidade de Lisboa.
            """
)

# Definindo o novo dataset sem outliers
df_clean = df.copy()
df_clean.drop(df_clean[df_clean.price > 300].index, axis=0, inplace=True)
df_clean.drop(df_clean[df_clean.minimum_nights > 14].index, axis=0, inplace=True)
df_clean = df_clean[df_clean["neighbourhood_group"] == "Lisboa"]

# Mostrando o código
with st.expander("Expandir Código"):
    st.code(
        """
        # Definindo o novo dataset sem outliers
    df_clean = df.copy()
    df_clean.drop(df_clean[df_clean.price > 600].index, axis=0, inplace=True)
    df_clean.drop(df_clean[df_clean.minimum_nights > 10].index, axis=0, inplace=True)
    df_clean = df_clean[df_clean['neighbourhood_group'] == 'Lisboa']
    """
    )

tab1, tab2 = st.tabs(["Diárias", "Valores"])
with tab1:
    st.write(
        "Nessa seção é possível ver como se encontra a distribuição dos valores no dataset."
    )
    coluna_selecionada = "minimum_nights"
    col1, col2 = st.columns([3, 1.5])

    # Plota o histograma da coluna selecionada
    fig = px.histogram(
        df_clean, x=coluna_selecionada, nbins=15, color_discrete_sequence=cor1
    )
    fig.update_yaxes(title="Contagem")
    fig.update_layout(title=coluna_selecionada, bargap=0.1)
    col1.plotly_chart(fig)

    fig2 = px.box(
        df_clean,
        y=coluna_selecionada,
        color_discrete_sequence=cor1,
        points="all",
        width=250,
        height=465,
    )
    fig2.update_traces(jitter=0, pointpos=-2)
    fig2.update_layout(yaxis_title="Valor")
    col2.plotly_chart(fig2)

with tab2:
    st.write(
       "Nessa seção é possível ver como se encontra a distribuição dos valores no dataset."
    )
    coluna_selecionada = "price"
    col1, col2 = st.columns([3, 1.5])

    # Plota o histograma da coluna selecionada
    fig = px.histogram(
        df_clean, x=coluna_selecionada, nbins=15, color_discrete_sequence=cor1
    )
    fig.update_yaxes(title="Contagem")
    fig.update_layout(title=coluna_selecionada, bargap=0.1)
    col1.plotly_chart(fig)

    fig2 = px.box(
        df_clean,
        y=coluna_selecionada,
        color_discrete_sequence=cor1,
        points="all",
        width=250,
        height=465,
    )
    fig2.update_traces(jitter=0, pointpos=-2)
    fig2.update_layout(yaxis_title="Valor")
    col2.plotly_chart(fig2)

st.markdown(
    """Ao analisar essas informações, podemos descobrir padrões e tendências que nos ajudarão a entender melhor as preferências dos turistas que visitam Lisboa e como podemos atender melhor suas necessidades.
    Além disso, podemos identificar oportunidades de negócios para proprietários de imóveis que desejam maximizar seus lucros e oferecer uma experiência de hospedagem de qualidade aos seus hóspedes.
     """
)
st.write(
    "Então, vamos mergulhar nesses dados e descobrir o que eles têm a nos revelar sobre a indústria de hospedagem em Lisboa pelo Airbnb!"
)

st.header("Tipos de acomodações mais reservados")
st.markdown(
    """Quando estamos buscando um lugar para nos hospedar, o tipo de acomodação pode fazer toda a diferença na experiência que teremos. Por isso, é importante entender quais são os tipos de acomodações mais populares em uma cidade, como Lisboa."""
)

qtd = df_clean.room_type.value_counts()
prec = df_clean.room_type.value_counts(normalize=True) * 100

tab1, tab2, tab3 = st.tabs(["Em quantidade", "Em porcentagem", "Média de preços"])
with tab1:
    fig1 = px.bar(
        df_clean,
        x=qtd.index,
        y=qtd,
        color=qtd.index,
        text=qtd,
        hover_name=qtd.index,
        color_discrete_map=colors,
    )

    fig1.update_traces(textposition="outside")
    fig1.update_layout(
        title="Quantidade de quartos por tipo",
        xaxis_title="Tipos de Quartos",
        yaxis_title="Contagem",
        legend_title="Tipos de quartos",
        width=1200,
    )
    st.plotly_chart(fig1)

with tab2:
    fig2 = px.bar(
        df_clean,
        x=prec.index,
        y=prec,
        color=prec.index,
        text=prec.apply(lambda x: "{:.2f}%".format(x)),
        hover_name=prec.index,
        color_discrete_map=colors,
    )

    fig2.update_traces(texttemplate="%{text}", textposition="outside")

    fig2.update_layout(
        title="Porcentagem de quartos por tipo",
        xaxis_title="Tipos de Quartos",
        yaxis_title="Porcentagem",
        legend_title="Tipos de quartos",
        width=1200,
    )
    st.plotly_chart(fig2)

with tab3:
    med = df_clean.groupby(["room_type"]).price.mean()
    fig1 = px.bar(
        df_clean,
        x=med.index,
        y=med,
        color=med.index,
        text=med,
        hover_name=med.index,
        color_discrete_map=colors,
    )

    fig1.update_traces(texttemplate="€ %{value:.2f}", textposition="outside")
    fig1.update_layout(
        title="Média de Preço por Tipo de Quarto",
        xaxis_title="Tipos de Quartos",
        yaxis_title="Média de Preço",
        legend_title="Tipos de quartos",
        width=1200,
    )
    st.plotly_chart(fig1)

st.markdown(
    """Agora que sabemos como está a disposição das propriedades no airbnb de Lisboa, é possível notar que mais de 75% das acomodações oferecidas são do tipo "Entire home/apt"
, que seriam acomodações inteiras. Com isso, sabemos que esse tipo de quarto é o mais alugado na cidade de Lisboa... mas será que é o mais em conta?

 Vamos descobrir a partir da média de preço de cada tipo de quarto.
 """
)

st.header("Tendências de preços na cidade de Lisboa")

st.markdown(
    """Nessa seção, vamos ver questões  relacionadas aos custos de hospedagens tanto em relação ao tipo de acomodação como também verificar quais 
os bairros mais caros e os mais baratos para se hospedar."""
)

top5 = df_clean.groupby(["neighbourhood"]).price.mean().sort_values(ascending=True)[-5:]
bot5 = (
    df_clean.groupby(["neighbourhood"]).price.mean().sort_values(ascending=False)[-5:]
)

default_color = "#262730"
colors = [default_color] * 5
colors[-1] = "#FF5A5F"
col1, col2 = st.columns([1, 1])

fig1 = px.bar(
    x=top5.values,
    y=top5.index,
    title="Bairros mais caros",
    width=550,
    color=top5.index,
    color_discrete_map={k: v for k, v in zip(top5.index, colors)},
    text=top5,
)
fig1.update_layout(
    xaxis_title="Média de Preço", yaxis_title="Bairros", showlegend=False
)
fig1.update_traces(texttemplate="€ %{value:.2f}", textposition="inside")
col1.plotly_chart(fig1)

fig2 = px.bar(
    x=bot5.values,
    y=bot5.index,
    title="Bairros mais baratos",
    width=550,
    color=bot5.index,
    color_discrete_map={k: v for k, v in zip(bot5.index, colors)},
    text=bot5,
)
fig2.update_layout(
    xaxis_title="Média de Preço", yaxis_title="Bairros", showlegend=False
)
fig2.update_traces(texttemplate="€ %{value:.2f}", textposition="inside")
col2.plotly_chart(fig2)

st.markdown(
    """Analisando os gráficos, vemos os 5 bairros mais caros e os 5 bairros mais baratos. O mais caro, que é o bairro ***Parque das Nações*** apresentou uma média de preços de **€123.70**,
 o que já era esperado por ser o bairro com um dos metros quadrados mais caros da cidade, por volta de 7 mil euros.


 Mas e se eu quiser me hospedar no bairro mais caro da cidade pagando pouco, é possível? **Vamos descobrir!**"""
)

col1, col2 = st.columns([2, 1])
df_pq = df_clean[df_clean["neighbourhood"] == "Parque das Naes"].price
fig2 = px.box(
    df_pq,
    y=coluna_selecionada,
    color_discrete_sequence=cor1,
    points="all",
    width=250,
    height=520,
)
fig2.update_traces(jitter=0, pointpos=-2)
fig2.update_layout(yaxis_title="Valor")
col2.plotly_chart(fig2)

col1.image(
    "https://content.r9cdn.net/rimg/dimg/84/94/535ec7a0-lm-167675-16d2176a611.jpg?width=1366&height=768&xhint=1339&yhint=1077&crop=true",
    width=800,
)

st.markdown(
    """E a resposta é **SIM!** É possível se hospedar no bairro mais caro pagando pouco. Com esse boxplot acima, é possível ver que o menor valor é de **€17**, que na cotação atual a noite sai por volta
de **R$92**.
"""
)

# Mapa das propriedades do Airbnb em Lisboa
st.header("Mapa das propriedades do Airbnb em Lisboa")
st.markdown(
    """Esse mapa abaixo, mostra os imóveis espalhados pelo dsitrito de Lisboa (não pela cidade) de acordo com sua localização e preço.
 Quanto mais vermelho, mais caro o preço por noite do imóvel..
"""
)
fig = px.scatter_mapbox(
    df_clean,
    lat="latitude",
    lon="longitude",
    hover_name="neighbourhood",
    height=600,
    hover_data=["price"],
    color="price",
    color_continuous_scale="jet",
    zoom=12,
    width=1200,
    title="Mapa de distribuição dos imóveis em Lisboa",
    labels={"price": "Preço médio"},
)
fig.update_layout(
    mapbox_style="carto-darkmatter",
    mapbox_center={"lat": df_clean.latitude.mean(), "lon": df_clean.longitude.mean()},
)
st.plotly_chart(fig)


st.header("Conclusões")
st.markdown(
    """Após análise detalhada dos dados do Airbnb em Lisboa, foram identificados diversos parâmetros relevantes, tais como as localidades mais caras para se hospedar,
 a média de preços por bairro, um mapa de calor com a distribuição dos imóveis e seus preços, e muito mais.


A partir dessas informações, foi possível concluir que mesmo com um orçamento limitado, é possível aproveitar tudo o que essa cidade incrível tem a oferecer e se hospedar em áreas nobres. 
Também foram identificados os tipos de imóveis mais procurados pelos usuários do Airbnb em Lisboa, bem como a média de noites de hospedagem.


É importante ressaltar que esta análise foi realizada de forma resumida, abordando apenas os principais parâmetros e utilizando um arquivo csv como fonte de dados. 
Apesar disso, os resultados obtidos permitem uma visão geral sobre a situação do mercado de hospedagem na cidade e podem ser úteis para quem busca informações relevantes sobre a 
hospedagem em Lisboa."""
)