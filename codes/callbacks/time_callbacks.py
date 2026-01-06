from dash import Input, Output
from codes.charts.time_charts import avg_response_by_month
from codes.charts.resolution_charts import avg_resolution_by_month

def register_time_callbacks(app, df):

    @app.callback(
        Output("response-chart", "figure"),
        Output("resolution-chart", "figure"),
        Input("time-month-filter", "value"),
        Input("time-office-filter", "value"),
    )
    def update_time_charts(month, office):

        dff = df.copy()

        if month != "ALL":
            dff = dff[dff["Month"] == month]

        if office != "ALL":
            dff = dff[dff["Office"] == office]

        return (
            avg_response_by_month(dff),
            avg_resolution_by_month(dff),
        )