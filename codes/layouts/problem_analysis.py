from dash import html, dcc

def problem_layout(offices, problems):
    return html.Div(
        [
            # 🔹 Title + Nav
            html.Div(
                [
                    html.H3(
                        "Problem-Based Performance Analysis",
                        className="page-title",
                    ),
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
                                html.Label("Problem Type"),
                                dcc.Dropdown(
                                    id="problem-type-filter",
                                    options=[{"label": "All Problems", "value": "ALL"}]
                                    + [{"label": p, "value": p} for p in problems],
                                    value="ALL",
                                    clearable=False,
                                ),
                            ],
                            className="filter-box",
                        ),
                        html.Div(
                            [
                                html.Label("Office"),
                                dcc.Dropdown(
                                    id="problem-office-filter",
                                    options=[{"label": "All Offices", "value": "ALL"}]
                                    + [{"label": o, "value": o} for o in offices],
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
                    html.Div(
                        dcc.Graph(id="problem-avg-resolution-chart"),
                        className="chart-card",
                    ),
                    html.Div(
                        dcc.Graph(id="problem-count-chart"),
                        className="chart-card",
                    ),
                ],
                className="chart-row",
            ),
        ],
        className="page-card",
    )