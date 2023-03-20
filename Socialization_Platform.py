# Simulated list of group activities for the day
activities = [
    {'name': 'Book Club', 'time': '10:00 AM', 'location': 'Library'},
    {'name': 'Bingo', 'time': '2:00 PM', 'location': 'Community Center'},
    {'name': 'Yoga', 'time': '4:00 PM', 'location': 'Park'},
    {'name': 'Movie Night', 'time': '7:00 PM', 'location': 'Senior Center'},
]

# Generate an HTML page to display the group activities
html_page = '<html><body><h1>Socialization Platform</h1><table>'
html_page += '<tr><th>Name</th><th>Time</th><th>Location</th></tr>'
for a in activities:
    html_page += f'<tr><td>{a["name"]}</td><td>{a["time"]}</td><td>{a["location"]}</td></tr>'
html_page += '</table></body></html>'

# Write the HTML page
with open('group_activities.html', 'w') as f:
    f.write(html_page)
