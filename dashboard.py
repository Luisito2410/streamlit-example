
import streamlit as st
import pandas as pd
import plotly.express as px
import calendar

# #Vamos a leer los datos
dfCafe = pd.read_excel("datos/resultadoLimpiezaCafe.xlsx")

st.title("Dashboard afluencia de los clientes - Cafe internet")

anios = list(set(dfCafe['fechaEntrada'].dt.year))
meses = list(set(dfCafe['fechaEntrada'].dt.month_name()))

#Vamos a usar el sidebar para mostrar los controles que nos sirven para aplicar los filtros
#1. Año
#2. Mes

anioSeleccionado = st.sidebar.selectbox('Seleccionar año', anios)
mesSeleccionado = st.sidebar.selectbox('Seleccionar mes', meses)
mesSorted = list(calendar.month_name)
###########################
#Antes de las gráficas mostramos tambien el df ya filtrado
dfFiltradoMesanio = dfCafe[ (dfCafe['fechaEntrada'].dt.month_name() == mesSeleccionado) & (dfCafe['fechaEntrada'].dt.year == anioSeleccionado)]
dfMes = dfFiltradoMesanio.groupby(pd.Grouper(key="fechaEntrada",freq="1D")).count().reset_index()
dfMes['fechaStr']=dfMes['fechaEntrada'].astype(str)+ ' - '
dfMes['Dia']= dfMes['fechaEntrada'].dt.day_name()+ ' - ' + dfMes['fechaStr']

#En la parte central vamos a mostrar la gráfica comparativa por mes de los dos años

#La gráfica de días por mes seleccionado
fig = px.bar(dfMes, x='Dia', y='horaEntrada',labels={'fechaEntrada':'Dia','horaEntrada':'Numero de clientes'}, text='horaEntrada',title='Número de clientes por semana')
st.plotly_chart(fig,use_container_width=True)
