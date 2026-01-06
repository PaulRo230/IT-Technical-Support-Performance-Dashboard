from dash import Input, Output
from codes.charts.bonus_charts import sla_by_office, resolution_buckets

def register_bonus_callbacks(app, df):

    @app.callback(
        Output("kpi-sla", "children"),
        Output("kpi-high-effort", "children"),
        Output("kpi-load", "children"),
        Output("sla-by-office-chart", "figure"),
        Output("resolution-buckets-chart", "figure"),
        Input("page-content", "children"),
    )
    def update_bonus(_):

        total = len(df)
        offices = df["Office"].nunique()

        sla_rate = (df["Response Time (Minutes)"] <= 60).mean() * 100
        high_effort = (df["Time to Resolution (Minutes)"] > 120).mean() * 100
        load = total / offices

        return (
            f"{sla_rate:.1f}%",
            f"{high_effort:.1f}%",
            round(load, 1),
            sla_by_office(df),
            resolution_buckets(df),
        )