import requests
import csv

token = 'rBBl1gxdbI8UahEHr01uP8K3dBy0Igl95yXjf3kf'

groupUrl = 'https://sunkingpaygo.zendesk.com/api/v2/groups'

user = 'ian.kamanda@greenlightplanet.com' + '/rBBl1gxdbI8UahEHr01uP8K3dBy0Igl95yXjf3kf'

userMail = user + token

def make_request(url):
    # Make the request to the given URL
    response = requests.get(url)

    # Process the response as needed (you can customize this part)
    data = {
        'url': url,
        'status_code': response.status_code,
        'content': response.text
    }

    return data

def main():
    # List of URLs to request
    urls = [
        'https://sunkingpaygo.zendesk.com/',
        'https://example.org',
        # Add more URLs as needed
    ]

    # Store the results in a list of dictionaries
    results = []

    # Make requests for each URL
    for url in urls:
        result = make_request(url)
        results.append(result)

    # Save the results to a CSV file
    csv_filename = 'output.csv'
    fieldnames = ['url', 'status_code', 'content']

    with open(csv_filename, 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        
        # Write the header
        writer.writeheader()

        # Write the data
        writer.writerows(results)

    print(f'Results saved to {csv_filename}')

if __name__ == "__main__":
    main()