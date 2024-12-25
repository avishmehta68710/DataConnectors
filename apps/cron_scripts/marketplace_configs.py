import requests
import sys
import os
import django
import time

sys.path.insert(0, os.path.realpath('/connectors/apps'))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DataConnectors.settings")
django.setup()

from config import Connectors
from amazon.utils import Region

MAX_RETRIES = 5
RATE_LIMIT_DELAY = 70


def main():
	for region in Region.get_list():
		marketplace = Connectors.AMAZON.value
		success = False
		retries = 0
		
		while not success and retries < MAX_RETRIES:
			response = requests.post("http://localhost:8000/marketplace/", data={"name": marketplace, "region": region})
			
			if response.status_code == 201:
				print(f"Marketplace {marketplace} in region {region} created successfully.")
				success = True
			else:
				print(
					f"Failed to create marketplace {marketplace} in region {region}. Retry {retries + 1} of {MAX_RETRIES}.")
				retries += 1
				time.sleep(RATE_LIMIT_DELAY)
		
		if not success:
			print(f"Could not create marketplace {marketplace} in region {region} after {MAX_RETRIES} retries.")


if __name__ == "__main__":
	main()
