import dash                              # pip install dash
from dash import html
from dash import dcc
from dash.dependencies import Output, Input
from dash_extensions import Lottie       # pip install dash-extensions
import dash_bootstrap_components as dbc  # pip install dash-bootstrap-components
import plotly.express as px              # pip install plotly
import pandas as pd                      # pip install pandas
from datetime import date
import calendar
from wordcloud import WordCloud
from dash import dependencies

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
            dbc.Col([
                dbc.Card([
                    dbc.CardHeader('Total Number of Journals Considered', style={'font-family': 'Inter'}),
                    dbc.CardBody([
                        html.P('12345'),
                        html.P('See full list here'),

                    ])
                ]),
            ], width=3),

        ], width=12),

    ], className='mb-2 mt-2'),

    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardHeader('Select the Journal from the dropdown below to see its details', style={'font-family': 'Helevitica'}),
                dbc.CardBody([
                    html.H6('Journal'),
                    html.H2(id='', children="dropdown here")
                ], style={'textAlign': 'center', 'box-shadow': 'rgba(0, 0, 0, 0.4) 0px 30px 90px'})
            ],style={'height': '100%'} ),

        ], width=4),
        dbc.Col([
            dbc.Card([
                dbc.CardHeader(Lottie(options='options', width="32%", height="32%", url='url_companies')),
                dbc.CardBody([
                    html.H6('Companies'),
                    html.H2(id='', children="000", style={'color': 'black'})
                ], style={'textAlign': 'center', 'color': 'red',
                          'box-shadow': 'rgba(0, 0, 0, 0.3) 0px 19px 38px, rgba(0, 0, 0, 0.22) 0px 15px 12px','height': '5rem'})
            ]),
            dbc.Card([
                    dbc.CardHeader(Lottie(options='options', width="32%", height="32%", url='url_companies')),
                    dbc.CardBody([
                        html.H6('Companies'),
                        html.H2(id='', children="000", style={'color': 'black'})
                    ], style={'textAlign': 'center', 'color': 'red',
                          'box-shadow': 'rgba(0, 0, 0, 0.3) 0px 19px 38px, rgba(0, 0, 0, 0.22) 0px 15px 12px','height': '5rem'})
                ], className = 'mt-2'),
            dbc.Card([
                dbc.CardHeader(Lottie(options='options', width="53%", height="53%", url='url_msg_out')),
                dbc.CardBody([
                    html.H6('Invites sent'),
                    html.H2(id='', children="000")
                ], style={'textAlign': 'center', 'color': 'red',
                          'box-shadow': 'rgba(0, 0, 0, 0.3) 0px 19px 38px, rgba(0, 0, 0, 0.22) 0px 15px 12px','height': '5rem'})
            ],className='mt-2'),
            ], width=2),
        dbc.Col([
            dbc.Card([
                dbc.CardHeader(Lottie(options='options', width="25%", height="25%", url='url_msg_in')),
                dbc.CardBody([
                    html.H6('Invites received'),
                    html.H2(id='', children="000")
                ], style={'textAlign': 'center', 'color': 'red',
                          'box-shadow': 'rgba(0, 0, 0, 0.3) 0px 19px 38px, rgba(0, 0, 0, 0.22) 0px 15px 12px','height': '5rem'})
            ]),
            dbc.Card([
                dbc.CardHeader(Lottie(options='options', width="25%", height="25%", url='url_msg_in')),
                dbc.CardBody([
                    html.H6('Invites received'),
                    html.H2(id='', children="000")
                ], style={'textAlign': 'center', 'color': 'red',
                          'box-shadow': 'rgba(0, 0, 0, 0.3) 0px 19px 38px, rgba(0, 0, 0, 0.22) 0px 15px 12px','height': '5rem'})
            ], className='mt-2'),
            dbc.Card([
                dbc.CardHeader(Lottie(options='options', width="53%", height="53%", url='url_msg_out')),
                dbc.CardBody([
                    html.H6('Invites sent'),
                    html.H2(id='', children="000")
                ], style={'textAlign': 'center', 'color': 'red',
                          'box-shadow': 'rgba(0, 0, 0, 0.3) 0px 19px 38px, rgba(0, 0, 0, 0.22) 0px 15px 12px','height': '5rem'})
            ],className='mt-2'),
        ], width=2),

        dbc.Col([
            dbc.Card([
                dbc.CardHeader(Lottie(options='options', width="53%", height="53%", url='url_msg_out')),
                dbc.CardBody([
                    html.H6('Invites sent'),
                    html.H2(id='', children="000")
                ], style={'textAlign': 'center', 'color': 'red',
                          'box-shadow': 'rgba(0, 0, 0, 0.3) 0px 19px 38px, rgba(0, 0, 0, 0.22) 0px 15px 12px','height': '5rem'})
            ]),
            dbc.Card([
                dbc.CardHeader(Lottie(options='options', width="53%", height="53%", url='url_msg_out')),
                dbc.CardBody([
                    html.H6('Invites sent'),
                    html.H2(id='', children="000")
                ], style={'textAlign': 'center', 'color': 'red',
                          'box-shadow': 'rgba(0, 0, 0, 0.3) 0px 19px 38px, rgba(0, 0, 0, 0.22) 0px 15px 12px','height': '5rem'})
            ],className='mt-2'),
            dbc.Card([
                dbc.CardHeader(Lottie(options='options', width="53%", height="53%", url='url_msg_out')),
                dbc.CardBody([
                    html.H6('Invites sent'),
                    html.H2(id='', children="000")
                ], style={'textAlign': 'center', 'color': 'red',
                          'box-shadow': 'rgba(0, 0, 0, 0.3) 0px 19px 38px, rgba(0, 0, 0, 0.22) 0px 15px 12px','height': '5rem'})
            ],className='mt-2'),
        ], width=2),
        dbc.Col([
            dbc.Card([
                dbc.CardHeader(Lottie(options='options', width="25%", height="25%", url='url_reactions')),
                dbc.CardBody([
                    html.H6('Reactions'),
                    html.H2(id='', children="000")
                ], style={'textAlign': 'center', 'color': 'red',
                          'box-shadow': 'rgba(0, 0, 0, 0.3) 0px 19px 38px, rgba(0, 0, 0, 0.22) 0px 15px 12px','height': '5rem'})
            ]),
            dbc.Card([
                dbc.CardHeader(Lottie(options='options', width="53%", height="53%", url='url_msg_out')),
                dbc.CardBody([
                    html.H6('Invites sent'),
                    html.H2(id='', children="000")
                ], style={'textAlign': 'center', 'color': 'red',
                          'box-shadow': 'rgba(0, 0, 0, 0.3) 0px 19px 38px, rgba(0, 0, 0, 0.22) 0px 15px 12px','height': '5rem'})
            ],className='mt-2'),
            dbc.Card([
                dbc.CardHeader(Lottie(options='options', width="53%", height="53%", url='url_msg_out')),
                dbc.CardBody([
                    html.H6('Invites sent'),
                    html.H2(id='', children="000")
                ], style={'textAlign': 'center', 'color': 'red',
                          'box-shadow': 'rgba(0, 0, 0, 0.3) 0px 19px 38px, rgba(0, 0, 0, 0.22) 0px 15px 12px','height': '5rem'})
            ],className='mt-2'),
        ], width=2),

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
                        [' African Journal Online (AJOL)',' SABINET Journal repository']
                        , style={'textAlign': 'left', 'margin-bottom': '5px'}
                    ),
                html.H5(id='', children="_____________"),
                    dcc.Checklist(
                        [' Indexed on Google Scholar',
                         ' Indexed on Scopus', ' Idexed on Google Scholar and Scopus',
                         ' Indexed on at least one platform', ' Open Access Journal',
                         ' Journal listed in the Directory of Open Access (DOAJ)',
                         ' Present on International Standard Serial Number (ISSN) portal',
                         ' The publisher is a member of Committee on publication Ethics (COPE)',
                         ' Online publisher based in Africa', ' Hosted on INASP\'S Journal online']
                        , style={'textAlign': 'left', 'margin-bottom': '10px'}
                    )

                ], style={'textAlign': 'center', 'color': 'red',
                          'box-shadow': 'rgba(0, 0, 0, 0.3) 0px 19px 38px, rgba(0, 0, 0, 0.22) 0px 15px 12px'}
                          )

            ], className='mt-2')

        ], width=6),
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
                dbc.CardBody([
                    #                     dcc.Graph(id='wordcloud', figure={}),
                ])
            ]),
        ], width=4),
    ], className='mb-2'),
], fluid=False)


if __name__=='__main__':
    app.run_server(debug=False, port=8001)