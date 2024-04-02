



import dash
from dash import dcc, html
from dash.dependencies import Input, Output
from pathlib import Path

app = dash.Dash(__name__)

# Define the layout
app.layout = html.Div([
    html.H1("Real-time Log Viewer"),
    html.Div(
        id='log-output',
        style={
            'height': '400px',  # Set fixed height
            'overflowY': 'scroll',  # Enable vertical scrolling
            'background-color': 'black',  # Set background color
            'color': 'white',  # Set text color
            'padding': '10px',  # Add padding for better appearance
            'scrollbar-width': 'thin',  # Set scrollbar width
            'scrollbar-color': 'gray black'  # Set scrollbar color
        },
        children=[]
    ),
    dcc.Interval(
        id='interval-component',
        interval=1000,  # in milliseconds
        n_intervals=0
    )
])

# Function to read the log file and return its content
def read_log_file(file_path):
    with open(file_path, 'r') as file:
        return file.readlines()

# Callback to update log content every 1 second
@app.callback(
    Output('log-output', 'children'),
    [Input('interval-component', 'n_intervals')]
)
def update_log(n):
    log_folder = Path(__file__).parent
    log_file_path = log_folder / "t.log"
    lines = read_log_file(log_file_path)
    return [html.Pre(line) for line in lines]

if __name__ == '__main__':
    app.run_server(debug=True)




# import dash
# from dash import dcc, html
# from dash.dependencies import Input, Output
# from pathlib import Path

# app = dash.Dash(__name__)

# # Define the layout
# app.layout = html.Div([
#     html.H1("Real-time Log Viewer"),
#     html.Div(
#         id='log-output',
#         style={
#             'height': '400px',  # Set fixed height
#             'overflowY': 'scroll',  # Enable vertical scrolling
#             'background-color': 'black',  # Set background color
#             'color': 'white'  # Set text color
#         }
#     ),
#     dcc.Interval(
#         id='interval-component',
#         interval=1000,  # in milliseconds
#         n_intervals=0
#     )
# ])

# # Function to read the log file and return its content
# def read_log_file(file_path):
#     with open(file_path, 'r') as file:
#         return file.readlines()

# # Callback to update log content every 1 second
# @app.callback(
#     Output('log-output', 'children'),
#     [Input('interval-component', 'n_intervals')]
# )
# def update_log(n):
#     log_folder = Path(__file__).parent
#     log_file_path = log_folder / "t.log"
#     lines = read_log_file(log_file_path)
#     return [html.Pre(line) for line in lines]

# if __name__ == '__main__':
#     app.run_server(debug=True)



# import dash
# from dash import dcc, html
# from dash.dependencies import Input, Output
# from pathlib import Path

# app = dash.Dash(__name__)

# # Define the layout
# app.layout = html.Div([
#     html.H1("Real-time Log Viewer"),
#     html.Div(id='log-output'),
#     dcc.Interval(
#         id='interval-component',
#         interval=1000,  # in milliseconds
#         n_intervals=0
#     )
# ])

# # Function to read the log file and return its content
# def read_log_file(file_path):
#     with open(file_path, 'r') as file:
#         return file.readlines()

# # Callback to update log content every 1 second
# @app.callback(
#     Output('log-output', 'children'),
#     [Input('interval-component', 'n_intervals')]
# )
# def update_log(n):
#     log_folder = Path(__file__).parent
#     log_file_path = log_folder / "t.log"
#     lines = read_log_file(log_file_path)
#     # return [html.Pre(line) for line in lines]
#     return [html.Pre(line) for line in lines]

# if __name__ == '__main__':
#     app.run_server(debug=True)
