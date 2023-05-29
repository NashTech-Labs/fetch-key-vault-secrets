# fetch-key-vault-secrets

This techhub template consists of the python script to fetch key vault secrets defined in the file and will give all the secret values in a file

## Steps for Execution

- clone the repository
- `pip install -r requirements.txt`
- add the vault name (from where to retreive the secret) and secret name (the secret you want to retreive) in the secret_input.txt file
  - vault_name,secret_name
- export the AZURE_CLIENT_ID, AZURE_CLIENT_SECRET_ID, AZURE_TENANT_ID using the following command:
  - `export AZURE_CLIENT_ID='<azure client id>'`
  - `export AZURE_CLIENT_SECRET_ID='<azure client secret>'`
  - `export AZURE_TENANT_ID='<azure tenant id>'`
- execute the python script using the command
  - `python download-git-repo-as-zip.py`

It will create a secret_output.txt file consisting of the `<vault name>,<secret name>,<secret value>`
