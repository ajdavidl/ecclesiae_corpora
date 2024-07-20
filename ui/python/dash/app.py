from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder_unfiltered.csv')

df_pt = pd.read_json('../../../papae_verba/pt.json').T
df_en = pd.read_json('../../../papae_verba/en.json').T
citations = df_pt.index

app = Dash()

app.layout = html.Div([
    html.H1(children='Papae verba', style={'textAlign':'center'}),
    dcc.Dropdown(['pt','en'], 'pt', id='dropdown-language'),
    dcc.Dropdown(citations, citations[0], id='dropdown-citations'),
    html.H2(id="textarea-evangelho-title", children='Evangelho'),
    html.Div(id="textarea-evangelho", children=[]),
    html.H2(id="textarea-homilia-title", children='Homilia'),
    html.Div(id="textarea-homilia", children=[])
])


@callback(
    Output('dropdown-citations','options'),
    Input('dropdown-language', 'value')
)
def update_language_dropdown(value):
    if value == 'pt':
        return df_pt.index.sort_values()
    elif value == 'en':
        return df_en.index.sort_values()
    else:
        return df_pt.index.sort_values()

@callback(
    Output('textarea-evangelho','children'),
    [Input('dropdown-language', 'value'),
    Input('dropdown-citations', 'value')]
)
def update_evangelho(dd1, dd2):
    print(dd1)
    print(dd2)
    if dd1 == 'pt':
        return df_pt.loc[dd2,'evangelho']
    elif dd1 == 'en':
        return df_en.loc[dd2,'evangelho']
    else:
        return df_pt.loc[dd2,'evangelho']


@callback(
    Output('textarea-homilia','children'),
    [Input('dropdown-language', 'value'),
    Input('dropdown-citations', 'value')]
)
def update_homilia(dd1, dd2):
    print(dd1)
    print(dd2)
    if dd1 == 'pt':
        h = df_pt.loc[dd2,'homilias']
        return '<br><br>'.join(h)
    elif dd1 == 'en':
        h = df_en.loc[dd2,'homilias']
        return '<br><br>'.join(h)
    else:
        h = df_pt.loc[dd2,'homilias']
        return '<br><br>'.join(h)

if __name__ == '__main__':
    app.run(debug=True)
