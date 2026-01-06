def compute_kpis(df):
    return {
        "total_tickets": len(df),
        "avg_response_time": df["Response Time (Minutes)"].mean(),
        "avg_resolution_time": df["Time to Resolution (Minutes)"].mean(),
        "sla_met_pct": (df["Response Time (Minutes)"] <= 60).mean() * 100,
    }