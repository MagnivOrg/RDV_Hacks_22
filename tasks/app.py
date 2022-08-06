import requests
from magniv.core import task

URL = "https://warrenlotas.com/"

@task(schedule="@daily")
def main():
	print("Hello")
	
	# Get website
	req = requests.get(URL)

	# Check if something dropped
	did_not_drop = "SITE IS CLOSED" in req.text

	print("Drop happened" if not did_not_drop else "No drop")

if __name__ == '__main__':
	main()