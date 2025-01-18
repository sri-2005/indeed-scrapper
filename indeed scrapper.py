from apify_client import ApifyClient
import csv

# Initialize the ApifyClient with your API token
client = ApifyClient("apify_api_uUrJUttSk1LudLVTFe9xnffsa3CHyz0Om2iJ")

# actor exechttps://github.com/sri-2005/indeed-scrapper/new/mainution
run_input = {
    "position": "web developer",
    "country": "IN",
    "location": "chennai",
    "maxItems": 20,
    "parseCompanyDetails": True,
    "saveOnlyUniqueItems": True,
    "followApplyRedirects": False,
}
# Run the Actor and wait for it to finish
run = client.actor("hMvNSpz3JnHgl5jkh").call(run_input=run_input)
# here i declared the csv file name as indeed scrapper_results.csv
csv_file_name = 'INDEED SCRAPPER_results.csv'
# Fetch and write Actor results to a CSV file
with open(csv_file_name, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    # Write the actor output dataset 
    writer.writerow(['Job Title', 'Company', 'Location', 'page url'])  # Modify as per the actual fields
    # exporting of csv
    for item in client.dataset(run["defaultDatasetId"]).iterate_items():
        writer.writerow([item.get('positionName'), item.get('company'), item.get('location'), item.get('url')])  # Modify as per actual item structure
print(f"Data has been written to {csv_file_name}")
