import requests
import urllib2
import json



uname = "gn.manikandan"
pwd="Mani@123"
jira_api_address = "http://localhost:8081/rest/auth/1/session"
jira_api_payload = { "username": uname, "password": pwd }
jira_api_payload = json.dumps(jira_api_payload)
headers = {'content-type': 'application/json'}



jira_json_data = requests.post(jira_api_address,data= jira_api_payload, headers=headers).json()

print jira_json_data
global sessionKey
sessionKey= jira_json_data["session"]["value"]


#sessionKey =  jira_json_data["session"]["value"]

jira_create_issue_url = "http://localhost:8081/rest/api/2/issue"


jira_create_issue_payload = {
      "fields": {
        "project": {
          "key": "RES"
        },
        "summary": "Credit card defect using python for 2nd time",
        "description": "This is api testing for creating an issue using python for the 2nd time",
        "issuetype": {
          "name": "Bug"
        }
      }
}

jira_create_issue_payload= json.dumps(jira_create_issue_payload)
headers = {'content-type': 'application/json','Cookie':'JSESSIONID='+sessionKey}


jira_create_issue_json_data = requests.post(jira_create_issue_url, data=jira_create_issue_payload, headers=headers).json()
print jira_create_issue_json_data

