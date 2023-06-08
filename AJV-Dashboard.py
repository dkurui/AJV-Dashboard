import dash                              # pip install dash
from dash import html
from dash import dcc
from dash.dependencies import Output, Input
from dash_extensions import Lottie       # pip install dash-extensions
import dash_bootstrap_components as dbc  # pip install dash-bootstrap-components
import plotly.express as px              # pip install plotly
import pandas as pd                      # pip install pandas
from dash.dependencies import Input, Output, State
from dash import dash_table
from datetime import date
import calendar
from wordcloud import WordCloud
from dash import dependencies
yes_url = 'https://assets7.lottiefiles.com/packages/lf20_oaw8d1yt.json'
no_url = 'https://assets7.lottiefiles.com/packages/lf20_g0rackmk.json'
options = dict(loop=True, autoplay=True, rendererSettings=dict(preserveAspectRatio='xMidYMid slice'))
data = pd.read_excel('ajv.xlsx')
journals = data['Journal tittle']

data_frame = pd.DataFrame()
# Bootstrap themes by Ann: https://hellodash.pythonanywhere.com/theme_explorer
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.LUX])

app.layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            dbc.Card([
                html.H1('AFRICAN JOURNALS VISIBILITY DASHBOARD', style={'font-family': 'Verdana', 'text-align': 'center'}),
                # dbc.CardImg(src='/assets/Linkedin-Logo.png') # 150px by 45px
            ], className='mb-2'),

        ], width=12),

    ], className='mb-2 mt-5'),

    dbc.Row([
        dbc.Col([
                dbc.Card([
                    dbc.CardHeader('Total Number of Journals Considered', style={'font-family': 'Inter'}),
                    dbc.CardBody([
                        # html.P('12345'),
                        html.Div(id='content-total', style={'color': 'darkviolet','font-weight': 'bold', 'font-size':'28px'}),
                        # html.P('See full list here'),

                    ],style={'textAlign': 'center'})
                ]),
        ], width=3),
        dbc.Col([
                dbc.Card([
                    dbc.CardHeader('Select the Journal from the dropdown below to see its details', style={'font-family': 'Helevitica'}),
                    dbc.CardBody([
                        html.P(''),
                        # dcc.Input(id='dropdown-id', value='initial value', type='text'),
                        dcc.Dropdown(
                            options=[{'label': journal, 'value': journal} for journal in journals],
                            # value=data['Journal tittle'][0],  # Set the initial value based on your data
                            value='',  # Set the initial value based on your data
                            id='dropdown-id'
                        ),

                    ])
                ] ),
        ], width=6),

    ], className='mb-2 mt-2'),

    dbc.Row([

        dbc.Col([
            dbc.Card([
                dbc.CardHeader(),
                dbc.CardBody([
                    html.H6('PLATFORM'),
                    # html.H2(id='content-platform', children="000", style={'color': 'black'}),
                    html.Div(id='content-platform', style={'color': 'darkviolet','font-weight': 'bold', 'font-size':'12px'}),
                ], style={'textAlign': 'center',
                          'box-shadow': 'rgba(0, 0, 0, 0.3) 0px 19px 38px, rgba(0, 0, 0, 0.22) 0px 15px 12px','line-height': '1', 'font-size':'11px','height': '6rem'})
            ]),
            dbc.Card([
                dbc.CardBody([
                    html.P('Hosted on INASP\'S Journal online'),
                    html.Div(id='content-based-inasp', style={'display': 'none'}),
                    html.Div(id='lottie-content-based-inasp')
                ], style={'textAlign': 'center',
                          'box-shadow': 'rgba(0, 0, 0, 0.3) 0px 19px 38px, rgba(0, 0, 0, 0.22) 0px 15px 12px',
                          'line-height': '1', 'font-size':'9px','height': '7rem'})
            ], className='mt-2'),

            ], width=2),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.P('Indexed on Google scholar'),
                    html.Div(id='content-google-scholar', style = {'display':'none'}),
                    html.Div(id='lottie-content-google-scholar')
                ], style={'textAlign': 'center',
                          'box-shadow': 'rgba(0, 0, 0, 0.3) 0px 19px 38px, rgba(0, 0, 0, 0.22) 0px 15px 12px','line-height':'1', 'font-size':'11px','height': '7rem'})
            ]),
            dbc.Card([
                dbc.CardBody([
                    html.P('Indexed on Scopus'),
                    html.Div(id='content-scopus', style={'display': 'none'}),
                    html.Div(id='lottie-content-scopus')
                ], style={'textAlign': 'center',
                          'box-shadow': 'rgba(0, 0, 0, 0.3) 0px 19px 38px, rgba(0, 0, 0, 0.22) 0px 15px 12px','line-height':'1', 'font-size':'11px','height': '7rem'})
            ],className='mt-2'),
        ], width=2),

        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.P('Indexed on at least one platform'),
                    html.Div(id='content-one-platform', style={'display': 'none'}),
                    html.Div(id='lottie-content-one-platform')
                ], style={'textAlign': 'center',
                          'box-shadow': 'rgba(0, 0, 0, 0.3) 0px 19px 38px, rgba(0, 0, 0, 0.22) 0px 15px 12px',
                          'line-height': '1', 'font-size':'11px','height': '7rem'})
            ]),
            dbc.Card([
                dbc.CardBody([
                    html.P('Open Access Journal'),
                    html.Div(id='content-oaj', style={'display': 'none'}),
                    html.Div(id='lottie-content-oaj')
                ], style={'textAlign': 'center',
                          'box-shadow': 'rgba(0, 0, 0, 0.3) 0px 19px 38px, rgba(0, 0, 0, 0.22) 0px 15px 12px',
                          'line-height': '1', 'font-size':'11px','height': '7rem'})
            ], className='mt-2'),
        ], width=2),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.P('Listed in the Directory of Open Access (DOAJ)'),
                    html.Div(id='content-doaj', style={'display': 'none'}),
                    html.Div(id='lottie-content-doaj')
                ], style={'textAlign': 'center',
                          'box-shadow': 'rgba(0, 0, 0, 0.3) 0px 19px 38px, rgba(0, 0, 0, 0.22) 0px 15px 12px',
                          'line-height': '1', 'font-size':'11px','height': '7rem'})
            ]),
            dbc.Card([
                dbc.CardBody([
                    html.P('Present on International Standard Serial Number (ISSN) portal'),
                    html.Div(id='content-issn', style={'display': 'none'}),
                     html.Div(id='lottie-content-issn')
                ], style={'textAlign': 'center',
                          'box-shadow': 'rgba(0, 0, 0, 0.3) 0px 19px 38px, rgba(0, 0, 0, 0.22) 0px 15px 12px',
                          'line-height': '1', 'font-size':'11px','height': '7rem'})
            ], className='mt-2'),
        ], width=3),

        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.P('Publisher is a member of Committee on publication Ethics (COPE)'),
                    html.Div(id='content-cope', style={'display': 'none'}),
                    html.Div(id='lottie-content-cope')
                ], style={'textAlign': 'center',
                          'box-shadow': 'rgba(0, 0, 0, 0.3) 0px 19px 38px, rgba(0, 0, 0, 0.22) 0px 15px 12px',
                          'line-height': '1', 'font-size':'11px','height': '7rem'})
            ]),
            dbc.Card([
                dbc.CardBody([
                    html.P('Online Publisher based in Africa'),
                    html.Div(id='content-based-in-africa', style={'display': 'none'}),
                    html.Div(id='lottie-content-based-in-africa')
                ], style={'textAlign': 'center',
                          'box-shadow': 'rgba(0, 0, 0, 0.3) 0px 19px 38px, rgba(0, 0, 0, 0.22) 0px 15px 12px',
                          'line-height': '1', 'font-size':'11px','height': '7rem'})
            ], className='mt-2'),
        ], width=3),



    ], className='mb-2 mt-2'),
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    # dcc.Graph(id='line-chart', figure={}),
                ])
            ]),
        ], width=6),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    #                     dcc.Graph(id='bar-chart', figure={}),
                ])
            ]),
        ], width=6),
    ], className='mb-2'),
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardHeader('Select the options below to see journals that meet your criteria'),
                dbc.CardBody([
                    html.H6('OPTIONS'),
                    html.H5(id='', children="_____________"),

                dcc.Checklist(
                            options=[
                                {'label': ' African Journal Online (AJOL)', 'value': 'African Journal Online (AJOL)'},
                                {'label': ' SABINET Journal repository', 'value': 'SABINET Journal repository'},
                                {'label': ' Indexed on Google Scholar', 'value': 'Indexed on Google Scholar'},
                                {'label': ' Indexed on Scopus', 'value': 'Indexed on Scopus'},
                                {'label': ' Indexed on at least one platform', 'value': 'Indexed on at least one platform'},
                                {'label': ' Open Access Journal', 'value': 'Open Access Journal'},
                                {'label': ' Journal listed in the Directory of Open Access (DOAJ)', 'value': 'Journal listed in the Directory of Open Access (DOAJ)'},
                                {'label': ' Present on International Standard Serial Number (ISSN) portal', 'value': 'Present on International Standard Serial Number (ISSN) portal'},
                                {'label': ' The publisher is a member of Committee on Publication Ethics (COPE)', 'value': 'The publisher is a member of Committee on publication Ethics (COPE)'},
                                {'label': ' Online publisher based in Africa', 'value': 'Online publisher based in Africa'},
                                {'label': " Hosted on INASP's Journal online", 'value': 'Hosted on INASP\'S Journal online'},
                            ],
                            id='checklist-id',
                            style={'textAlign': 'left', 'margin-bottom': '10px', 'font-size':'10px'},
                            value=[],  # Set the initial value of the checklist
                        ),

                        dcc.Store(id='selected-values-store')

                ], style={'textAlign': 'center',
                          'box-shadow': 'rgba(0, 0, 0, 0.3) 0px 19px 38px, rgba(0, 0, 0, 0.22) 0px 15px 12px'}
                          )

            ], className='mt-2', style={'height': '23.5rem'})

        ], width=5),
        dbc.Col([
            dbc.Card([
                dbc.CardHeader('List of journals that met your criteria'),

                dbc.CardBody(
                    html.Div(
                        id='output',
                        style={
                            'height': '19rem',
                            'overflowY': 'auto',
                            'font-family': 'sans-serif',
                            'font-size': '11px',
                            'line-height': '1'

                        },
                        children=[
                            # Your table code goes here
                        ]
                    ),
                    style={'text-align': 'left', 'margin-top':'2', 'font-family': 'sans-serif',
                          'box-shadow': 'rgba(0, 0, 0, 0.3) 0px 19px 38px, rgba(0, 0, 0, 0.22) 0px 15px 12px'}

                )
            ] , className='mt-2')

        ], width=7),
        dbc.Row([
            dbc.Col([
                dbc.Card([
                    dbc.CardHeader('List of journals that met your criteria'),
                    dbc.CardBody([
                        #                     dcc.Graph(id='pie-chart', figure={}),
                    ])
                ]),

            ],width=6),
            dbc.Col([
                dbc.Card([
                    dbc.CardHeader('List of journals that met your criteria'),
                    dbc.CardBody([
                        #                     dcc.Graph(id='pie-chart', figure={}),
                    ])
                ]),

            ], width=6),
            ], className='mb-2, mt-2'),

            dbc.Row([
            dbc.Col([
                dbc.Card([
                    dbc.CardHeader('List of journals that met your criteria'),
                    dbc.CardBody([
                        #                     dcc.Graph(id='pie-chart', figure={}),
                    ])
                ]),
            ],width=6),
            dbc.Col([
                dbc.Card([
                    dbc.CardHeader('List of journals that met your criteria'),
                    dbc.CardBody([
                        #                     dcc.Graph(id='pie-chart', figure={}),
                    ])
                ]),

            ], width=6)
            ], className='mb-2, mt-2'),
            dbc.Row([
                dbc.Col([
                    dbc.Card([
                        dbc.CardHeader('List of journals that met your criteria'),
                        dbc.CardBody([
                            #                     dcc.Graph(id='pie-chart', figure={}),
                        ])
                    ]),
                ], width=6),
                dbc.Col([
                    dbc.Card([
                        dbc.CardHeader('List of journals that met your criteria'),
                        dbc.CardBody([
                            #                     dcc.Graph(id='pie-chart', figure={}),
                        ])
                    ]),

                ], width=6)
            ], className='mb-2, mt-2'),
        dbc.Row([
            dbc.Col([
                dbc.Card([
                    dbc.CardHeader('List of journals that met your criteria'),
                    dbc.CardBody([
                        #                     dcc.Graph(id='pie-chart', figure={}),
                    ])
                ]),
            ], width=6),
            dbc.Col([
                dbc.Card([
                    dbc.CardHeader('List of journals that met your criteria'),
                    dbc.CardBody([
                        #                     dcc.Graph(id='pie-chart', figure={}),
                    ])
                ]),

            ], width=6)
        ], className='mb-2, mt-2')
    ], className='mb-2'),
], fluid=False)


