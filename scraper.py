from apify_client import ApifyClient
import pymongo

# Replace this with your actual API token from Apify
API_TOKEN = "apify_api_gZyq6S2NfddCal9LtheafhzkthKjPi1v179s"

def scrape_jobs(city, country="IN", max_items=50):
    """Scrape job listings using Apify's Indeed Actor."""
    
    client = ApifyClient(API_TOKEN)

    run_input = {
        "position": "Python Developer",
        "country": country,
        "location": "Lucknow",
        "maxItems": max_items,
        "parseCompanyDetails": False,
        "saveOnlyUniqueItems": True,
        "followApplyRedirects": False,
    }

    # Run the scraper
    run = client.actor("hMvNSpz3JnHgl5jkh").call(run_input=run_input)

    # Fetch the job listings
    jobs = []
    for item in client.dataset(run["defaultDatasetId"]).iterate_items():
        jobs.append({
            "title": item.get("positionName"),
            "company": item.get("company"),
            "location": item.get("location"),
            "salary": item.get("salary"),
            "job_description": item.get("description"),
            "url": item.get("url"),
        })

    return jobs

def store_jobs_in_mongo(jobs):
    """Store the job listings in MongoDB."""
    
    try:
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        db = client['job_database']
        collection = db['jobs_job']
        
        if jobs:
            collection.insert_many(jobs)
            print(f"Inserted {len(jobs)} jobs into MongoDB.")
        else:
            print("No jobs to insert.")
    
    except Exception as e:
        print("Error inserting jobs into MongoDB:", e)

if __name__ == "__main__":
    city = "Lucknow"  
    jobs = scrape_jobs(city)
    store_jobs_in_mongo(jobs)
