import pandas as pd
from dash import html
import dash_bootstrap_components as dbc


def from_dataframe(df: pd.DataFrame) -> dbc.Table:
    table_header = [html.Thead(html.Tr([html.Th(col) for col in df.columns]))]
    rows = [
        html.Tr([html.Td(row[col]) for col in df.columns]) for idx, row in df.iterrows()
    ]
    table_body = [html.Tbody(rows)]
    return dbc.Table(table_header + table_body, bordered=True)
