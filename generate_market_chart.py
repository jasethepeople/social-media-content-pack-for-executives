from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

NAVY, TEAL, GRAY = "#102A43", "#1F9D8B", "#6B7280"

def make_chart(csv_path="market_data.csv", output="market_chart.png", title="Illustrative submarket trend"):
    df = pd.read_csv(csv_path)
    required = {"period", "occupancy_pct", "asking_rent_index"}
    missing = required - set(df.columns)
    if missing: raise ValueError(f"Missing columns: {sorted(missing)}")
    plt.style.use("default")
    fig, ax1 = plt.subplots(figsize=(12,7), dpi=160)
    ax1.plot(df.period, df.occupancy_pct, marker="o", color=TEAL, linewidth=3, label="Occupancy (%)")
    ax1.set_ylabel("Occupancy (%)", color=TEAL); ax1.tick_params(axis="y", labelcolor=TEAL); ax1.set_ylim(0,100)
    ax2 = ax1.twinx(); ax2.plot(df.period, df.asking_rent_index, marker="s", color=NAVY, linewidth=3, label="Asking rent index")
    ax2.set_ylabel("Asking rent index", color=NAVY); ax2.tick_params(axis="y", labelcolor=NAVY)
    ax1.set_title(title, loc="left", fontsize=18, fontweight="bold", color=NAVY, pad=16)
    ax1.grid(axis="y", alpha=.18); fig.tight_layout(); fig.savefig(output, bbox_inches="tight"); plt.close(fig)

if __name__ == "__main__": make_chart()
