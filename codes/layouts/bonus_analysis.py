from dash import html, dcc

def bonus_layout(offices):
    return html.Div(
        [
            # Title + Nav
            html.Div(
                [
                    html.H3("SLA & Efficiency Analysis", className="page-title"),
                    html.Div(
                        [
                            html.Button("Home", id="nav-home", className="nav-btn"),
                            html.Button("Time Analysis", id="nav-time", className="nav-btn"),
                            html.Button("Problem Analysis", id="nav-problem", className="nav-btn"),
                            html.Button("SLA", id="nav-bonus", className="nav-btn"),
                        ],
                        className="nav-buttons",
                    ),
                ],
                className="page-header",
            ),

            html.P(
                "SLA (Service Level Agreement) represents the percentage of support tickets responded to within the agreed threshold of 60 minutes.",
                style={
                    "marginTop": "6px",
                    "marginBottom": "22px",
                    "color": "#1F2937",
                    "fontSize": "17px",   
                    "fontWeight": "500",
                },
            ),

            # KPIs
            html.Div(
                html.Div(
                    [
                        html.Div(
                            [
                                html.Div("SLA Compliance (%)", className="kpi-label"),
                                html.Div(id="kpi-sla", className="kpi-value"),
                            ],
                            className="kpi-card",
                        ),
                        html.Div(
                            [
                                html.Div("High-Effort Tickets (>120 min)", className="kpi-label"),
                                html.Div(id="kpi-high-effort", className="kpi-value"),
                            ],
                            className="kpi-card",
                        ),
                        html.Div(
                            [
                                html.Div("Avg Tickets per Office", className="kpi-label"),
                                html.Div(id="kpi-load", className="kpi-value"),
                            ],
                            className="kpi-card",
                        ),
                    ],
                    className="kpi-row",
                ),
                className="kpi-container",
            ),
            
            # Charts
            html.Div(
                [
                    html.Div(dcc.Graph(id="sla-by-office-chart"), className="chart-card"),
                    html.Div(dcc.Graph(id="resolution-buckets-chart"), className="chart-card"),
                ],
                className="chart-row",
            ),
        ],
        className="page-card",
    )