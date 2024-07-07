from flask import Flask, render_template

app = Flask(__name__)

headings = ("Name", "Position", "Office", "Age", "Start date", "Salary")
data = (
    ("Rolf", "Software Engineer", "N/A", "N/A", "N/A", "£42,000.00"),
    ("Amy", "Product Owner", "N/A", "N/A", "N/A", "£55,000.00"),
    ("Bob", "Security Engineer", "N/A", "N/A", "N/A", "£45,000.00"),
    ("Tim", "VP", "N/A", "N/A", "N/A", "£80,000.00"),
    ("Dave", "Head Honcho", "N/A", "N/A", "N/A", "£100,000.00"),
)

@app.route('/', methods=["GET"])
def homePage():
    return render_template("index.html", headings=headings, data=data)

if __name__ == '__main__':
    app.run(debug=True)