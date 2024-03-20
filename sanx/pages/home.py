import dash
from dash import html
import dash_bootstrap_components as dbc
from sanx.web import logo_img
from sanx.paths import RESOURCES_DIR

from PIL import Image

dashboard_img = Image.open(RESOURCES_DIR / "card_images" / "dashboard.jpg")
dataforms_img = Image.open(RESOURCES_DIR / "card_images" / "datainput.jpg")
settings_img = Image.open(RESOURCES_DIR / "card_images" / "settings.jpg")


dash.register_page(__name__, path="/", title="Application Home")


def get_card(title="Card title", link="", img="", desc=""):
    return dbc.Card(
        [
            dbc.CardImg(src=img if img else logo_img, top=True),
            dbc.CardBody(
                [
                    html.H4(title, className="card-title"),
                    html.P(
                        "Some quick example text to build on the card title and "
                        "make up the bulk of the card's content.",
                        className="card-text",
                    ),
                    dbc.Button(f"Go to {title}", color="primary", href=f"/{link}"),
                ]
            ),
        ],
        style={"width": "30rem"},
    )


layout = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H1(
                            "Application Tracker",
                            style={
                                "textAlign": "center",
                                "line-height": "3.0em",
                                # "padding-top": "2.0em",
                            },
                        )
                    ]
                )
            ]
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.Div(
                            get_card(
                                title="Data Forms", link="dataforms", img=dataforms_img
                            ),
                            className="d-flex justify-content-center",
                            # style={"width": "100%", "background-color": "green"},
                        ),
                    ],
                    width=4,
                ),
                dbc.Col(
                    [
                        html.Div(
                            get_card(
                                title="Dashboard", link="dashboard", img=dashboard_img
                            ),
                            className="d-flex justify-content-center",
                            # style={"width": "100%", "background-color": "green"},
                        ),
                    ],
                    width=4,
                ),
                dbc.Col(
                    [
                        html.Div(
                            get_card(
                                title="Settings", link="settings", img=settings_img
                            ),
                            className="d-flex justify-content-center",
                            # style={"width": "100%", "background-color": "green"},
                        ),
                    ],
                    width=4,
                ),
            ],
            style={
                # "padding-top": "100px",
                "padding-left": "80px",
                "padding-right": "80px",
            },
        ),
    ]
)
