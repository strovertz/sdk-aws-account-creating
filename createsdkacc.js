public void awsCreateAccount(){
Region region = Region.US_WEST_2;
AwsBasicCredentials.create("", "");
AwsBasicCredentials awsBasicCreds = AwsBasicCredentials.create("", "");
ServiceCatalogClient serviceCatalogClient = ServiceCatalogClient.builder()
.region(region)
.credentialsProvider(StaticCredentialsProvider.create(awsBasicCreds))
.build();
ProvisioningPreferences provisioningPreferences = ProvisioningPreferences.builder()
.stackSetAccounts("")
.build();
ProvisionProductRequest provisionProductRequest = ProvisionProductRequest.builder()
.productId("prod-2au6asfsdfsfds")
.provisioningArtifactId("pa-dsfdsfdfsfs")
.provisionedProductName("CatalogFortest-Custom-Account")
.provisioningParameters(ProvisioningParameter.builder()
.key("SSOUserEmail")
.value("test@example.com")
.build(),
ProvisioningParameter.builder()
.key("SSOUserFirstName")
.value("test")
.build()
, ProvisioningParameter.builder()
.key("SSOUserLastName")
.value("test")
.build()
, ProvisioningParameter.builder()
.key("ManagedOrganizationalUnit")
.value("OU_Name (OU_ID)")
.build()
, ProvisioningParameter.builder()
.key("AccountName")
.value("test-Custom-Account")
.build()
, ProvisioningParameter.builder()
.key("AccountEmail")
.value("test@example.com")
.build())
.build();
ProvisionProductResponse provisionProductResponse = serviceCatalogClient.provisionProduct(provisionProductRequest);
System.out.println(provisionProductResponse.toString());
}