from dash import Input, Output
from codes.charts.problem_charts import (
    avg_resolution_by_problem,
    count_cases_by_problem,
)

def register_problem_callbacks(app, df):

    @app.callback(
        Output("problem-avg-resolution-chart", "figure"),
        Output("problem-count-chart", "figure"),
        Input("problem-type-filter", "value"),
        Input("problem-office-filter", "value"),
    )
    def update_problem_charts(problem_type, office):

        if problem_type != "ALL":
            dff = df[df["Type of Technical Problem"] == problem_type]
        else:
            dff = df.copy()

        if office != "ALL":
            dff = dff[dff["Office"] == office]

        fig_avg = avg_resolution_by_problem(dff, "ALL", "ALL")
        fig_count = count_cases_by_problem(dff, "ALL", "ALL")

        return fig_avg, fig_count