from pathlib import Path

import streamlit as st

from PIL import Image

current_dir=  Path(__file__).parent if "__file__" in locals() else Path.cwd()

resume_file =  current_dir / "Assets" / "CV.pdf"



st.set_page_config(
    page_title="VVR Chandhran - Digital CV",
    layout="wide"
)

st.write(f"""
<div class="title" style="text-align: center; background-color: mustardyellow; opacity: 5;">
    <span style="font-size: 28px; text-shadow: 1px 1px 2px #FFD700, -1px -1px 2px #FFD700, 1px -1px 2px #FFD700, -1px 1px 2px #FFD700;">VVR CHANDHRAN | Digital-Savvy | Talent Acquisition Leader</span>
</div>
""", unsafe_allow_html=True)

st.markdown('<style>.title { animation: animateTitle 2s infinite ease-in-out; }</style>', unsafe_allow_html=True)

professional_summary = [
    "9.6+ years of Experience in Global IT & Engineering recruitment with strategic sourcing IT and Engineering Consultants utilizing standard tools such as internal database, job boards, and referrals.",
    "Has experience in Volume hiring / Contract staffing / Inhouse hiring.",
    "Has experience in Stakeholder management.",
    "Have recruiting experience in Industries like BFSI, Semiconductor, Insurance, Aerospace, Food and Beverages, Pharmaceuticals, Ecommerce.",
    "Recruitment tools used; Naukri, Monster, LinkedIn, Google, Job Street, Jobs dB.",
    "Regions Handled: Domestic – (PAN India), Middle east, APAC (Malaysia, Philippines, Singapore & Australia)",
    "Has working experience in ATS Tools – Taleo, Workday.",
    "Has experience in Involving with Campus Hiring when working with DXC (Computer Sciences corporation).",
    "Knowledge of developing Resume parser using python to understand the profile fitment as per JD."
]


# Display the professional summary as a list of bullet points
st.subheader("Professional Summary")
for item in professional_summary:
    st.markdown("- " + item)
st.sidebar.success("select a page above")

st.title("My Work Experience")

st.write("**Abeyaantirx Solutions | Recruitment Lead**")
st.write("08/2023 - Present")
st.write("""
**Managing Domain Requirements Across Regions:**

* Responsible to manage recruitment processes across multiple domains including Aerospace, Engineering, and IT.
* Managing recruitment activities across regions such as India, the US, and Canada, ensuring consistency and alignment with local requirements.

**Team Management:**

* Lead and manage a team of 6 recruiters, including 2 senior and 2 junior recruiters.
* Providing mentorship, performance feedback, and ensure the team achieves recruitment goals across different regions.

**Recruitment Framework Development:**

* Involved in Building recruitment framework strategies from scratch.
* Develop and implement process flow charts for recruitment to optimize efficiency.
* Frame and enforce compliance policies to ensure adherence to local regulations and industry standards in different regions.

**Stakeholder/Client Management:**

* Responsible to Act as the primary liaison for stakeholders and clients across regions, ensuring their recruitment needs are met effectively.
* Foster strong relationships with stakeholders to facilitate seamless recruitment processes and address any issues proactively.

**Handling Multiple Positions:**

* Manage the recruitment of 15+ positions simultaneously across various regions, balancing priorities to meet diverse needs and deadlines.

**Strategizing Sourcing Methodologies:**

* Responsible to Develop and implement sourcing strategies tailored to niche requirements, using advanced techniques such as:
    * Recruit'em for X-Ray searches.
    * Conducting reference campaigns to leverage networks.
    * Enhancing employer branding to attract top talent in different regions.

**Reporting and Analytics:**

* Build, maintain, and share comprehensive recruitment reports using tools like Excel and Power BI.
* Use data analytics to gain insights into recruitment processes and make informed decisions for continuous improvement.
""")

st.write("**Curious to know about my professional journey? Download my CV to learn more.**")

with open("Assets/CV.pdf", "rb") as pdf_file:
    pdf_bytes = pdf_file.read()


#download cv button

st.download_button(
    label=" Download my CV",
    data=pdf_bytes,
    file_name="CV.pdf",
    mime="application/pdf"
) 
social_icons = {
    "LinkedIn": {
        "icon_url": "https://cdn-icons-png.freepik.com/256/3536/3536505.png?semt=ais_hybrid",
        "link": "https://www.linkedin.com/in/vvr-chandhran/",
    },
    "GitHub": {
        "icon_url": "https://www.svgrepo.com/show/508828/github-01.svg",
        "link": "https://github.com/vvrchand",
    }
}

social_icons_html = []
for platform, data in social_icons.items():
    social_icons_html.append(
        f"""
        <a href="{data['link']}" target="_blank" style="margin-right: 10px;">
            <img class="social_icon" src="{data['icon_url']}" alt="{platform}" style="width: 40px; height: 40px;">
        </a>
        """
    )

st.markdown("**Feel free to connect with me on social media:**")
st.markdown("".join(social_icons_html), unsafe_allow_html=True)