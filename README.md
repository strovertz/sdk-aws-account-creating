# Using AWS SDK with Boto3 to create and deploy an AWS Account with Control Tower + Service Catalog
 
## Creating an AWS Account with Python3 using boto3
This repo creates a Docker container with AWS credentials, boto3, python3 and our python file.

## Prerequisities:
An IAM User, AWS Key ID and Secret Key.

You also needs that account have Control Tower Enabled and an Catalog with an AWS Control Tower Account Factory Portfolio.

## Using AWS credentials:
Setup ur credentials using the aws/credentials file.

By default AWS SDK and CLI uses ~/.aws/credentials to authenticate and authorize.

## Pip requirements file:
The file docker/requirements.txt holds a list of python packages pip should install inside the image. One package per line is the format. In this case, we just need the Boto3 lib.

## Variables in DockerFile:
Change the variables as needed.

# Container management:

Create Docker container

### Build image
The following command builds an image boto3-image, you can found more commands at Docker Documentation.
```bash
docker build . --tag=boto3-image
```
### Run container
Run the container using our created image. Please check the option -v (volume) to fix the mapping. In the DockerFile, there is a variable VOLUME which a string value, change to solve possbile problems.
```
docker run -itd --rm --name boto3 --hostname boto3 -v CHANGE_HERE
```
### Inside our container
```
docker exec -it boto3 bash
```
These container uses centos:latest, installs python3-pip library in order to install virtualenv using pip3, it's also work if you change the OS.

It also creates a user of your choice (default is centos) which is used to run the python scripts.

- Here is a Python example package and file which use library boto3 to create an aws account using AWS Service Catalog + AWS Control Tower.
