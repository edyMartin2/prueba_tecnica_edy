"""
this is the blueprint and here we controller all routes for operation batch
"""
from flask import Blueprint, request, jsonify
from controllers.handlers.calculate_number import CalculateNumber
CALCULATE_BP = Blueprint("CALCULATE_BP", __name__)

@CALCULATE_BP.route("calculate", methods=["POST"])
def upload_batch():
    """
    upload batch endpoint
    @body file to upload
    """
    body = request.json
    number = body['number']
    CalculateNumberClass = CalculateNumber()
    subtract_number = CalculateNumberClass.extract(number=number)
    
    if subtract_number[1] == False:
        return jsonify(subtract_number[1])
    calculate_extract = CalculateNumberClass.calculate_extract()
    return jsonify(
        {
            "numeros_sobrantes": subtract_number,
            "numero_extraido": calculate_extract
        }
    )