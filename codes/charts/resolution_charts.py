import plotly.express as px

def avg_resolution_by_month(df):
    agg = (
        df.groupby(["Month", "Office"], observed=True)["Time to Resolution (Minutes)"]
        .mean()
        .reset_index()
    )

    if agg.empty:
        return px.line(title="No data for selected filters")

    fig = px.line(
        agg,
        x="Month",
        y="Time to Resolution (Minutes)",
        color="Office",
        color_discrete_map={
            "Bellingham": "#4C7D9A",
            "Olympia": "#5FA8A0",
            "Seattle": "#E0B36A",
            "Spokane": "#C97A6D",
        },
        markers=True,
        text=agg["Time to Resolution (Minutes)"].round(0),
    )

    fig.update_traces(
        mode="lines+markers+text",
        textposition="top center"
    )

    fig.update_layout(
        title={
            "text": "Average Resolution Time Trend by Month",
            "x": 0.02,
            "font": {
                "size": 18,
                "color": "#2F3E3A",
                "family": "Inter, Arial, sans-serif",
            },
        },
        plot_bgcolor="#FFFFFF",
        paper_bgcolor="#FFFFFF",
        font={
            "family": "Inter, Arial, sans-serif",
            "color": "#2F3E3A",
        },
        yaxis=dict(
            showgrid=True,
            gridcolor="rgba(47, 62, 58, 0.12)",
            zeroline=False,
        ),
        xaxis=dict(showgrid=False),
        legend_title_text="Office",
        margin=dict(t=70, l=40, r=20, b=40),
    )

    return fig