from dash import html, dcc, register_page, Input, Output, State, callback
import dash_bootstrap_components as dbc
from sanx.web import table, search
from sanx.db import get_users


register_page(
    __name__,
    path="/dataforms",
    title="Data Forms Input Page",
)


tab1_content = dbc.Card(
    dbc.CardBody(
        [
            html.P("This is tab 1!", className="card-text"),
            dbc.Button("Click here", color="success"),
        ]
    ),
    className="mt-3",
)

tab2_content = dbc.Card(
    dbc.CardBody(
        [
            html.P("This is tab 2!", className="card-text"),
            dbc.Button("Don't click here", color="danger"),
        ]
    ),
    className="mt-3",
)

hr = html.Div(style={"height": "1em"})


user_form = dbc.Form(
    [
        dbc.Row(
            [
                dbc.Label("Full Name", width="auto"),
                dbc.Col(
                    dbc.Input(type="text", placeholder="Full Name"),
                    # className="me-3",
                ),
                dbc.Label("Employee ID", width="auto"),
                dbc.Col(
                    dbc.Input(type="text", placeholder="Employee ID"),
                    # className="me-3",
                ),
            ],
            className="g-2",
        ),
        hr,
        dbc.Row(
            [
                dbc.Label("Email", width="auto"),
                dbc.Col(
                    dbc.Input(type="email", placeholder="Enter email"),
                    # className="me-3",
                ),
                dbc.Label("Password", width="auto"),
                dbc.Col(
                    dbc.Input(type="password", placeholder="Enter password"),
                    # className="me-3",
                ),
            ],
            className="g-2",
        ),
        hr,
        dbc.Col(
            dbc.Button("Submit User", color="primary", style={"width": "100%"}),
            width=12,
            style={
                "textAlign": "center",
            },
        ),
    ]
)

view_table_collapse = html.Div(
    [
        dbc.Button(
            "View User Table",
            id="collapse-button",
            className="mb-3",
            color="primary",
            n_clicks=0,
        ),
        dbc.Collapse(
            dbc.Card(dbc.CardBody("This content is hidden in the collapse")),
            id="collapse",
            is_open=True,
        ),
    ]
)

user_tab = html.Div(
    dbc.Accordion(
        [
            dbc.AccordionItem(
                user_form,
                title="Add User",
            ),
            dbc.AccordionItem(
                html.Div(
                    [
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
                    ]
                ),
                title="View Users",
            ),
        ],
        always_open=True,
    )
)


tabs = dbc.Tabs(
    [
        dbc.Tab(user_tab, label="Admin", style={"margin-top": "2em"}, disabled=False),
        dbc.Tab(tab1_content, label="Tasks"),
        dbc.Tab(tab2_content, label="Others", disabled=True),
    ]
)


layout = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H4(
                            "Data Forms",
                            style={
                                "textAlign": "center",
                                # "line-height": "2.0em",
                                # "padding-top": "2.0em",
                            },
                        )
                    ]
                )
            ]
        ),
        dbc.Container(
            tabs,
            fluid=True,
            className="py-3",
        ),
    ],
    className="p-3 rounded-3",  # bg-light
    style={
        "margin-top": "2em",
    },
)


# @callback(
#     Output("collapse", "is_open"),
#     [Input("collapse-button", "n_clicks")],
#     [State("collapse", "is_open")],
# )
# def toggle_collapse(n, is_open):
#     if n:
#         return not is_open
#     return is_open
