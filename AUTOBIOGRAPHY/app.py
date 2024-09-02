import streamlit as st
from streamlit_extras.stylable_container import stylable_container

st.markdown("# April Gem's Autobiography")

tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["About", "Education", "Family & Friends", "Interests", "Portfolio", "Certifications"])

with tab1:
    st.header("About Me")
    
    col1, col2 = st.columns(2, gap="large", vertical_alignment="center")

    with col1:
        with stylable_container(
            key = "main_pic",
            css_styles="""
            img {
                border-radius: 100px;
            }        
            """,
        ):
            st.image("./AUTOBIOGRAPHY/images/me1.jpg", width=300)

    with col2:
        st.markdown("Hello, everyone! I'm ***April Gem M. Jagmoc***. Yes, you guessed it right! I was born on the month of April which was the 4th Friday of April in the year 2002 (April 26, 2002). No, I don't have a sibling named May, June, or July. In fact, I'm the only child my parents named after their child's birth month.") 
        st.markdown("I'm currently a ***4th year college student*** taking up *Bachelor of Science in Information Technology* at *Cebu Institute of Technology - University*. I only have 3 courses left to pass to graduate from college, including this course.")
with tab2:
    st.header("Education")

    col1, col2 = st.columns(2, gap="small", vertical_alignment="center")
    col3, col4 = st.columns(2, gap="small", vertical_alignment="center")
    col5, col6 = st.columns(2, gap="small", vertical_alignment="center")
    col7, col8 = st.columns(2, gap="small", vertical_alignment="center")

    with col1:
        st.markdown("**ELEMENTARY**")
        st.markdown("Name of the School: City Central Elementary School")
        st.markdown("School's Address: P. Del Rosario Street,Brgy, Kalubihan, Cebu City")
        st.markdown("Years Attended: 2008 - 2014")
    
    with col2: 
        with stylable_container(
        key = "con",
        css_styles=["""
        {
            background-color: pink;
            border-radius: 1em;
            padding: 1em;
        }        
        """,
        """
        .stMarkdown {
            padding-right: 1.5em;
        }
        """]
    ):
            st.markdown("")
            st.markdown("")
            st.markdown("")
            st.markdown("")
            st.markdown("")
            st.markdown("")
            st.markdown("**NO PHOTO**")
            st.markdown("")
            st.markdown("")
            st.markdown("")
            st.markdown("")
            st.markdown("")

    with col3:
        with stylable_container(
            key = "pics",
            css_styles="""     
            img {
                border-radius: 20px;
            }   
            """,
        ):
            st.image("./AUTOBIOGRAPHY/images/grad1.jpg", width=300)
            
    with col4:
        st.markdown("**JUNIOR HIGH SCHOOL**")
        st.markdown("Name of the School: Southwestern University PHINMA")
        st.markdown("School's Address: Aznar Road, Urgello Street, Cebu City")
        st.markdown("Years Attended: 2014 - 2018")

    with col5:
            st.markdown("**SENIOR HIGH SCHOOL**")
            st.markdown("Name of the School: Southwestern University PHINMA")
            st.markdown("School's Address: Aznar Road, Urgello Street, Cebu City")
            st.markdown("Years Attended: 2018 - 2020")
            
    with col6:
        with stylable_container(
            key = "pics",
            css_styles="""     
            img {
                border-radius: 20px;
            }   
            """,
        ):
            st.image("./AUTOBIOGRAPHY/images/grad2.JPG", width=300)

    with col7:
        with stylable_container(
        key = "con",
        css_styles=["""
        {
            background-color: pink;
            border-radius: 1em;
            padding: 1em;
        }        
        """,
        """
        .stMarkdown {
            padding-right: 1.5em;
        }
        """]
    ):
            st.markdown("")
            st.markdown("")
            st.markdown("")
            st.markdown("")
            st.markdown("")
            st.markdown("")
            st.markdown("**TO BE FOLLOWED**")
            st.markdown("")
            st.markdown("")
            st.markdown("")
            st.markdown("")
            st.markdown("")
            
    with col8:
        st.markdown("**COLLEGE**")
        st.markdown("Name of the School: Cebu Institute of Technology - University")
        st.markdown("School's Address: N. Bacalso Street, Cebu City")
        st.markdown("Years Attended: 2020 - present")

