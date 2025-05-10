"""
this is the blueprint and here we controller all routes for operation batch
"""
from flask import Blueprint

BATCH_BP = Blueprint("BATCH_BP", __name__)

@BATCH_BP.route("upload_batch", methods=["POST"])
def upload_batch():
    """
    upload batch endpoint
    @body file to upload
    """