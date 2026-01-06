from dash import html, dcc

def time_layout(months, offices):
    return html.Div(
        [
            # 🔹 Title + Nav
            html.Div(
                [
                    html.H3("Time-Based Performance Analysis", className="page-title"),
                    html.Div(
                        [
                            html.Button("Home", id="nav-home", className="nav-btn"),
                            html.Button("Time Analysis", id="nav-time", className="nav-btn"),
                            html.Button("Problem Analysis", id="nav-problem", className="nav-btn"),
                            html.Button("SLA", id="nav-bonus", className="nav-btn")
                        ],
                        className="nav-buttons",
                    ),
                ],
                className="page-header",
            ),

            # 🔹 Filters
            html.Div(
                html.Div(
                    [
                        html.Div(
                            [
                                html.Label("Office"),
                                dcc.Dropdown(
                                    id="time-office-filter",
                                    options=[{"label": "All Offices", "value": "ALL"}]
                                    + [{"label": o, "value": o} for o in offices],
                                    value="ALL",
                                    clearable=False,
                                ),
                            ],
                            className="filter-box",
                        ),
                        html.Div(
                            [
                                html.Label("Month"),
                                dcc.Dropdown(
                                    id="time-month-filter",
                                    options=[{"label": "All Months", "value": "ALL"}]
                                    + [{"label": m, "value": m} for m in months],
                                    value="ALL",
                                    clearable=False,
                                ),
                            ],
                            className="filter-box",
                        ),
                    ],
                    className="filter-row",
                ),
                className="filter-card",
            ),

            # 🔹 Charts
            html.Div(
                [
                    html.Div(dcc.Graph(id="response-chart"), className="chart-card"),
                    html.Div(dcc.Graph(id="resolution-chart"), className="chart-card"),
                ],
                className="chart-row",
            ),
        ],
        className="page-card",
    )