# Updating selected Journal
@app.callback(
    Output(component_id='content-total', component_property='children'),
    Output(component_id='content-platform', component_property='children'),
    Output(component_id='content-google-scholar', component_property='children'),
    Output(component_id='content-scopus', component_property='children'),
    Output(component_id='content-one-platform', component_property='children'),
    Output(component_id='content-oaj', component_property='children'),
    Output(component_id='content-doaj', component_property='children'),
    Output(component_id='content-issn', component_property='children'),
    Output(component_id='content-cope', component_property='children'),
    Output(component_id='content-based-in-africa', component_property='children'),
    Output(component_id='content-based-inasp', component_property='children'),

    Input(component_id='dropdown-id', component_property='value')
)
def update_output_div(journal):
    data_copy = data.copy()
    df = data_copy.loc[data_copy['Journal tittle'] == journal]
    total = len(data_copy)
    platform = df['Platform']
    google_scholar = df['Indexed on Google Scholar']
    scopus = df['Indexed on Scopus']
    one_platform = df['Indexed on at least one platform']
    oaj = df['Open Access Journal']
    doaj = df['Journal listed in the Directory of Open Access (DOAJ)']
    issn = df['Present on International Standard Serial Number (ISSN) portal']
    cope = df['The publisher is a member of Committee on publication Ethics (COPE)']
    based_in_africa = df['Online publisher based in Africa']
    inasp = df['Hosted on INASP\'S Journal online']

    return total,platform, google_scholar, scopus, one_platform, oaj, doaj, issn, cope, based_in_africa, inasp


