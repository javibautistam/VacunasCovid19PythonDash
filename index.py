import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
from dash.dependencies import Input, Output


df = pd.read_csv("Covid19VacunasAgrupadas.csv")
df2 = df.groupby('vacuna_nombre')[['dosis_unica_cantidad', 'primera_dosis_cantidad', 'segunda_dosis_cantidad', 'dosis_adicional_cantidad', 'dosis_refuerzo_cantidad']].sum().reset_index()

app = dash.Dash(__name__)

app.layout = html.Div([

    html.Div([  #Barra superior, titulo y banner
        html.H1('Vacunados por Covid'),
        html.Img(src='assets/vacunas.jpg')
    ], className = 'banner'),

    html.Div([  # cuadro de seleccion de dosis
        html.Div([
            html.P('Selecciona la dosis', className='fix_label', style={'color':'black', 'margin-top':'2px'}),
            dcc.RadioItems(id = 'dosis-radioitems',
                labelStyle={'display':'inline-block'},
                options = [
                    {'label' : 'Primera dosis', 'value' : 'primera_dosis_cantidad'},
                    {'label' : 'Segunda dosis', 'value' : 'segunda_dosis_cantidad'},
                    {'label' : 'Dosis adicional', 'value' : 'dosis_adicional_cantidad'},
                    {'label' : 'Dosis refuerzo', 'value' : 'dosis_refuerzo_cantidad'},
                    {'label' : 'Dosis única', 'value' : 'dosis_unica_cantidad'}
                ], value = 'primera_dosis_cantidad',
                style = {'text-aling' : 'center', 'color' : 'black'}, className='dcc_compon'),
        ], className='create_container2 dosis_seleccion', style={'margin-bottom' : '20px'}),]
        , className='row flex-display', id="cuadroDosis"),

    html.Div([
        html.Div([
            dcc.Graph(id = 'my_graph', figure = {})
        ], className='create_container2 eight columns'),

        html.Div([
            dcc.Graph( id = 'pie_graph', figure={})
        ], className='create_container2 five columns'),

        ], className='row flex-display'),


    html.Div([
        html.Div([
            dcc.Graph(id = 'pieVacunas', figure = {})
        ], className='create_container2 five columns'),

        html.Div([
            dcc.Graph( id = 'pieNombreVacunas', figure={})
        ], className='create_container2 eight columns'),

        ], className='row flex-display'),
], id='mainContainer', style={'display': 'flex', 'flex-direction' : 'column'})

@app.callback(
    Output('my_graph', component_property='figure'),
    [Input('dosis-radioitems', component_property='value')]
)

