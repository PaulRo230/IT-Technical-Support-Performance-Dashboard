import plotly.express as px

def avg_response_by_month(df):
    agg = (
        df.groupby(["Month", "Office"], observed=True)["Response Time (Minutes)"]
        .mean()
        .reset_index()
    )

    if agg.empty:
        return px.bar(title="No data for selected filters")

    fig = px.bar(
        agg,
        x="Month",
        y="Response Time (Minutes)",
        color="Office",
        barmode="group",
        color_discrete_map={
            "Bellingham": "#4C7D9A",
            "Olympia": "#5FA8A0",
            "Seattle": "#E0B36A",
            "Spokane": "#C97A6D",
        },
        text_auto=".1f"
    )
    fig.update_traces(textposition="outside")


    fig.update_layout(margin=dict(t=60))



    fig.update_layout(
        title={
            "text": "Average Response Time by Month",
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
            "color": "#494d5f",
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