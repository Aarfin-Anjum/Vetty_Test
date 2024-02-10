# Import necessary modules
from flask import Flask, render_template, request

# Create a Flask application
app = Flask(__name__)

# Define a single GET route
@app.route('/read_file', methods=['GET'])
def read_file():
    try:
        # Get parameters from the URL
        filename = request.args.get('filename', 'file1.txt')
        start_line = int(request.args.get('start_line', 1))
        end_line = int(request.args.get('end_line', None))

        # Read the content of the file
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()

            # Process lines based on start and end line parameters
            if end_line is not None:
                lines = lines[start_line - 1:end_line]
            else:
                lines = lines[start_line - 1:]

            # Join lines to form content
            content = ''.join(lines)

        # Render the content in an HTML page
        return render_template('index.html', content=content)

    except Exception as e:
        # Handle exceptions and render an error page with details
        return render_template('error.html', error=str(e))

# Run the Flask application if this script is executed directly
if __name__ == '__main__':
    app.run(debug=True)