with tab3:
    st.header("Family")

    col1, col2 = st.columns(2, gap="small", vertical_alignment="center")

    with col1:
        with stylable_container(
            key = "pics",
            css_styles="""     
            img {
                border-radius: 20px;
            }   
            """,
        ):
            st.image("./AUTOBIOGRAPHY/images/fam1.jpg", width=300)
            
    with col2:
        st.markdown("This is my big family.")
        st.markdown("I have 6 siblings,  2 brothers, 3 sisters, and 1 younger brother. I'm the youngest daughter in our family. My younger brother died two days after he was born so I never really got the chance to spend time with him.")
        st.markdown("I have three nephews. I've been taking care of them, and I can honestly say that it's both exhausting and rewarding at the same time. I've witnessed their first crawl, walk, word, and solid food.")
    
    st.header("Friends")

    col1, col2 = st.columns(2, gap="small", vertical_alignment="center")

    with col1:
        st.markdown("These are my best friends, a.k.a. my cousins.")
        st.markdown("We've been together for almost all our lives since we live so close. I just can't picture not having my cousins with me. Whenever I have problems, stories, and stuff, I just have to share it with them immediately.")
        st.markdown("We've shared so many laughters, fights, cries, and silly moments. I can just share everything with them without any judgement but, ofcourse, we don't tolerate bad behaviors.")
    with col2:
        with stylable_container(
            key = "pics",
            css_styles="""      
            """,
        ):
            st.image("./AUTOBIOGRAPHY/images/cous.jpg", width=300)

with tab4:
    st.header("Interests")
    
    col1, col2 = st.columns(2, gap="small", vertical_alignment="center")

    with col1:
        with stylable_container(
            key = "pics",
            css_styles=""" 
            """,
        ):
            st.image("./AUTOBIOGRAPHY/images/hike.jpg", width=300)
            st.image("./AUTOBIOGRAPHY/images/food8.jpg", width=300)
            st.image("./AUTOBIOGRAPHY/images/luigi.jpg", width=300)
            
    with col2:
        with stylable_container(
            key = "pics",
            css_styles="""
            """,
        ):
            st.image("./AUTOBIOGRAPHY/images/travel3.jpg", width=300)
            st.image("./AUTOBIOGRAPHY/images/travel2.jpg", width=300)
            st.image("./AUTOBIOGRAPHY/images/food5.jpg", width=300)

    with stylable_container(
        key = "con",
        css_styles=["""
        {
            background-color: pink;
            border-radius: 1em;
            padding: 1em;
        }        
        """,
        """
        .stMarkdown {
            padding-right: 1.5em;
        }
        """]
    ):

        st.markdown("I enjoy cafe hoping, travelling, connecting with nature, taking care of my pet, and lots of eating!!!")
        st.markdown("Last month, I started taking care of my physical health again so I started doing my morning walks and jogging and even tried hiking, which was a success. Now, I can say that I'm more active in the morning than when I was just spending my time scrolling through my socials and lying in bed.")
        st.markdown("My pet's name is Luigi. My boyfriend and I adopted him last February and he's turning 1 year old this coming November 11, 2024. I've had bad experiences with cats before so I wasn't really a fan of cats and never thought that I would adopt one. But, my cousin showed me a picture of him. He was just 2 months when we got him. I super duper love him!")

with tab5:
    st.header("Portfolio")

    st.markdown("In this section, you will see a compilation of my design projects (individual & team). These are just from the figma files since I can't find the other files but, hopefully soon I can add some of my works here.")

    with stylable_container(
        key = "main_pic",
        css_styles="""
        img {
            border-radius: 50px;
        }        
        """,
    ):
        st.image("./AUTOBIOGRAPHY/images/work1.png", width=700)
        st.image("./AUTOBIOGRAPHY/images/work2.png", width=700)
        st.image("./AUTOBIOGRAPHY/images/work3.png", width=700)

with tab6:
    st.header("Certifications")

    st.markdown("In this section, you will see a compilation of the certifications I received from finishing some courses related to my subjects.")

    with stylable_container(
        key = "main_pic",
        css_styles="""
        img {
            border-radius: 50px;
        }        
        """,
    ):
        st.image("./AUTOBIOGRAPHY/images/cert1.jpg", width=700)
        st.image("./AUTOBIOGRAPHY/images/cert2.jpg", width=700)
        st.image("./AUTOBIOGRAPHY/images/cert3.jpg", width=700)
        st.image("./AUTOBIOGRAPHY/images/cert4.png", width=700)
        st.image("./AUTOBIOGRAPHY/images/cert5.png", width=700)
        st.image("./AUTOBIOGRAPHY/images/cert6.png", width=700)
        st.image("./AUTOBIOGRAPHY/images/cert7.png", width=700)
