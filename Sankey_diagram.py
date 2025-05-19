import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.path as mpath

# --- Data from Appendix C (Nyamwaya et al. 2025) ---
flows = {
    ("Reinforcement Learning", "Exploitation"): 9,
    ("Reinforcement Learning", "Command & Control"): 4,
    ("Traditional ML",        "Exploitation"): 5,
    ("LLMs",                  "Exploitation"): 3,
    ("Hybrid ML + Rule‑based","Exploitation"): 1
}

techniques = ["Reinforcement Learning", "Traditional ML", "LLMs", "Hybrid ML + Rule‑based"]
phases     = ["Exploitation", "Command & Control"]

tech_totals  = {t: 0 for t in techniques}
phase_totals = {p: 0 for p in phases}
for (t, p), v in flows.items():
    tech_totals[t]  += v
    phase_totals[p] += v

# Normalised rectangle heights
scale = 1.0 / sum(tech_totals.values())

def accumulate(items, totals):
    pos = {}
    y = 0.0
    for it in items:
        h = totals[it] * scale
        pos[it] = (y, h)
        y += h
    return pos

tech_pos  = accumulate(techniques, tech_totals)
phase_pos = accumulate(phases,     phase_totals)

fig, ax = plt.subplots(figsize=(9, 5))
ax.axis("off")
LEFT_X, RIGHT_X, NODE_W = 0.1, 0.75, 0.08

# Nodes
for t, (y, h) in tech_pos.items():
    ax.add_patch(patches.Rectangle((LEFT_X, y), NODE_W, h, color="#4C78A8"))
    ax.text(LEFT_X - 0.02, y + h/2, f"{t}\n({tech_totals[t]})", ha="right", va="center", fontsize=8)

for p, (y, h) in phase_pos.items():
    ax.add_patch(patches.Rectangle((RIGHT_X, y), NODE_W, h, color="#F58518"))
    ax.text(RIGHT_X + NODE_W + 0.02, y + h/2, f"{p}\n({phase_totals[p]})", ha="left", va="center", fontsize=8)

# Flows
tech_offset  = {t: 0.0 for t in tech_totals}
phase_offset = {p: 0.0 for p in phase_totals}

for (t, p), v in flows.items():
    y0 = tech_pos[t][0]  + tech_offset[t]
    y1 = y0 + v * scale
    y2 = phase_pos[p][0] + phase_offset[p]
    y3 = y2 + v * scale
    tech_offset[t]  += v * scale
    phase_offset[p] += v * scale

    verts = [
        (LEFT_X + NODE_W, (y0 + y1) / 2),
        (LEFT_X + NODE_W + 0.25, (y0 + y1) / 2),
        (RIGHT_X - 0.25, (y2 + y3) / 2),
        (RIGHT_X,           (y2 + y3) / 2)
    ]
    codes = [mpath.Path.MOVETO] + [mpath.Path.CURVE4] * 3
    path  = mpath.Path(verts, codes)
    width = max(0.6, v * 0.25)
    ax.add_patch(patches.PathPatch(path, edgecolor="#888888", linewidth=width, facecolor="none", alpha=0.7, capstyle="round"))

ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_title("Sankey‑style Mapping: AI/ML Techniques vs. Cyber Kill Chain Phases", fontsize=11)
plt.tight_layout()
plt.show()
