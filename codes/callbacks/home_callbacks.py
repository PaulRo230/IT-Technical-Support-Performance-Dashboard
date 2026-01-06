from dash import Input, Output
from codes.charts.time_charts import avg_response_by_month
from codes.charts.resolution_charts import avg_resolution_by_month
from codes.charts.problem_charts import (
    avg_resolution_by_problem,
    count_cases_by_problem,
)

def register_home_callbacks(app, df):

    @app.callback(
        Output("kpi-total-cases", "children"),
        Output("kpi-avg-response", "children"),
        Output("kpi-avg-resolution", "children"),
        Output("kpi-long-cases", "children"),
        Output("home-response-chart", "figure"),
        Output("home-resolution-chart", "figure"),
        Output("home-problem-resolution-chart", "figure"),
        Output("home-problem-count-chart", "figure"),
        Input("home-office-filter", "value"),
        Input("home-month-filter", "value"),
    )
    def update_home_dashboard(office, month):

        dff = df.copy()

        if office != "ALL":
            dff = dff[dff["Office"] == office]

        if month != "ALL":
            dff = dff[dff["Month"] == month]

        total_cases = len(dff)
        avg_response = round(dff["Response Time (Minutes)"].mean(), 1)
        avg_resolution = round(dff["Time to Resolution (Minutes)"].mean(), 1)
        long_pct = round((dff["Time to Resolution (Minutes)"] > 60).mean() * 100, 1)

        return (
            total_cases,
            avg_response,
            avg_resolution,
            f"{long_pct}%",
            avg_response_by_month(dff),
            avg_resolution_by_month(dff),
            avg_resolution_by_problem(dff, "ALL", "ALL"),
            count_cases_by_problem(dff, "ALL", "ALL"),
        )