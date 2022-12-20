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

## Managing container:

Create Docker container
Build image
The following command builds an image boto3-image, you can found more commands at Docker Documentation.
```bash
docker build . --tag=boto3-image
```
Run container
Run the container using the image created in the previous command. Check the option -v to fix the mapping. In the DockerFile, there is a variable VOLUME which points to the mapped folder in the Docker (in this case VOLUME=/local-git), change it if you want to avoid python errors like missing module logic.
```
docker run -itd --rm --name boto3 --hostname boto3 -v C:\marko\GitHub\boto3:/local-git boto3-image
```
Inside our container
```
docker exec -it boto3 bash
```
About the container
The container uses latest centOS, installs python3-pip library in order to install virtualenv using pip3, it's also work if you change the OS.

It also creates a user of your choice (default is centos) which is used to run the python scripts.

Virtual environment with Python 3.6 is created and the path to the binaries in the virtual environment's folder is added to the $PATH. With that, running command python will use Python3.6 or whichever Python version is installed in the virtual environment.

Example
In folder logic here is a Python example package and file which use library boto3 to list all buckets in the AWS S3.
