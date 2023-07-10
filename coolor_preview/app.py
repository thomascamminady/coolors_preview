import streamlit as st
from coolor_preview.url2palette import url2palette
from coolor_preview.preview import create_preview


def app():
    st.set_page_config(layout="wide")
    st.markdown("# Preview palettes from coolors.co")
    # st.markdown("Just enter the url of a specific palette below to see some charts.")
    example_url = "https://coolors.co/palette/cdb4db-ffc8dd-ffafcc-bde0fe-a2d2ff"
    coolors_url = st.text_input(
        "palette",
        placeholder=example_url,
        label_visibility="hidden",
    )
    if coolors_url:
        palette = url2palette(coolors_url)
        st.code(palette.get_hex)
        # st.markdown(f"""[{coolors_url}]({coolors_url})""")
        altair_chart = create_preview(palette)
        st.altair_chart(altair_chart)


if __name__ == "__main__":
    app()
