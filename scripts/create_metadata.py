from brownie import SimpleCollectable2, config, network
from metadata.metadata_sample import metadata_template
from scripts.helpful_scripts import get_cycle
from pathlib import Path
import requests
import json


def main():
    simp_collectable = SimpleCollectable2[-1]
    number_of_collectables = simp_collectable.tokenCounter()
    print(f"number of Collectables: {number_of_collectables}")

    for token_id in range(number_of_collectables):
        cycle = get_cycle(simp_collectable.tokenIdToCycle(token_id))
        metadata_file_name = (
            f"./metadata/{network.show_active()}/{token_id}-{cycle}.json"
        )
        # METADATA
        collectable_metadata = metadata_template
        print(f"{metadata_file_name}: NEW Metadata File")
        collectable_metadata["name"]: cycle
        collectable_metadata["description"] = f"Me doing my virtual {cycle}!!!"
        print(f"MetaData Attributes: {collectable_metadata}")
        # IPFS
        # 1- set image in folder
        # 2- set Path
        image_path = "./img/" + cycle.lower().replace("_,", "-") + ".png"
        # 3- upload
        image_uri = upload_to_ipfs(image_path)
        collectable_metadata["image"] = image_uri
        with open(metadata_file_name, "w") as file:
            json.dump(collectable_metadata, file)
        upload_to_ipfs(metadata_file_name)


def upload_to_ipfs(filepath):
    # 1- IMG BINARY
    with Path(filepath).open("rb") as fp:
        image_binary = fp.read()

        # 2 UPLOAD to IPFS
        ipfs_url = "http://127.0.0.1:5001"
        endpoint = "/api/v0/add"

        # 3 POST REQUEST
        response = requests.post(ipfs_url + endpoint, files={"file": image_binary})

        #  4 GET HASH
        ipfs_hash = response.json()["Hash"]

        # 5 FileName
        filename = filepath.split("/")[-1:][0]

        # 6 URI
        image_uri = f"https://ipfs.io/ipfs/{ipfs_hash}?filename={filename}"
        print(f"IMAGE URI: {image_uri}")
        return image_uri
