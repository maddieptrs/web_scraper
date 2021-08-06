import requests
from bs4 import BeautifulSoup

# Find jobs
URL = "https://au.indeed.com/jobs"
payload = {'q': 'software engineer', 'l': 'brisbane', 'sort': 'date'}

page = requests.get(URL, params=payload)
soup = BeautifulSoup(page.content, "html.parser")

results = soup.find(id="mosaic-provider-jobcards")
jobs = results.find_all("a", class_="result")

URL = "https://au.indeed.com"

for job in jobs:
    remote = False
    link = job["href"]
    titles = job.find(class_="jobTitle").find_all("span")
    if len(titles) == 1:
        title = titles[0]["title"]
    else:
        title = titles[1]["title"]
    company = job.find(class_="companyName")
    location = job.find(class_="companyLocation")
    salary = job.find(class_="salary-snippet")

    print("Job: " + title)
    print("Company: " + company.text.strip())
    print("Location: " + location.text.strip())
    if (salary is not None):
        print("Salary: " + salary.text.strip())
    print("Link: " + URL + link + "\n")