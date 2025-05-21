from flask import Flask, request, render_template_string
import mysql.connector

app = Flask(__name__)

db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Dipj@15072006',
    'database': 'ecommerce'
}

# Load the HTML form
html_form=open('index.html').read()

# Route to display the form
@app.route('/', methods=['GET'])
def show_form():
    return render_template_string(html_form)

# Route to handle form submission
@app.route('/upload', methods=['POST'])
def upload():
    category = request.form['category']
    description = request.form['description']
    minRange = int(request.form['minRange'])
    maxRange = int(request.form['maxRange'])

    image_file = request.files['image_data']  # Name should match HTML form
    image_data = image_file.read()

    print("Received:")
    print("Category:", category)
    print("Description:", description)
    print("Min:", minRange)
    print("Max:", maxRange)
    print("Image size:", len(image_data), "bytes")

    # Save to DB
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    sql = """
    INSERT INTO chatbox (category, description, minRange, maxRange, image_data)
    VALUES (%s, %s, %s, %s, %s)
    """
    cursor.execute(sql, (category, description, minRange, maxRange, image_data))
    conn.commit()

    cursor.close()
    conn.close()

    return "Data inserted successfully!"

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/view')
def view_data():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("SELECT id, category, description, minRange, maxRange, LENGTH(image_data) FROM chatbox")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()

    result = "<h2>Submitted Entries:</h2><ul>"
    for row in rows:
        result += f"<li>ID: {row[0]}, Category: {row[1]}, Description: {row[2]}, Min: {row[3]}, Max: {row[4]}, Image Size: {row[5]} bytes</li>"
    result += "</ul>"
    return result
