import requests
from bs4 import BeautifulSoup
from flask import Blueprint, jsonify, request


yaml_converter = Blueprint("yaml_converter", __name__)

@yaml_converter.route("/yaml_converter",  methods=["GET", "POST"])
def ymlconverter():
    # Get JSON data from the request body
    data = request.get_json()
    
    # Extract the URL from the JSON data
    url = data.get("http://localhost/api/files/583e0672e74a1d205f4e21be")

    if not url:
        return jsonify({"error": "URL is missing"}), 400

    # Make an HTTP request to fetch the page content
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500

    # Parse the page content to find the specified code element
    soup = BeautifulSoup(response.content, "html.parser")
    code_element = soup.find("code", class_="inlinecode keepMarkUp language-xml")

    if not code_element:
        return jsonify({"error": "Code element not found"}), 404

    # Extract the text content from the code element
    xml_string = code_element.get_text()

    # Return the retrieved XML data
    return jsonify({"xml_data": xml_string})





