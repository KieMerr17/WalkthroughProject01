import streamlit as st
from app_pages.multipage import MultiPage

# load pages scripts
from app_pages.page_one_information import site_information
from app_pages.page_two_feedback_generator import feedback_page
from app_pages.page_three_intervention_perception import intervention_perception


app = MultiPage(app_name="")  # Create an instance of the app

# Add your app pages here using .add_page()
app.add_page("Information", site_information)
app.add_page("Feedback Generator", feedback_page)
app.add_page("Intervention Perception", intervention_perception)


app.run()  # Run the app
