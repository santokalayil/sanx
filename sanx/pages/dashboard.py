import dash
from dash import html, dcc, Input, Output, Dash, callback
import dash_bootstrap_components as dbc
import plotly.express as px
from dash_extensions import Mermaid
from sanx.web import table, search
from sanx.db import get_hero_rows

dash.register_page(
    __name__,
    path="/dashboard",
    title="Our Analytics Dashboard",
)

df = px.data.gapminder().query("year == 2007").query("continent == 'Europe'")
df.loc[df["pop"] < 2.0e6, "country"] = (
    "Other countries"  # Represent only large countries
)
fig = px.pie(
    df, values="pop", names="country", title="Population of European continent"
)
fig.update_layout()


layout = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H1(
                            children="Data Dashboard",
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
                    value="Spider-Boy",
                    placeholder="Search",
                    style=search.search_box_style,
                    id="search_text",
                ),
                dcc.Markdown(children="", id="input_text_shower"),
            ]
        ),
        dbc.Row(
            [
                dbc.Col([], id="table_row", width=12),
            ],
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        dcc.Graph(figure=fig),
                    ],
                    width=6,
                ),
                dbc.Col(
                    [
                        # Mermaid(
                        #     chart="""
                        #         graph TD;
                        #         A-->B;
                        #         A-->C;
                        #         B-->D;
                        #         C-->D;
                        #         """
                        # )
                    ]
                ),
            ],
        ),
    ]
)


@callback(
    Output("input_text_shower", component_property="children"),
    Input("search_text", component_property="value"),
)
def update_graph(text):
    return ("Results for " + text) if text else ""


@callback(
    Output("table_row", component_property="children"),
    Input("search_text", component_property="value"),
)
def update_table(text):
    cols = ["id", "name", "secret_name", "age"]
    return table.from_dataframe(get_hero_rows(text, cols))
