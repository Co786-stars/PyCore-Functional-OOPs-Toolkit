# 0️⃣ QUESTION_______From__Multipal__Inheritance_______
"""
🎁 PRACTICE QUESTION : ➖ Related to Multipal Inheritance ➖

You're creating a system for a tech company. You need to design classes for:

1. Programmer Class:
   - Attributes: name, programming_language
   - Methods:
        code(): prints "{name} is coding in {programming_language}"
        get_language(): returns "Language: {programming_language}"

2. Manager Class:
   - Attributes: name, team_size
   - Methods:
        manage(): prints "{name} is managing {team_size} people"
        get_team_size(): returns "Team Size: {team_size}"

3. TechLead Class (inherits from both Programmer and Manager):
   - Attributes: name, programming_language, team_size, project_name
   - Methods:
        lead_project(): prints "{name} is leading {project_name}"
        code_and_manage(): calls both code() and manage() methods

Create these classes and test them with:
name = "Alice", programming_language = "Python",
team_size = 5, project_name = "AI Assistant"

Expected Output:
Alice
Alice is coding in Python
Language: Python
Alice is managing 5 people
Team Size: 5
Alice is leading AI Assistant
Alice is coding in Python
Alice is managing 5 people
"""

