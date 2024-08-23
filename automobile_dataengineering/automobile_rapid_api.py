import http.client
import csv
import os
import json
import time
from google.cloud import storage

# Function to generate or read the list of VINs (Modify as needed)
def generate_or_load_vin_list():
    vin_list = []
    for i in range(1000):
        vin = f"1HGCM82633A{i:06d}"  # Example: creates VINs like '1HGCM82633A000001'
        vin_list.append(vin)
    return vin_list

# Function to call the API and store data
def fetch_and_store_data(vins, batch_size=100, delay=2):
    csv_file_path = 'D:/automobile_dataengineering/dcar_data.csv'  # File path to store data

    with open(csv_file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        headers_written = False

        for i in range(0, len(vins), batch_size):
            vin_batch = vins[i:i + batch_size]
            for vin in vin_batch:
                conn = http.client.HTTPSConnection("car-api2.p.rapidapi.com")

                headers = {
                    'x-rapidapi-key': "d49860f31fmsh9cbf179f6fd76b4p17f4a9jsn2433b07cbb82",
                    'x-rapidapi-host': "car-api2.p.rapidapi.com"
                }

                conn.request("GET", f"/api/vin/{vin}", headers=headers)

                res = conn.getresponse()
                data = res.read()

                car_data_str = data.decode("utf-8")
                car_data = json.loads(car_data_str)

                if not headers_written:
                    writer.writerow(car_data.keys())
                    headers_written = True

                writer.writerow(car_data.values())
            
            # Delay between batches to avoid API rate limits
            time.sleep(delay)

    # Upload to Google Cloud Storage
    upload_to_gcs(csv_file_path, 'automobiles-api', 'car_data.csv')

    # Clean up local file
    os.remove(csv_file_path)

def upload_to_gcs(source_file_name, bucket_name, destination_blob_name):
    """Uploads a file to the Google Cloud Storage bucket."""
    # Explicitly specify the path to your service account key
    storage_client = storage.Client.from_service_account_json("C:/Users/sahan/Downloads/automobiles-433108-241a25e58b51.json")
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    # Upload the file
    blob.upload_from_filename(source_file_name)

    print(f"File {source_file_name} uploaded to {destination_blob_name}.")

if __name__ == "__main__":
    vin_list = generate_or_load_vin_list()
    fetch_and_store_data(vin_list)  # Run the main function with the list of VINs
