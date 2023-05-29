from azure.keyvault.secrets import SecretClient
from azure.identity import ClientSecretCredential
import os


# fetch secret value from the key vault
def fetch_key_vault_secret(vault_name:str, secret_name: str) -> str:
    """Fetch the secret value from the key vault

    Args:
        secret_name (str): name of the secret to fetch

    Returns:
        str: value of the secret (in plaintext format)
    """
    print(f'Fetching {secret_name} secret value from {vault_name} \n')
    
    # Retrieve the IDs and secret to use with ServicePrincipalCredentials
    tenant_id = os.environ["AZURE_TENANT_ID"]
    client_id = os.environ["AZURE_CLIENT_ID"]
    client_secret = os.environ["AZURE_CLIENT_SECRET_ID"]

    credential = ClientSecretCredential(
        tenant_id=tenant_id,
        client_id=client_id,
        client_secret=client_secret,
    )

    client = SecretClient(
        vault_url=f'https://{vault_name}.vault.azure.net/',
        credential=credential
    )

    secret = client.get_secret(secret_name)
    print('Successfully fetched secret')
    return secret.value


def main():
    file_content=[]

    try:
        with open('secrets_input.txt', 'r') as file:
            file_content=file.readlines()
    except FileNotFoundError:
        print(f'secret_input.txt not found. Try again after creating the file')
        exit

    for single_line in file_content:
        line_without_newline=single_line.strip()
        
        vault_name = (line_without_newline.split(','))[0]
        print(f'Vault Name: {vault_name}')
        secret_name = (line_without_newline.split(','))[1]
        print(f'Secret Name: {secret_name}')
        # vault_name = input('Enter vault name to retreive secret from: ')
        # print(f'Secret name: {vault_name}')
        
        # secret_name = input('Enter secret name to retreive: ')
        # print(f'Secret name: {secret_name}')
        
        secret_value = fetch_key_vault_secret(vault_name=vault_name,secret_name=secret_name)
        
        try:
            with open('secrets_output.txt', 'a') as file:
                file.writelines(f'{vault_name},{secret_name},{secret_value}')
                print(f'{secret_name} secret value written to the secret_output.txt file')
        except Exception as e:
            print('Error writing the file')
            print(e)
            exit
            
        print('--------------------------------------------------------')
    

if __name__=="__main__":
    main()