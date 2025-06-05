import plotly.graph_objects as go

labels = [
    "Reinforcement Learning<br>(13)",        # 0
    "Traditional&nbsp;ML<br>(5)",            # 1
    "LLMs<br>(3)",                           # 2
    "Hybrid ML + Rule‐based\n(1)",           # 3  ← updated here
    "Exploitation<br>(18)",                  # 4
    "Command &amp; Control<br>(4)"           # 5
]

# left‐side nodes (techniques): indices 0–3
sources = [0, 0, 1, 2, 3]
# right‐side nodes (CKC phases): indices 4–5
targets = [4, 5, 4, 4, 4]
values  = [9, 4, 5, 3, 1]

node_colours = [
    "#1f77b4",  # Reinforcement Learning
    "#ff7f0e",  # Traditional ML
    "#d62728",  # LLMs
    "#17becf",  # Hybrid ML + Rule‐based
    "#2ca02c",  # Exploitation
    "#7f7f7f"   # Command & Control
]
link_colours = [node_colours[s] for s in sources]

fig = go.Figure(data=[go.Sankey(
    node=dict(
        pad=15,
        thickness=30,
        label=labels,
        color=node_colours,
        line=dict(width=0.5, color="black")
    ),
    link=dict(
        source=sources,
        target=targets,
        value=values,
        color=link_colours,
        hovertemplate="<b>%{value}</b> papers<extra></extra>"
    )
)])

fig.update_layout(
    title_text="Mapping AI/ML Techniques in Intelligent Honeypots to Cyber Kill Chain Phases",
    font=dict(size=16, color="black"),     # larger, dark text for readability
    width=900,
    height=550,
    margin=dict(l=0, r=0, t=60, b=0),
    paper_bgcolor='rgba(0,0,0,0)',          # transparent background
    plot_bgcolor='rgba(0,0,0,0)'            # transparent background
)

fig.show()