@app.callback(
    Output('lottie-content-google-scholar', 'children'),
    [Input('content-google-scholar', 'children')]
)
def update_lottie(value):
    if (len(value) > 0):
        if value[0] == 0:
            return (
                Lottie(options=options, width="50px", height="50px", url=no_url)
            )
        elif value[0] == 1:
            return (
                Lottie(options=options, width="50px", height="50px", url=yes_url)
            )
        else:
            return html.Div()  # Return an empty div if the value is not 0 or 1
@app.callback(
    Output('lottie-content-scopus', 'children'),
    [Input('content-scopus', 'children')]
)
def update_lottie(value):
    if (len(value) > 0):
        if value[0] == 0:
            return (
                Lottie(options=options, width="50px", height="50px", url=no_url)
            )
        elif value[0] == 1:
            return (
                Lottie(options=options, width="50px", height="50px", url=yes_url)
            )
        else:
            return html.Div()  # Return an empty div if the value is not 0 or 1
@app.callback(
    Output('lottie-content-one-platform', 'children'),
    [Input('content-one-platform', 'children')]
)
def update_lottie(value):
    if (len(value) > 0):
        if value[0] == 0:
            return (
                Lottie(options=options, width="50px", height="50px", url=no_url)
            )
        elif value[0] == 1:
            return (
                Lottie(options=options, width="50px", height="50px", url=yes_url)
            )
        else:
            return html.Div()  # Return an empty div if the value is not 0 or 1
