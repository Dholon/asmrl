import sys

with open('index.html', 'r') as f:
    lines = f.readlines()

new_lines = [
    '    <script src="https://cdn.jsdelivr.net/npm/lucide@latest/dist/umd/lucide.min.js"></script>\n',
    '    <script src="https://cdn.tailwindcss.com"></script>\n',
    '    <script>\n',
    '        tailwind.config = {\n',
    '            theme: {\n',
    '                extend: {\n',
    '                    colors: {\n',
    '                        bracu: \'#004B87\',\n',
    '                        bracuLight: \'#0066b3\',\n',
    '                        bracuDark: \'#00335e\'\n',
    '                    },\n',
    '                    fontFamily: {\n',
    '                        sans: [\'Inter\', \'sans-serif\'],\n',
    '                    }\n',
    '                }\n',
    '            }\n',
    '        }\n',
    '    </script>\n'
]

# Replace lines 15-499 (index 14 to 498)
lines = lines[:14] + new_lines + lines[499:]

# Also fix the "Researcher" to "Student Researcher" and "Teaching Assistant"
for i in range(len(lines)):
    if 'session: "Researcher"' in lines[i]:
        if '"Shahnil Zulkarnain"' in lines[i]:
            lines[i] = lines[i].replace('session: "Researcher"', 'session: "Teaching Assistant"')
        else:
            lines[i] = lines[i].replace('session: "Researcher"', 'session: "Student Researcher"')

with open('index.html', 'w') as f:
    f.writelines(lines)
