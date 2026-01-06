import plotly.express as px
import pandas as pd

def sla_by_office(df):
    dff = df.copy()
    dff["SLA Met"] = dff["Response Time (Minutes)"] <= 60

    agg = (
        dff.groupby("Office")["SLA Met"]
        .mean()
        .reset_index(name="SLA Rate")
    )

    fig = px.bar(
        agg,
        x="Office",
        y="SLA Rate",
        text=(agg["SLA Rate"] * 100).round(1),
    )

    fig.update_traces(
        marker_color="#6FA6B8",   
        textposition="outside",
    )
    

    fig.update_traces(texttemplate="%{text}%", textposition="outside")
    fig.update_layout(
        title="SLA Compliance Rate by Office",
        yaxis_title="SLA Compliance (%)",
        yaxis_tickformat=".0%",
    )

    return fig


def resolution_buckets(df):
    bins = [0, 60, 120, float("inf")]
    labels = ["≤ 60 min", "61–120 min", "> 120 min"]

    dff = df.copy()
    dff["Resolution Bucket"] = pd.cut(
        dff["Time to Resolution (Minutes)"],
        bins=bins,
        labels=labels,
    )

    agg = (
        dff.groupby(["Office", "Resolution Bucket"])
        .size()
        .reset_index(name="Count")
    )

    fig = px.bar(
        agg,
        x="Office",
        y="Count",
        color="Resolution Bucket",
        barmode="stack",
        color_discrete_map={
            "≤ 60 min": "#8FC1A9",   
            "61–120 min": "#F2C57C",
            "> 120 min": "#C0392B",  
        },
    )

    fig.update_traces(
        marker_line_color="#FFFFFF",
        marker_line_width=1,
    )

    return fig