#Análisis para Corte 3
import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html, Input, Output
import plotly.graph_objects as go

zaga = pd.read_excel("dataset\Radicaciones y pagos.xlsx")
app = Dash(__name__)

app.layout = html.Div(children=[
    html.H1(children='Dashboard de Rendimiento'),
    html.Div([
    dcc.Graph(id='chart1'),
    dcc.Graph(id='chart2'),
    dcc.Graph(id='chart3'),
    dcc.Graph(id='chart4'),
    dcc.Graph(id='chart5')
    ])
])
@app.callback(
    Output(component_id='chart1', component_property='figure'),
    [Input('chart1', 'relayoutData')]
)
def display_chart1(relayoutData):
    advisor_counts = zaga['ASESOR'].value_counts().nlargest(30)
    fig1 = go.Figure(data=[go.Bar(x=advisor_counts.index, y=advisor_counts.values, marker_color='thistle')])
    fig1.update_layout(
        title="Rendimiento de los asesores",
        xaxis_title="Asesores",
        yaxis_title="Cantidad de clientes",
        xaxis=dict(tickangle=45),
        yaxis=dict(
            type='linear',
            tickmode='linear',
            tick0=0,
            dtick=1,
        ),
        showlegend=False,
        font=dict(family='Courier New', size=14, color='black'),
        height=800
    )
    return fig1

@app.callback(
    Output(component_id='chart2', component_property='figure'),
    [Input('chart2', 'relayoutData')]
)
def display_chart2(relayoutData):
    convenio_counts = zaga['CONVENIO'].value_counts().nlargest(30)
    fig2 = go.Figure(data=[go.Bar(x=convenio_counts.index, y=convenio_counts.values, marker_color='skyblue')])
    fig2.update_layout(
        title="Rendimiento del convenio",
        xaxis_title="Convenios",
        yaxis_title="Cantidad de clientes",
        xaxis=dict(tickangle=45),
        yaxis=dict(type='linear'),
        showlegend=False,
        font=dict(family='Courier New', size=12, color='black'),
        height=600
    )
    return fig2

@app.callback(
    Output(component_id='chart3', component_property='figure'),
    [Input('chart3', 'relayoutData')]
)
def display_chart3(relayoutData):
    zaga_sin_negados = zaga[~zaga['ESTADO'].isin(['Negado', 'Desistio'])]
    rendimiento_asesores = zaga_sin_negados.groupby('ASESOR')['MONTO '].sum()
    rendimiento_asesores_sorted = rendimiento_asesores.sort_values()
    fig3 = go.Figure(data=[go.Bar(x=rendimiento_asesores_sorted.index, y=rendimiento_asesores_sorted.values, marker_color='plum')])
    fig3.update_layout(
        title='Rendimiento de Asesores por Monto Prestado',
        xaxis_title='Asesor',
        yaxis_title='Monto Prestado (en millones)',
        xaxis=dict(tickangle=45),
        yaxis=dict(type='linear', tickformat="$.1fM"),
        showlegend=False,
        font=dict(family='Courier New', size=14, color='black')
    )
    return fig3

@app.callback(
        Output(component_id='chart4', component_property='figure'),
        [Input('chart4', 'relayoutData')]
)
def display_chart4(relayoutData):
    scatter_graph = px.scatter(zaga, x='ESTADO', y='MONTO ', title='Relación entre el monto y el estado', color='ESTADO', color_continuous_scale='Burg')
    scatter_graph.update_layout(title_font=dict(family='Courier New', size=16, color='black'), font=dict(family='Courier New', size=14, color='black'))

    return scatter_graph


@app.callback(
    Output(component_id='chart5', component_property='figure'),
    [Input('chart5', 'relayoutData')]
)
def display_chart5(relayoutData):
    df_pie = zaga['ESTADO'].value_counts().nlargest(20).reset_index()
    df_pie.columns = ['Estado', 'Count']
    
    pie_chart_fig = px.pie(
        df_pie, 
        names='Estado', 
        values='Count', 
        title="Estado de los créditos",
        labels={'Count': 'Número de créditos'}, 
        width=800, height=600,
        color_discrete_sequence=px.colors.qualitative.Set3
    )
    pie_chart_fig.update_layout(
        title_font=dict(family='Courier New', size=16, color='black'),
        
    )
    return pie_chart_fig

if __name__ == '__main__':
    app.run_server(debug=True)