from dash import Dash, html, dcc, Input, Output, callback_context

from codes.data_loader import load_data

from codes.layouts.home import home_layout
from codes.layouts.time_analysis import time_layout
from codes.layouts.problem_analysis import problem_layout
from codes.layouts.bonus_analysis import bonus_layout

from codes.callbacks.time_callbacks import register_time_callbacks
from codes.callbacks.problem_callbacks import register_problem_callbacks
from codes.callbacks.home_callbacks import register_home_callbacks
from codes.callbacks.bonus_callbacks import register_bonus_callbacks

# --------------------------------------------------
# Load data
# --------------------------------------------------
df = load_data()

months = sorted(df["Month"].unique())
offices = sorted(df["Office"].unique())
problems = sorted(df["Type of Technical Problem"].unique())

# --------------------------------------------------
# App
# --------------------------------------------------
app = Dash(__name__, suppress_callback_exceptions=True)

app.layout = html.Div(
    [
        # Track current page for active nav styling
        dcc.Store(id="current-page", data="home"),

        html.Div(
            id="page-content",
            children=home_layout(months, offices, problems),
        ),
    ]
)

# --------------------------------------------------
# Page navigation
# --------------------------------------------------
@app.callback(
    Output("page-content", "children"),
    Output("current-page", "data"),
    Input("nav-home", "n_clicks"),
    Input("nav-time", "n_clicks"),
    Input("nav-problem", "n_clicks"),
    Input("nav-bonus", "n_clicks"),
    prevent_initial_call=True,
)
def switch_page(home, time, problem, bonus):
    ctx = callback_context

    if not ctx.triggered:
        return home_layout(months, offices, problems), "home"

    button_id = ctx.triggered[0]["prop_id"].split(".")[0]

    if button_id == "nav-time":
        return time_layout(months, offices), "time"

    if button_id == "nav-problem":
        return problem_layout(offices, problems), "problem"

    if button_id == "nav-bonus":
        return bonus_layout(offices), "bonus"

    return home_layout(months, offices, problems), "home"

# --------------------------------------------------
# Active navigation button styling
# --------------------------------------------------
@app.callback(
    Output("nav-home", "className"),
    Output("nav-time", "className"),
    Output("nav-problem", "className"),
    Output("nav-bonus", "className"),
    Input("current-page", "data"),
)
def update_active_nav(current_page):

    def cls(page):
        return "nav-btn active" if current_page == page else "nav-btn"

    return (
        cls("home"),
        cls("time"),
        cls("problem"),
        cls("bonus"),
    )

# --------------------------------------------------
# Register callbacks
# --------------------------------------------------
register_time_callbacks(app, df)
register_problem_callbacks(app, df)
register_home_callbacks(app, df)
register_bonus_callbacks(app, df)

# --------------------------------------------------
# Run
# --------------------------------------------------
if __name__ == "__main__":
    app.run(debug=True)