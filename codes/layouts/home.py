from dash import html, dcc

def home_layout(months=None, offices=None, problems=None):
    return html.Div(
        [
            # 🔹 Title + Nav
            html.Div(
                [
                    html.H3(
                        "IT Technical Support Performance Dashboard",
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

            # 🔹 KPI Row
            # 🔹 KPI Section
            html.Div(
                html.Div(
                    [
                        html.Div(
                            [
                                html.Div("Total Cases", className="kpi-label"),
                                html.Div(id="kpi-total-cases", className="kpi-value"),
                            ],
                            className="kpi-card",
                        ),
                        html.Div(
                            [
                                html.Div("Avg Response Time (min)", className="kpi-label"),
                                html.Div(id="kpi-avg-response", className="kpi-value"),
                            ],
                            className="kpi-card",
                        ),
                        html.Div(
                            [
                                html.Div("Avg Resolution Time (min)", className="kpi-label"),
                                html.Div(id="kpi-avg-resolution", className="kpi-value"),
                            ],
                            className="kpi-card",
                        ),
                        html.Div(
                            [
                                html.Div("% Long Resolution (>60 min)", className="kpi-label"),
                                html.Div(id="kpi-long-cases", className="kpi-value"),
                            ],
                            className="kpi-card",
                        ),
                    ],
                    className="kpi-row",
                ),
                className="kpi-container",
            ),

            # 🔹 Filters
            html.Div(
                html.Div(
                    [
                        html.Div(
                            [
                                html.Label("Office"),
                                dcc.Dropdown(
                                    id="home-office-filter",
                                    options=[{"label": "All Offices", "value": "ALL"}]
                                    + [{"label": o, "value": o} for o in (offices or [])],
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
                                    id="home-month-filter",
                                    options=[{"label": "All Months", "value": "ALL"}]
                                    + [{"label": m, "value": m} for m in (months or [])],
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

            # 🔹 Charts (ALL 4)
            html.Div(
                [
                    html.Div(dcc.Graph(id="home-response-chart"), className="chart-card"),
                    html.Div(dcc.Graph(id="home-resolution-chart"), className="chart-card"),
                ],
                className="chart-row",
            ),
            html.Div(
                [
                    html.Div(dcc.Graph(id="home-problem-resolution-chart"), className="chart-card"),
                    html.Div(dcc.Graph(id="home-problem-count-chart"), className="chart-card"),
                ],
                className="chart-row",
            ),
        ],
        className="page-card",
    )