from dash import html, dcc

login_info_style = {
    "position": "absolute",
    "top": "20px",
    "right": "20px",
    "padding": "10px",
    "border": "2px solid #45a1b0",
    "border-radius": "10px",
    "cursor": "pointer",
}

# Define the login overlay style
login_overlay_style = {
    "position": "fixed",  # Position the overlay fixed to the viewport
    "top": "0",  # Position the overlay at the top of the viewport
    "left": "0",  # Position the overlay at the left of the viewport
    "width": "100%",  # Set the width of the overlay to cover the entire viewport
    "height": "100%",  # Set the height of the overlay to cover the entire viewport
    "background-color": "rgba(0, 0, 0, 0.5)",  # Set the background color with transparency
    "z-index": "2",  # Set a higher z-index to place the overlay above other content
}
# Define the login container style
login_container_style = {
    "position": "absolute",  # Set position to absolute
    "top": "50%",  # Position the container vertically at 50% from the top
    "left": "50%",  # Position the container horizontally at 50% from the left
    "transform": "translate(-50%, -50%)",  # Center the container
    "background-color": "#fff",  # Set the background color of the container
    "padding": "20px",  # Add padding to the container
    "border-radius": "10px",  # Add rounded corners to the container
    "z-index": "3",  # Set a higher z-index to place the container above the overlay
}

# Define the close button style
close_button_style = {
    "position": "absolute",  # Set position to absolute
    "top": "10px",  # Position the button 10px from the top
    "right": "10px",  # Position the button 10px from the right
    "background-color": "transparent",  # Set the background color to transparent
    "border": "none",  # Remove border
    "cursor": "pointer",  # Set cursor to pointer on hover
}


login_overlay_interface = html.Div(
    [
        # Hidden element to capture "Escape" key press
        # html.Div(id="escape-key", style={"display": "none"}),
        html.Div(id="login-overlay", style=login_overlay_style),
        html.Div(
            [
                # html.Button("X", id="close-button", style=close_button_style),
                html.Div(
                    [
                        html.Button(
                            "X", id="close-button", n_clicks=0, style=close_button_style
                        ),
                        html.H2("Login"),
                        dcc.Input(
                            id="username-input",
                            type="text",
                            placeholder="Username",
                        ),
                        dcc.Input(
                            id="password-input",
                            type="password",
                            placeholder="Password",
                        ),
                        html.Button("Login", id="login-button", n_clicks=0),
                        html.Div(id="login-feedback"),
                    ],
                    style=login_container_style,
                ),
            ]
        ),
    ],
    id="login-overlay-container",
    style={"display": "none"},
)