def update_graph(value):

    if value == 'primera_dosis_cantidad':
        # Sumar la cantidad acumulada por provincia
        sum_df = df.groupby('jurisdiccion_nombre')['primera_dosis_cantidad'].sum().reset_index()
        # Ordenar el dataframe resultante por la cantidad acumulada
        sorted_df = sum_df.sort_values('primera_dosis_cantidad', ascending=False)
        fig = px.bar(
            data_frame = sorted_df,
            x = 'jurisdiccion_nombre',
            y = 'primera_dosis_cantidad',
            category_orders={'jurisdiccion_nombre': sorted_df['jurisdiccion_nombre'].tolist()},
            labels={"jurisdiccion_nombre": "Provincia", "primera_dosis_cantidad":"Cantidad de primeras dosis"},
            title='Distribución de primeras dosis por Provincia')
    elif value == 'dosis_adicional_cantidad':
        # Sumar la cantidad acumulada por provincia
        sum_df = df.groupby('jurisdiccion_nombre')['dosis_adicional_cantidad'].sum().reset_index()
        # Ordenar el dataframe resultante por la cantidad acumulada
        sorted_df = sum_df.sort_values('dosis_adicional_cantidad', ascending=False)
        fig = px.bar(
            data_frame = sorted_df,
            x = 'jurisdiccion_nombre',
            y = 'dosis_adicional_cantidad',
            category_orders={'jurisdiccion_nombre': sorted_df['jurisdiccion_nombre'].tolist()},
            labels={"jurisdiccion_nombre": "Provincia", "dosis_adicional_cantidad":"Cantidad de dosis adicional"},
            title='Distribución dosis adicional por Provincia')
        
    elif value == 'dosis_refuerzo_cantidad':
        # Sumar la cantidad acumulada por provincia
        sum_df = df.groupby('jurisdiccion_nombre')['dosis_refuerzo_cantidad'].sum().reset_index()
        # Ordenar el dataframe resultante por la cantidad acumulada
        sorted_df = sum_df.sort_values('dosis_refuerzo_cantidad', ascending=False)
        fig = px.bar(
            data_frame = sorted_df,
            x = 'jurisdiccion_nombre',
            y = 'dosis_refuerzo_cantidad',
            category_orders={'jurisdiccion_nombre': sorted_df['jurisdiccion_nombre'].tolist()},
            labels={"jurisdiccion_nombre": "Provincia", "dosis_refuerzo_cantidad":"Cantidad de dosis refuerzo"},
            title='Distribución de dosis de refuerzo por Provincia')
    
    elif value == 'segunda_dosis_cantidad':
        # Sumar la cantidad acumulada por provincia
        sum_df = df.groupby('jurisdiccion_nombre')['segunda_dosis_cantidad'].sum().reset_index()
        # Ordenar el dataframe resultante por la cantidad acumulada
        sorted_df = sum_df.sort_values('segunda_dosis_cantidad', ascending=False)
        fig = px.bar(
            data_frame = sorted_df,
            x = 'jurisdiccion_nombre',
            y = 'segunda_dosis_cantidad',
            category_orders={'jurisdiccion_nombre': sorted_df['jurisdiccion_nombre'].tolist()},
            labels={"jurisdiccion_nombre": "Provincia", "segunda_dosis_cantidad":"Cantidad de segunda dosis"},
            title='Distribución de segundas dosis por Provincia')
    elif value == 'dosis_unica_cantidad':
        # Sumar la cantidad acumulada por provincia
        sum_df = df.groupby('jurisdiccion_nombre')['dosis_unica_cantidad'].sum().reset_index()
        # Ordenar el dataframe resultante por la cantidad acumulada
        sorted_df = sum_df.sort_values('dosis_unica_cantidad', ascending=False)
        fig = px.bar(
            data_frame = sorted_df,
            x = 'jurisdiccion_nombre',
            y = 'dosis_unica_cantidad',
            category_orders={'jurisdiccion_nombre': sorted_df['jurisdiccion_nombre'].tolist()},
            labels={"jurisdiccion_nombre": "Provincia", "dosis_unica_cantidad":"Cantidad de dosis unica"},
            title='Distribución de dosis unica por Provincia')
    return fig


@app.callback(
    Output('pie_graph', component_property='figure'),
    [Input('dosis-radioitems', component_property='value')]
)

def update_graph_pie(value):
    if value == 'primera_dosis_cantidad':
        fig2 = px.pie(
            data_frame = df,
            names='jurisdiccion_nombre',
            values='primera_dosis_cantidad')

    elif value == 'dosis_adicional_cantidad':
        fig2 = px.pie(
            data_frame = df,
            names='jurisdiccion_nombre',
            values='dosis_adicional_cantidad')

    elif value == 'dosis_refuerzo_cantidad':
        fig2 = px.pie(
            data_frame = df,
            names='jurisdiccion_nombre',
            values='dosis_refuerzo_cantidad')

    elif value == 'segunda_dosis_cantidad':
        fig2 = px.pie(
            data_frame = df,
            names='jurisdiccion_nombre',
            values='segunda_dosis_cantidad')
    elif value == 'dosis_unica_cantidad':
        fig2 = px.pie(
            data_frame = df,
            names='jurisdiccion_nombre',
            values='dosis_unica_cantidad')

    return fig2


