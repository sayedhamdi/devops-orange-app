from flask import Flask, render_template, request

app = Flask(__name__)

# Sample DevOps Questions (MCQs)
questions = [
    {
        "question": "What does CI stand for in DevOps?",
        "options": ["Continuous Integration", "Code Inspection", "Centralized Infrastructure", "Continuous Improvement"],
        "answer": "Continuous Integration"
    },
    {
        "question": "Which tool is used for containerization?",
        "options": ["Ansible", "Docker", "Jenkins", "Nagios"],
        "answer": "Docker"
    },
    {
        "question": "Which language is primarily used in writing Terraform code?",
        "options": ["Python", "Bash", "HCL", "Ruby"],
        "answer": "HCL"
    },
    {
        "question": "What does YAML stand for?",
        "options": ["Yet Another Markup Language", "YAML Ain't Markup Language", "Your Application Markup Language", "None of the above"],
        "answer": "YAML Ain't Markup Language"
    },
]

# Add dummy questions until we have 20
while len(questions) < 20:
    questions.append({
        "question": f"Sample Question {len(questions) + 1}?",
        "options": ["Option A", "Option B", "Option C", "Option D"],
        "answer": "Option A"
    })

@app.route('/')
def index():
    return render_template('index.html', questions=questions)

@app.route('/submit', methods=['POST'])
def submit():
    score = 0
    answers = []  # Track selected answers for feedback
    for i, q in enumerate(questions):
        selected = request.form.get(f'q{i}')
        correct = q['answer']
        answers.append({'question': q['question'], 'selected': selected, 'correct': correct})
        if selected == correct:
            score += 1
    return render_template('result.html', score=score, total=len(questions), answers=answers)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
