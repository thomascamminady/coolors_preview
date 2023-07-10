import altair as alt
import numpy as np
import polars as pl
from camminapy.plot import altair_theme

from coolors_preview.palette import Palette


def create_data(hex: list[str]) -> pl.DataFrame:
    np.random.seed(1)
    k = len(hex)
    n = 10
    x = np.random.rand(k * n)
    y = np.random.rand(k * n)
    t = np.hstack([np.arange(n)] * k)
    c = np.hstack([[h] * n for h in hex])

    return pl.DataFrame({"x": x, "y": y, "c": c, "t": t})


def create_palette(palette: Palette) -> alt.Chart:
    altair_theme()
    df = pl.DataFrame(
        [{"i": i, "color": color} for i, color in enumerate(palette.get_hex)]
    )
    return (
        alt.Chart(df)
        .mark_rect()
        .encode(
            x=alt.X("i:N").axis(None),
            y=alt.value(1.0),
            color=alt.Color("color:N", sort=None)
            .scale(range=palette.get_hex)
            .legend(None),
        )
    ).properties(height=200, width=1250)


def create_preview(palette: Palette) -> alt.HConcatChart:
    altair_theme()
    hex = palette.get_hex
    df = create_data(hex)

    base = (
        alt.Chart(df.to_pandas())
        .encode(
            color=alt.Color("c:N").scale(range=hex, domain=hex).legend(None),
        )
        .properties(width=400, height=300)
    )

    chart1 = base.mark_point(filled=True, size=200, opacity=1).encode(
        x=alt.X("x:Q").axis(None),
        y=alt.Y("y:Q").axis(None),
    )
    chart2 = base.mark_line(strokeWidth=3).encode(
        x=alt.X("t:Q", sort=None).axis(None),
        y=alt.Y("y:Q").axis(None),
    )

    chart3 = base.mark_bar(strokeOpacity=1, strokeWidth=10).encode(
        x=alt.X("x:N").bin().axis(None),
        y=alt.Y("count():Q").axis(None),
    )

    chart = alt.hconcat(chart1, chart2, chart3)
    return chart
