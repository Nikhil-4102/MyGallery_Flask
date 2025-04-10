# MyGallery_Flask

MyGallery_Flask is a simple web application built using **Flask** that allows users to view images stored in a static folder. This project demonstrates how to create a lightweight image gallery using Python and Flask.

## 🗂️ Folder Structure

MyGallery_Flask/ ├── static/ │ └── images/ # Contains all the images to be displayed in the gallery ├── templates/ # HTML templates (e.g., gallery.html, layout.html) ├── app.yaml # Configuration for deployment (e.g., Google App Engine) ├── main.py # Main Flask application script ├── requirement.txt # Python dependencies └── README.md # Project documentation

markdown
Copy
Edit

## 🚀 Features

- View all images stored in the `static/images/` directory.
- Simple and clean gallery layout using Flask and HTML templates.
- Easy to deploy on platforms like Google App Engine.

## 🛠️ How to Run

1. **Clone the repository:**

```bash
git clone https://github.com/yourusername/MyGallery_Flask.git
cd MyGallery_Flask
Create a virtual environment (optional but recommended):

bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install dependencies:

bash
Copy
Edit
pip install -r requirement.txt
Run the Flask app:

bash
Copy
Edit
python main.py
Visit the app in your browser:

cpp
Copy
Edit
http://127.0.0.1:5000/
🌐 Deployment
The app can be deployed on Google App Engine using app.yaml. Make sure to install and configure the Google Cloud SDK.

bash
Copy
Edit
gcloud app deploy
📁 Add Your Images
To add your own images to the gallery, simply place them in the static/images/ directory.