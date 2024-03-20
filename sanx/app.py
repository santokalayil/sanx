import dash
from dash import Dash, html, dcc, Input, Output, callback, callback_context
import dash_bootstrap_components as dbc
from sanx.web import logo_img, logo_style, login

app = Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div(
    [
        html.A(html.Img(src=logo_img, style=logo_style, id="home_logo"), href="/"),
        html.Div(
            id="login-info-link",
            children=html.Div(["Logged In as Santo"], id="loginfo-container-top-right"),
            style=login.login_info_style,
        ),
        dash.page_container,
        # Hidden store to capture keydown events
        dcc.Store(id="keydown-store", data={"key": None}),
        login.login_overlay_interface,
        html.Footer(
            "Copyright © 2023 Your Company",
            style={
                "font-size": "12px",  # Decrease font size
                "position": "fixed",
                "bottom": "0",
                "width": "100%",
                "background-color": "#f8f9ff",
                "padding": "5px",  # Decrease padding
                "text-align": "center",  # Center-align text
            },
        ),
    ]
)


# @callback(
#     Output("loginfo-container-top-right"),
#     []
# )


@callback(
    Output("login-overlay-container", "style"),
    [
        Input("login-info-link", "n_clicks"),
        Input("close-button", "n_clicks"),
    ],
    prevent_initial_call=True,
)
def toggle_login_overlay(login_clicks, close_clicks):
    ctx = callback_context

    if ctx.triggered:
        triggered_id = ctx.triggered[0]["prop_id"].split(".")[0]

        if triggered_id == "login-info-link":
            return {"display": "block"}
        elif triggered_id == "close-button":
            return {"display": "none"}

    return {"display": "none"}  # Default to hiding the login overlay


# @callback(
#     Output("input_text_shower", component_property="children"),
#     Input("home_logo", component_property="value"),
# )
# def update_graph(text):
#     return ("Results for " + text) if text else ""


# app.layout = html.Div(
#     [
#         html.H1("Multi-page app with Dash Pages"),
#         html.Div(
#             [
#                 html.Div(
#                     dcc.Link(
#                         f"{page['name']} - {page['path']}", href=page["relative_path"]
#                     )
#                 )
#                 for page in dash.page_registry.values()
#             ]
#         ),
#         dash.page_container,
#     ]
# )
