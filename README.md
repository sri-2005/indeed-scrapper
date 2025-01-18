# indeed-scrapper
The Indeed Scraper is a Python-based tool that extracts job listings from Indeed, gathering details like title, company, location, salary, description, and date posted. It helps job seekers, researchers, and recruiters analyze job market trends and track opportunities.

Here’s a stepwise breakdown of what the script does, formatted for inclusion in a GitHub README file:  

 Steps in the Indeed Scraper Script  

1. Import Required Libraries  
    `apify_client` for interacting with the Apify API.  
    `csv` for writing job data into a CSV file.  

2. Initialize ApifyClient  
   The script initializes the Apify client with an API token to authenticate API requests.  

3. Define Scraping Parameters  
   Job search criteria such as position, country, location, and maximum job listings to fetch are set in `run_input`.  

4. Execute the Apify Actor 
    The script runs the Apify actor (`hMvNSpz3JnHgl5jkh`) with the defined parameters and waits for execution to complete.  

5. Create and Open a CSV File  
    A CSV file (`INDEED SCRAPPER_results.csv`) is created to store job data.  

6. Write Header Row in CSV  
    The script writes column headers: `Job Title`, `Company`, `Location`, and `Page URL`.  

7. Fetch and Write Job Listings  
   The script iterates over the retrieved job data and writes relevant details into the CSV file.  

8. Print Confirmation Message  
   After successfully writing data, a confirmation message is displayed.  

This structured breakdown helps users understand how the script functions step by step. Would you like to add installation instructions for dependencies as well? 🚀
