"""

Config file for Streamlit App

"""

from .member import Member


TITLE = "Accident de la route"

TEAM_MEMBERS = [
    Member(
        name="Artem",
        linkedin_url="http://linkedin.com",
        github_url="https://github.com/artmskfr",
    ),
    Member(
        name="Fabien",
        linkedin_url="http://linkedin.com",
        github_url="https://github.com/Henri35/",
    ),
    Member(
        name="Jérôme",
        linkedin_url="http://linkedin.com",
        github_url="https://github.com/Jeromik/",
    ),
    Member(
        name="Juliette",
        linkedin_url="http://linkedin.com",
        github_url="https://github.com/JulietteB927/",
    )
    
]

PROMOTION = "Promotion Bootcamp Data Scientist - Novembre 2023"
