# Simulated list of daily activities
activities = [
    {'name': 'Breakfast', 'time': '8:00 AM'},
    {'name': 'Morning Walk', 'time': '9:00 AM'},
    {'name': 'Lunch', 'time': '12:00 PM'},
    {'name': 'Nap', 'time': '2:00 PM'},
    {'name': 'Afternoon Walk', 'time': '4:00 PM'},
    {'name': 'Dinner', 'time': '6:00 PM'},
]

# Generate an HTML page to display daily activities
html_page = '<html><body><h1>Daily Activity Tracker</h1><table>'
html_page += '<tr><th>Name</th><th>Time</th><th>Completed</th></tr>'
for a in activities:
    html_page += f'<tr><td>{a["name"]}</td><td>{a["time"]}</td><td><input type="checkbox"></td></tr>'
html_page += '</table></body></html>'

# Write the HTML page
with open('daily_activity_tracker.html', 'w') as f:
    f.write(html_page)
