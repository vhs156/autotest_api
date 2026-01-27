import xml.etree.ElementTree as ET

xml_data = """
<person>
    <id>1</id>
    <first_name>John</first_name>
    <last_name>Doe</last_name>
    <age>30</age>
    <email>joe@gmail.com</email>
    <address>
        <street>Lubyanka</street>
        <city>Moscow</city>
        <zipcode>100100</zipcode>
    </address>
</person>
"""

root = ET.fromstring(xml_data)

print("User age:", root.find('age').text)
print("User email:", root.find('email').text)

