# Simulated list of medications
medications = [
    {'name': 'Metformin', 'dosage': '500 mg', 'time': '8:00 AM'},
    {'name': 'Lisinopril', 'dosage': '10 mg', 'time': '12:00 PM'},
    {'name': 'Simvastatin', 'dosage': '20 mg', 'time': '6:00 PM'},
]

# Generate an HTML page to display medication reminders
html_page = '<html><body><h1>Medication Reminder</h1><table>'
html_page += '<tr><th>Name</th><th>Dosage</th><th>Time</th><th>Completed</th></tr>'
for m in medications:
    html_page += f'<tr><td>{m["name"]}</td><td>{m["dosage"]}</td><td>{m["time"]}</td><td><input type="checkbox"></td></tr>'
html_page += '</table></body></html>'

# Write the HTML page
with open('medication_reminder.html', 'w') as f:
    f.write(html_page)
