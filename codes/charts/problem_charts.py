import plotly.express as px

COLOR_MAP = {
    "Bellingham": "#4C7D9A",
    "Olympia": "#5FA8A0",
    "Seattle": "#E0B36A",
    "Spokane": "#C97A6D",
}

def avg_resolution_by_problem(df, office, problem):
    data = df.copy()

    if office != "ALL":
        data = data[data["Office"] == office]

    if problem != "ALL":
        data = data[data["Type of Technical Problem"] == problem]

    agg = (
        data
        .groupby(["Type of Technical Problem", "Office"], observed=True)
        ["Time to Resolution (Minutes)"]
        .mean()
        .reset_index()
    )

    if agg.empty:
        return px.bar(title="No data for selected filters")

    fig = px.bar(
        agg,
        x="Type of Technical Problem",
        y="Time to Resolution (Minutes)",
        color="Office",
        barmode="group",
        color_discrete_map=COLOR_MAP,
        text_auto=".1f",
    )

    fig.update_traces(textposition="outside")

    fig.update_layout(
        title="Average Resolution Time by Problem Type and Office",
        paper_bgcolor="#F3F6FA",
        plot_bgcolor="#F3F6FA",
        margin=dict(t=70, l=40, r=30, b=40),
        xaxis_title="Technical Problem Type",
        yaxis_title="Avg Resolution Time (Minutes)",
        font=dict(size=13),
    )

    return fig


def count_cases_by_problem(df, office, problem):
    data = df.copy()

    if office != "ALL":
        data = data[data["Office"] == office]

    if problem != "ALL":
        data = data[data["Type of Technical Problem"] == problem]

    agg = (
        data
        .groupby(["Type of Technical Problem", "Office"], observed=True)
        .size()
        .reset_index(name="Case Count")
    )

    if agg.empty:
        return px.bar(title="No data for selected filters")

    fig = px.bar(
        agg,
        x="Case Count",
        y="Type of Technical Problem",
        color="Office",
        orientation="h",
        barmode="group",
        color_discrete_map=COLOR_MAP,
        text_auto=".0f",
    )

    fig.update_traces(textposition="outside")

    fig.update_layout(
        title="Number of Cases by Problem Type and Office",
        paper_bgcolor="#F3F6FA",
        plot_bgcolor="#F3F6FA",
        margin=dict(t=70, l=40, r=30, b=40),
        xaxis_title="Number of Cases",
        yaxis_title="Technical Problem Type",
        font=dict(size=13),
    )

    return fig