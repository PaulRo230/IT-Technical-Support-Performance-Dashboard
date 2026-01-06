from dash import html

def header():
    return html.Div(
        [
            html.Div(
                [
                    html.Button("Home", id="nav-home", className="nav-btn"),
                    html.Button("Time Analysis", id="nav-time", className="nav-btn"),
                    html.Button("Problem Analysis", id="nav-problem", className="nav-btn"),
                    html.Button("SLA", id="nav-bonus", className="nav-btn")
                ],
                className="nav-buttons",
            )
        ],
        style={"display": "none"},  # header kept for nav IDs, but hidden
    )