@app.callback(
    Output('lottie-content-oaj', 'children'),
    [Input('content-oaj', 'children')]
)
def update_lottie(value):
    if (len(value) > 0):
        if value[0] == 0:
            return (
                Lottie(options=options, width="50px", height="50px", url=no_url)
            )
        elif value[0] == 1:
            return (
                Lottie(options=options, width="50px", height="50px", url=yes_url)
            )
        else:
            return html.Div()  # Return an empty div if the value is not 0 or 1
@app.callback(
    Output('lottie-content-doaj', 'children'),
    [Input('content-doaj', 'children')]
)
def update_lottie(value):
    if (len(value) > 0):
        if value[0] == 0:
            return (
                Lottie(options=options, width="50px", height="50px", url=no_url)
            )
        elif value[0] == 1:
            return (
                Lottie(options=options, width="50px", height="50px", url=yes_url)
            )
        else:
            return html.Div()  # Return an empty div if the value is not 0 or 1
@app.callback(
    Output('lottie-content-issn', 'children'),
    [Input('content-issn', 'children')]
)
def update_lottie(value):
    if (len(value) > 0):
        if value[0] == 0:
            return (
                Lottie(options=options, width="50px", height="50px", url=no_url)
            )
        elif value[0] == 1:
            return (
                Lottie(options=options, width="50px", height="50px", url=yes_url)
            )
        else:
            return html.Div()  # Return an empty div if the value is not 0 or 1
@app.callback(
    Output('lottie-content-cope', 'children'),
    [Input('content-cope', 'children')]
)
def update_lottie(value):
    if (len(value) > 0):
        if value[0] == 0:
            return (
                Lottie(options=options, width="50px", height="50px", url=no_url)
            )
        elif value[0] == 1:
            return (
                Lottie(options=options, width="50px", height="50px", url=yes_url)
            )
        else:
            return html.Div()  # Return an empty div if the value is not 0 or 1
