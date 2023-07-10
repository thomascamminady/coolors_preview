import altair as alt
import numpy as np
import polars as pl
from camminapy.plot import altair_theme

from coolor_preview.palette import Palette


def create_data(hex: list[str]) -> pl.DataFrame:
    np.random.seed(1)
    k = len(hex)
    n = 10
    x = np.random.rand(k * n)
    y = np.random.rand(k * n)
    t = np.hstack([np.arange(n)] * k)
    c = np.hstack([[h] * n for h in hex])

    return pl.DataFrame({"x": x, "y": y, "c": c, "t": t})


def create_preview(palette: Palette) -> alt.HConcatChart:
    altair_theme()
    hex = palette.get_hex
    df = create_data(hex)

    base = (
        alt.Chart(df.to_pandas())
        .encode(
            color=alt.Color("c:N").scale(range=hex, domain=hex).legend(None),
        )
        .properties(width=300, height=300)
    )

    chart1 = base.mark_point(filled=True, size=200, opacity=1).encode(
        x="x:Q",
        y="y:Q",
    )
    chart2 = base.mark_line(strokeWidth=3).encode(
        x=alt.X("t:Q", sort=None),
        y="y:Q",
    )

    chart3 = base.mark_bar(strokeOpacity=1).encode(
        x=alt.X("c:N"),
        y="x:Q",
    )

    chart4 = base.mark_rect().encode(
        x=alt.X("x:Q").bin(maxbins=5),
        y=alt.Y("y:Q").bin(maxbins=5),
        color=alt.Color("count():N").scale(range=hex).legend(None),
    )

    chart = alt.hconcat(
        alt.hconcat(chart1, chart2),
        alt.hconcat(chart3, chart4),
    )
    return chart
