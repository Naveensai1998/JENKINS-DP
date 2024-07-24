# -*- coding: iso-8859-1 -*-
#!/usr/bin/python

"""
This Python script calls CretaV6 API to download DICOM (DCM) files.

It does not take any input parameters but expects some environment variables to be set.

Modifications:
- Added comments to explain functionalities of core functions.
- Improved variable naming for better readability (e.g., `creta_revision_names` instead of `creta_revisions`).
- Removed unused comments about `sys.exit(1)`.
"""

import requests
import os
import logging
import shutil


# Define Creta API endpoint URL
REST_URL = "https://creta-api-dev.rd.corpintra.net:8602/odata/"

# List to store revision names that weren't found
unfound_revisions = []

# Configure logging level (INFO for informational messages)
logging.basicConfig(level=logging.INFO)


def get_token(username, password):
    """
    Retrieves an authorization token from the Creta API using credentials.
    """

    logging.info("Getting token")
    url = REST_URL + "Connect"
    payload = {
        "Username": username,
        "Password": password,
    }
    response = requests.post(url, json=payload)

    if response.status_code == 200:
        result = response.json()
        token = result['value']
        logging.info("Token fetched successfully")
        return token
    else:
        logging.error("Unable to fetch token")
        # Exit the script if token retrieval fails
        return None


def get_project_suid(project_name):
    """
    Gets the unique identifier (SUID) for a specified Creta project.
    """

    logging.info(f"Get Project Suid for project: {project_name}")
    url = REST_URL + "Areas('01_00')/Creta.Projects()?%24filter=Name%20in%20%28%27" + project_name + "%27%29"
    response = requests.get(url, headers={'Authorization': token})

    if response.status_code == 200:
        result = response.json()
        project_suid = result['value'][0]["Suid"]
        logging.info(f"Project Suid: {project_suid}")
        return project_suid
    else:
        logging.error(f"Cannot fetch project suid for {project_name}")
        logging.error(response.reason)
        return None


def get_revision_suid(project_suid, revision_name):
    """
    Gets the SUID for a particular revision within a Creta project.

    If the revision isn't found, it logs an error and adds the revision name to the `unfound_revisions` list.
    """

    logging.info(f"Get Revision Suid for revision: {revision_name}")
    url = REST_URL + "Projects('" + project_suid + "')/Creta.Revisions()?%24filter=Name%20in%20%28%27" + revision_name + "%27%29"
    response = requests.get(url, headers={'Authorization': token})

    if response.status_code == 200:
        result = response.json()
        if result['value'] != []:
            revision_suid = result['value'][0]["Suid"]
            logging.info(f"Revision Suid: {revision_suid}")
            return revision_suid
        else:
            logging.error(f"Creta revision not found: {revision_name}")
            unfound_revisions.append(revision_name)
            return None
    else:
        logging.error(f"Cannot fetch revision suid for {revision_name}")
        logging.error(response.reason)
        unfound_revisions.append(revision_name)
        return None


def export_dcm(revision_suid, save_path):
    """
    Downloads a specific revision (DCM format) and saves it to the designated path.
    """

    post_json = {
        "Encoding": "Windows_1252",
        "AddAxis": True,
        "Filter": {
            "Type": "Label",
            "FilterBy": 
        }   
    }
