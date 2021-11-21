import streamlit as st

import streamlit.components.v1 as components
def sidebar_info():
    st.sidebar.subheader('Covid-19')
    st.sidebar.markdown("""
                   This visualization is based on the data from Pakistan Covid-19 .


                   **Context**: Covid Cases and Deaths over Time,
                   Total Confirmed Cases and
                   Incidence Rate by province.
                   

                   **Tool Used**: Tableau embedded
                   """)





def main():
    st.title("PAKISTAN COVID-19 DASHBOARD")
    st.write("""The below interactive dashboard displays the most covid cases in each province. \n\n  """)
    html_temp = """<div class='tableauPlaceholder' id='viz1637406626633' style='position: relative'><noscript><a href='#'><img alt='Dashboard 1 ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Co&#47;Covid-19Dashboard_16374062055850&#47;Dashboard1&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='Covid-19Dashboard_16374062055850&#47;Dashboard1' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Co&#47;Covid-19Dashboard_16374062055850&#47;Dashboard1&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-GB' /><param name='filter' value='publish=yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1637406626633');                    var vizElement = divElement.getElementsByTagName('object')[0];                    vizElement.style.width='1650px';vizElement.style.height='1227px';                    var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"""
    components.html(html_temp, width=1750, height=1300)
    max_width_str = f"max-width: 1030px;"
    st.markdown(f"""<style>.reportview-container .main .block-container{{{max_width_str}}}</style>""",unsafe_allow_html=True)
    st.markdown(f'Link to the public dashboard [here](https://public.tableau.com/views/Covid-19Dashboard_16374062055850/Dashboard1?:language=en-GB&publish=yes&:display_count=n&:origin=viz_share_link)')
    
if __name__ == "__main__":    
    sidebar_info()
    main()