@app.callback(
    Output('lottie-content-based-in-africa', 'children'),
    [Input('content-based-in-africa', 'children')]
)
def update_lottie(value):
    if (len(value) > 0):
        if value[0] == 0:
            return (
                Lottie(options=options, width="50px", height="50px", url=no_url)
            )
        elif value[0] == 1:
            return (
                Lottie(options=options, width="50px", height="50px", url=yes_url)
            )
        else:
            return html.Div()  # Return an empty div if the value is not 0 or 1
@app.callback(
    Output('lottie-content-based-inasp', 'children'),
    [Input('content-based-inasp', 'children')]
)
def update_lottie(value):
    if (len(value) > 0):
        if value[0] == 0:
            return (
                Lottie(options=options, width="50px", height="50px", url=no_url)
            )
        elif value[0] == 1:
            return (
                Lottie(options=options, width="50px", height="50px", url=yes_url)
            )
        else:
            return html.Div()  # Return an empty div if the value is not 0 or 1

# @app.callback(
#     Input(component_id='input-google-scholar', component_property='value'),
#     Input(component_id='input-scopus', component_property='value'),
#     Input(component_id='input-one-platform', component_property='value'),
#     Input(component_id='input-oaj', component_property='value'),
#     Input(component_id='input-doaj', component_property='value'),
#     Input(component_id='input-issn', component_property='value'),
#     Input(component_id='input-cope', component_property='value'),
#     Input(component_id='input-based-in-africa', component_property='value'),
#     Input(component_id='input-based-inasp', component_property='value'),
#
#     Input(component_id='dropdown-id', component_property='children')
# )
def filter_data(platform,google_scholar, scopus, one_platform, oaj, doaj, issn, cope, based_in_africa, inasp):
    df = data.copy()
    final_df = df.loc[(df['Platform']==platform) & (df['Indexed on Google Scholar']==google_scholar) & (df['Indexed on Scopus']==scopus) &
                     (df['Indexed on at least one platform']==one_platform)  & (df['Open Access Journal']==oaj) &
                      (df['Journal listed in the Directory of Open Access (DOAJ)']==doaj) & (df['Present on International Standard Serial Number (ISSN) portal']==issn) &
                      (df['The publisher is a member of Committee on publication Ethics (COPE)']==cope) & (df['Online publisher based in Africa']==based_in_africa) &
                      (df['Hosted on INASP\'S Journal online']==inasp)
                     ]
    print(final_df)
    return final_df['Journal tittle']

def fil(cols):
    dataf=data.copy()
    if len(cols)>0:
        for i in cols:
            dataf = dataf.loc[dataf[i]==1]
            fin_df = pd.DataFrame(dataf, columns = ['Journal tittle'])
            print(fin_df)
        return fin_df
    else:
        fin_df = pd.DataFrame(dataf, columns=['Journal tittle'])
        return fin_df

@app.callback(
    Output('selected-values-store', 'data'),
    [Input('checklist-id', 'value')]
)
def save_selected_values(selected_values):
    return selected_values


@app.callback(
    Output('output', 'children'),
    [Input('selected-values-store', 'data')]
)
def display_selected_values(selected_values):
    if selected_values is not None:
        data_df = fil(selected_values)
        data_df['Number'] = range(1, len(data_df) + 1)
        num = len(data_df)

        # Swap the columns in the DataFrame
        data_df = data_df[['Number'] + list(data_df.columns[:-1])]

        data_table = dash_table.DataTable(
            id='data-table',
            columns=[{"name": col, "id": col} for col in data_df.columns],
            data=data_df.to_dict('records'),
            style_table={ 'font-family': 'sans-serif'},
            style_cell_conditional=[
                {'if': {'column_id': 'Date'}, 'textAlign': 'left'},
                {'if': {'column_id': 'Region'}, 'textAlign': 'left'}
            ],
            style_data={
                'color': 'black',
                'backgroundColor': 'white',
                'textAlign': 'left',
                'font-family': 'sans-serif',
            },
            style_data_conditional=[
                {'if': {'row_index': 'odd'}, 'backgroundColor': 'rgb(220, 220, 220)'}
            ],
            style_header={
                'backgroundColor': 'rgb(210, 210, 210)',
                'color': 'black',
                'fontWeight': 'bold',
                'textAlign': 'left',
                'font-family': 'sans-serif',
            }
        )

        return html.Div(data_table)
    else:
        return html.Div("No values selected")


if __name__=='__main__':
    app.run_server(debug=False, port=8001)