@app.callback(
    Output('pieVacunas', component_property='figure'),
    [Input('dosis-radioitems', component_property='value')]
)
def update_PieVacunas(value):
    totalArgentinos = 46044703

    if value == 'primera_dosis_cantidad':
        totalDosis = df["primera_dosis_cantidad"].sum()
        sinDosis = totalArgentinos - totalDosis
        valores = [totalDosis, sinDosis]
        nombres = ['Total de Vacunados', 'Personas sin vacunar']
        fig3 = px.pie(
            values=valores,
            names=nombres,
            title='Distribución de primeras dosis por vacunados y no vacunados'
)
    elif value == 'segunda_dosis_cantidad':
        totalDosis = df["segunda_dosis_cantidad"].sum()
        sinDosis = totalArgentinos - totalDosis
        valores = [totalDosis, sinDosis]
        nombres = ['Total de Vacunados', 'Personas sin vacunar']
        fig3 = px.pie(
            values=valores,
            names=nombres,
            title='Distribución de segundas dosis por vacunados y no vacunados'
        )
    elif value == 'dosis_adicional_cantidad':
        totalDosis = df["dosis_adicional_cantidad"].sum()
        sinDosis = totalArgentinos - totalDosis
        valores = [totalDosis, sinDosis]
        nombres = ['Total de Vacunados', 'Personas sin vacunar']
        fig3 = px.pie(
            values=valores,
            names=nombres,
            title='Distribución de dosis adicional por vacunados y no vacunados'
        )
    elif value == 'dosis_refuerzo_cantidad':
        totalDosis = df["dosis_refuerzo_cantidad"].sum()
        sinDosis = totalArgentinos - totalDosis
        valores = [totalDosis, sinDosis]
        nombres = ['Total de Vacunados', 'Personas sin vacunar']
        fig3 = px.pie(
            values=valores,
            names=nombres,
            title='Distribución de dosis de refuerzo por vacunados y no vacunados'
        )
    elif value == 'dosis_unica_cantidad':
        totalDosis = df["dosis_unica_cantidad"].sum()
        sinDosis = totalArgentinos - totalDosis
        valores = [totalDosis, sinDosis]
        nombres = ['Total de Vacunados', 'Personas sin vacunar']
        fig3 = px.pie(
            values=valores,
            names=nombres,
            title='Distribución de dosis unica por vacunados y no vacunados'
        )
    return fig3


@app.callback(
    Output('pieNombreVacunas', component_property='figure'),
    [Input('dosis-radioitems', component_property='value')])
def update_nombreVacunas(value):
        if value == 'primera_dosis_cantidad':
            fig4 = px.pie(
                data_frame = df2,
                names='vacuna_nombre',
                values='primera_dosis_cantidad',
                title='Distribución de primeras dosis por fabricante de vacunas')

        elif value == 'dosis_adicional_cantidad':
            fig4 = px.pie(
                data_frame = df2,
                names='vacuna_nombre',
                values='dosis_adicional_cantidad',
                title='Distribución de dosis adicional por fabricante de vacunas')

        elif value == 'dosis_refuerzo_cantidad':
            fig4 = px.pie(
                data_frame = df2,
                names='vacuna_nombre',
                values='dosis_refuerzo_cantidad',
                title='Distribución de dosis de refuerzo por fabricante de vacunas')

        elif value == 'segunda_dosis_cantidad':
            fig4 = px.pie(
                data_frame = df2,
                names='vacuna_nombre',
                values='segunda_dosis_cantidad',
                title='Distribución de segundas dosis por fabricante de vacunas')
            
        elif value == 'dosis_unica_cantidad':
            fig4 = px.pie(
                data_frame = df2,
                names='vacuna_nombre',
                values='dosis_unica_cantidad',
                title='Distribución de dosis unica por fabricante de vacunas')

        return fig4


if __name__ == ('__main__'):
    app.run_server(debug=True)