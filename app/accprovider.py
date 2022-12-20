import boto3

session = boto3.Session(profile_name='access-yes')

client = boto3.client('servicecatalog')
prod_id = client.search_products_as_admin(Filters={'FullTextSearch': [ 'AWS Control Tower Account Factory',]}, SortBy='Title')["ProductViewDetails"][0]["ProductViewSummary"]["ProductId"]
pa_id = client.describe_product_as_admin(Id=prod_id)["ProvisioningArtifactSummaries"][-1]["Id"]

def create_account(account_name, account_email):
  try:
    response = client.provision_product(
      AcceptLanguage='en',
      ProductId= prod_id,
      ProvisioningArtifactId= pa_id,
      ProvisionedProductName=account_name,
      ProvisioningParameters=[
          {
              'Key': 'SSOUserEmail',
              'Value': 'STRING'
            },
            {
              'Key': 'SSOUserFirstName',
              'Value': 'Gleison'
      
            },
            {
              'Key': 'SSOUserLastName',
              'Value': 'Pires'
            },
            {
              'Key': 'ManagedOrganizationalUnit',
              'Value': 'OU_NAME (OU_ID)'
            },
            {
              'Key': 'AccountName',
              'Value': account_name
            },
            {
              'Key': 'AccountEmail',
              'Value': account_email
            }
      ],
      Tags=[
          {
              'Key': 'Provisioned',
              'Value': 'PySDK'
          },
      ]
    )
    if response['ResponseMetadata']['HTTPStatusCode'] == 200:
      return True
    else: 
      return False
  except Exception as e:
    print(str(e))
    return False
  
def main():
  account_name = input('Insira um nome para a conta: ')
  account_email = input('Insira um email para a conta: ')

  create_account(account_name, account_email)

if __name__ == "__main__":
  main()
