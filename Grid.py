# File name: Grid.py
# Author: Eduardo Nunez
# Date created: 3/24/2019
# Python Version: 3.7


# Standard library.
from xml.dom import minidom
import csv

# Third party package.
import requests


def main():

    #  This block will call and create the XML file.
    url = 'https://raw.githubusercontent.com/Gridium/interview/master/pge_electric_interval_data.xml'
    resp = requests.get(url)
    with open('Gridium.xml', 'wb') as f:
        f.write(resp.content)

    #  Using MINIDOM to parse the XML file.
    xmldoc = minidom.parse('Gridium.xml')

    # This will creat the CSV file where the data will be written.
    with open('gridium.csv', 'w', newline='') as f:
        fieldnames = ['Usage Point', 'Occurred', 'Value']
        thewriter = csv.DictWriter(f, fieldnames=fieldnames)
        thewriter.writeheader()

        #  Getting the data from the desired elements and writing the data to the CSV file.
        occurred = xmldoc.getElementsByTagName('published')
        for o in occurred:
            thewriter.writerow({'Occurred' : o.childNodes[0].data})
        value = xmldoc.getElementsByTagName('value')
        for v in value:
            thewriter.writerow({'Value' : v.childNodes[0].data})

        # Pulling the attribute from the tag and writing the data the the CSV file.
        up = xmldoc.getElementsByTagName('UsagePoint')
        for u in up:
            thewriter.writerow({'Usage Point': u.getAttribute("xmlns")})


if __name__ == "__main__":
    main()



