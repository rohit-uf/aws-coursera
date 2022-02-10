# Modern Python Applications on AWS


1. Week 1

## Amazon Web Services

- Services provided by Amazon over the Web.
- Services to develop web applications, Rest API
- Different ways to interact with AWS
  - **REST API**: Documentation can be found online under "*API Reference*" tab for any service 
  - **Management Console**: Web UI provided by Amazon
  - [**AWS Command Line Interface**](#aws-cli): Goes through the Python SDK to interact with the API.

      `aws <options> <sub-command> <parameters>`
  - **AWS SDK**: For code to interact with AWS.

**Objectives**

- Use multiple AWS Services to create an API
- Services like
  - API Gateway
  - Cognito Pool
  - S3 Storage
  - Lambda Functions
  - Simple Notification Service (SNS)
  - STEP Functions
  
> We'll develop a Dragon API in this course

## Cloud 9

- Cloud based IDE by Amazon
- Can directly use AWS CLI


### AWS CLI

Download from [here](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)

1. Via Cloud 9 (has **aws cli** pre-installed) or install on local system
2. Configure with AWS Account's credentials
   -  > aws configure
        - AWS Access Key
        - AWS Secret Access Key

3. By default, these keys are stored in **~/.aws/credentials** file
4. Other parameters like **Region** are stored in AWS Config Path/Folder. Can also provide this with each request
5. Default output format: Can use JSON, YAML, text, ASCII Table

> PROFILE

`aws configure --profile`

Configure a specific profile with a set of keys (Collection of settings). helpful when we want to test the API from multiple roles. 


### AWS SDK

> Python: BOTO3

**Client**
- Low level interface
- maps 1-1 to all service APIs
- Gives response as Python Dictionary
- No Pagination

**Resource**
- High Level Interface
- Object oriented wrapper around **client**
- Expose a subset of AWS API methods
- Gives response as Collection of Python Objects
- Can handle pagination

> Can access the Client from a Resource instance

```py
    client = boto3.resource('s3').meta.client

```


**Sessions**

- Created by default when using a Client/Resource
- Store AWS Credentials

**Credentials**

While making a request, the client searches for AWS Credentials in this order:

1. Parameters passed to Client instance
2. Parameters passed to the session
3. Environment Variables
4. Credentials File (Made when the command `aws configure` runs)
5. IAM Roles : Allows to use Temporary Credentials

> If Cloud 9 is used to interact with aws-cli, it will retrieve the managed credentials.

### Managed Temporary Credentials by Cloud 9

When accessing the AWS-CLI via Cloud 9 (hosted on an Amazon EC2 instance), Cloud 9 manages the credentials automatically for us. This can be toggled here, in Cloud 9 Preferences:

```php
    Preferences->AWS-Settings->AWS->Region->Credentials 
```

- These credentials are replaced (changed) every **5 minutes**

When any request is sent to AWS via CLI, it checks:

1. Whether the **Calling Entity** has appropriate permissions for this request. i.e. it checks the **IAM User's Policy**, who has logged in the Cloud 9 for the relevant permissions.

2. Whether **Cloud 9 Credential Policy** has relevant permissions for this request.

Overlap of these two policies is called: **Effective Access** which determines the effective permissions.


Alternative to Managed Temporary Credentials are:
1. **Attach an IAM Role** to the Instance, running this Cloud 9 IDE
2. Run `aws configure` inside Cloud 9 IDE and set the credentials there


## S3

### S3 Select

- Allows us to query data present in the S3 bucket via SQL-like queries
- Cost effective method, as S3 charges an account based on
  - No of requests
  - Amount of Data
  - Data transferred outside the region
- Data filtering is done by S3, not application code.

## Systems Manager Parameter Store

- Lets us store + retrieve **key-value** pairs
- Used to store the latest information for a key. Example a **bucket_name: bucket_name_value**.
- Can store encrypted, or unencrypted values

## Serverless Application Model

- Short for SAM, is an open-source framework for building serverless applications
- Provides short-hand syntax for specifying Database, API and other things we'd like to interact with.
- A serverless application is a combination of following, to perform distributed tasks:
  - Lambda Functions
  - Event Sources
- Has 2 components
  - AWS SAM Template Specification: DEFINE
  - AWS SAM CLI: BUILD

[Reading Material](https://www.coursera.org/learn/building-modern-python-applications-on-aws/supplement/PRBtr/cloud9-temporary-credentials-aws-sdk-aws-toolkits-aws-sam-python)