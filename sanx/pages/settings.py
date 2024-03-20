import dash
from dash import html, dcc, Input, Output, Dash, callback
import dash_bootstrap_components as dbc
import plotly.express as px
from sanx.web import table, search
from sanx.db import get_users

from dash_extensions import Lottie

dash.register_page(
    __name__,
    path="/settings",
    title="Settings - Admin",
)


layout = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H1(
                            children="Settings",
                            style={
                                "textAlign": "center",
                                "line-height": "2.0em",
                            },
                        )
                    ]
                )
            ]
        ),
        dbc.Row(
            [
                # search_text := search_box,
                dcc.Input(
                    value="",
                    placeholder="Search Users",
                    style=search.search_box_style,
                    id="search_user",
                ),
                dcc.Markdown(children="", id="input_text_shower"),
            ]
        ),
        dbc.Row(
            [
                dbc.Col([], id="user_table", width=12),
            ],
        ),
        Lottie(
            options=dict(loop=True, autoplay=True),
            width="25%",
            url="https://assets6.lottiefiles.com/packages/lf20_rwwvwgka.json",
        ),
    ]
)


@callback(
    Output("user_table", component_property="children"),
    Input("search_user", component_property="value"),
)
def update_table(text):
    cols = "id", "name", "employee_id", "access_level"
    return table.from_dataframe(get_users(text, cols))
