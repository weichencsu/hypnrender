import streamlit as st
import streamlit.components.v1 as components

def main():
    st.set_page_config(page_title="HyPnMaster", layout="wide", initial_sidebar_state='auto')
    st.markdown(
            f"""
            <style>
                .reportview-container .main .block-container{{
                    max-width: 1800px;
                    padding-top: 1rem;
                    padding-right: 1rem;
                    padding-left: 1rem;
                    padding-bottom: 1rem;
                }}
            """,
            unsafe_allow_html=True,
        )


    #st.markdown("建设中，敬请期待！")
    iframeLINK = "http://dexing-pump-nzjah350-7b9d991d6fe-1306024390.tcloudbaseapp.com/"
    #local_pvModel(iframeLINK)
    #HtmlFile_tSS1 = open("Dexing.html", 'r', encoding='utf-8').read()
    #components.html(HtmlFile_tSS1, height=800)
    st.write(
            f'<iframe src=' + iframeLINK + ' height = "4000" width = "100%"></iframe>',
            unsafe_allow_html=True,
    )
    st.markdown("_______________________________________________________________________")

    hide_streamlit_style = """
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                </style>
                """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True) 






if __name__ == "__main__":
    main()











