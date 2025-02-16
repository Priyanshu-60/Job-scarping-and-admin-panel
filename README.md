# Job Admin

Job Admin is a web-based job management system built with **Django**. It allows users to manage job listings efficiently. Additionally, it includes a **job scraper** using the **Apify Client** to fetch job postings from external sources.

## Features
- **Job Posting Management** (CRUD operations)
- **Job Scraper** (Fetch job listings using Apify)
- **Database Integration** (MongoDB via Djongo)

## Installation
### Prerequisites
Ensure you have the following installed:
- Python 3.12
- Virtualenv (optional but recommended)
- MongoDB (if using Djongo)

### Setup
1. **Clone the repository**
   ```sh
   git clone https://github.com/yourusername/job_admin.git
   cd job_admin
   ```

2. **Create a virtual environment (optional but recommended)**
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```sh
   pip install -r requirements.txt
   ```

4. **Set up the database**

   - Using MongoDB (Djongo):
     ```python
     DATABASES = {
         'default': {
             'ENGINE': 'djongo',
             'NAME': 'job_admin_db',
         }
     }
     ```

5. **Run Migrations**
   ```sh
   python manage.py migrate
   ```

6. **Create a Superuser (Admin Panel Access)**
   ```sh
   python manage.py createsuperuser
   ```

7. **Run the Development Server**
   ```sh
   python manage.py runserver
   ```
   Access the app at `http://127.0.0.1:8000/`

## Job Scraper (Using Apify Client)
The project includes a job scraper using **Apify** to extract job listings from external sources.

### **Setup Apify Client**
1. Install Apify SDK:
   ```sh
   pip install apify-client
   ```
2. Add your **APIFY API Token** in `.env` file:
   ```env
   APIFY_API_TOKEN=your_apify_api_token
   ```
3. Run the scraper:
   ```sh
   python scraper.py
   ```


## Contributing
1. Fork the repository
2. Create a new branch (`feature-xyz`)
3. Commit your changes
4. Push to your branch
5. Open a Pull Request

## License
This project is licensed under the MIT License.

---
