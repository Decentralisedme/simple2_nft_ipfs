# simple2_nft_ipfs

Very simple approach to complete the process from smart conract deployment to OpenSea publication:
1) Smart contract to mint an ERC721 token and set the token URI: ```SimpleCollectable2.sol```
2) Deploy the smart contract: ```deploy_and_create.py```
3) Create the metadata for your token including the URI obtained by uploading to IPFS the digital asset: ```create_metadata.py```
4) Publish it to OpenSea: ```set_toek_uri.py```

As regard IPFS
1) To run an IPFS node: https://docs.ipfs.io/install/command-line/#official-distributions. 
You can check by ipfs --version
2) To initialise ipfs repository: ipfs init. You need to this only the first time, otherwise you ll change you keys
3) To run the node: ipfs daemon. 
This will also gigve your WebUI
4) To upload the file follow: https://docs.ipfs.io/reference/http/api/#api-v0-add. 
The file/image you have upload via cmd line you won't see it in the webUI
5) To have the file in your WebUi: https://github.com/ipfs/ipfs-webui/issues/897
