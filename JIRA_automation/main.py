
from jira import JIRA
import re
# Make a file credentials.py with code
# def getUser():
#     return "Ihor.Maidanovskyi"
# def getPass():
#     return "foobar"
from credentials import *

TEAM = {"Ihor.Maidanovskyi", "Dmytro.Trunov", "Sergii.Litovchuk", "Serhii.Anhelov", "Vadym.Ostanin", "Oksana.Shyshka", "Vadym.Savchuk", "Konstantin.Popov", "Oleksandr.Ihnatenko", "Yevhenii.Andrus"}
options = {
    'server': 'http://automotive.atlassian.infopulse.local:8080'}
jira = JIRA(options, basic_auth=(getUser(), getPass()))

PROJECT_NAME = "PCCMIB3"
MEETINGS_ESTIMATE = "8h" #0.5h everyday + retro + grooming + sprint planning
MEETINGS_TITLE = "FrontDesk repetitive meetings - "
SPRINT_TEMPLATE = "Navi Sprint Y18"
SPRINT_WEEKS = "CW43-44"
COMPONENT = 'NAV_DI_FrontDesk'
FRONT_DESK_MEETINGS_EPIC = jira.issue("PCCMIB3-5500")

print("start adding meeting tasks to " + COMPONENT + " on " + SPRINT_TEMPLATE + SPRINT_WEEKS)
print("Estimate for " + MEETINGS_TITLE + " is  " + MEETINGS_ESTIMATE)

for member in TEAM:
    issue_dict = {
        'project': PROJECT_NAME,
        'summary': MEETINGS_TITLE + member,
        'description': 'Daily meetings + Retro + Sprint planning',
        'issuetype': {'name': 'Dev Task'},
        'components': [{'name': COMPONENT}],
        'assignee': {'name': member},
        'timetracking': {"originalEstimate": MEETINGS_ESTIMATE,  "remainingEstimate": MEETINGS_ESTIMATE}
    }
    new_issue = jira.create_issue(fields=issue_dict)
    jira.assign_issue(new_issue, member)
    jira.add_issues_to_epic(FRONT_DESK_MEETINGS_EPIC.id, [new_issue.key])
    jira.add_issues_to_sprint(SPRINT_TEMPLATE + SPRINT_WEEKS, [new_issue.key])
    print(member + " is processed")
print ("done")