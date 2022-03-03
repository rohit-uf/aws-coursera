# Optimizations


## API Gateway

1. Edge-optimized endpoints: Regional-Edge locations. 

**Point of Presence**: Physical points in the world, where ISP's are connected with AWS's ISP. AWS can put hardware here
- These are called Edge-Locations
- 6 services are available here
- One service called `Amazon Cloudfront` -> CDN -> Caching Service : Provides (Data, Audio, Video, APIs)
- It sits in front of the API, and routes an incoming request directly to the Regional endpoint via **AWS-Backbone**

2. Response Caching

- Cache the response in API Gateway
- Cache Capacity (Size of cache storage)
- If cache capacity is changed -> Delete existing cache -> Create new cache with the new capacity
- Dedicated Cache instance is created
- By default, GET methods can be cached
- Request Parameters can also be Cached in `Method Request` section

Can be used as a Proxy for other services, without using Lambda
- Storing data in S3
- Querying from DynamoDB

3. HTTP API

- Cheaper and faster than REST API
- Can be used to proxy request to Lambda or any HTTP endpoint
- Support CORS
- OAuth2.0 and OpenID
- Private Integration
- Does not provide full control like transformation, validation etc over Request and Response

### Lambda

Lambda @ Edge -> Uses Cloudfront to run Lambda closer to the origin of the request

**Lambda Layers**

- Mechanism to externally package dependencies
- These layers can be shared among multiple lambda functions
- Need **Layer Usage Permissions**
- Lambda Function can use **5 Layers** at max, at one time
- Size limit: 250MB Unzipped
- On runtime, layers are copied to /opt folder

[Best Practices](https://docs.aws.amazon.com/lambda/latest/dg/best-practices.html)
- Small package size
- Minimize dependencies complexity
- Avoid recursive code
- Set concurrent execution limit to 0 -> throttle all invocations
- Reuse execution context (Dont keep sensitive information)
- Load test to determine optimal Timeout value
- Use [AWS Lambda Power Tuning](https://serverlessrepo.aws.amazon.com/applications/arn:aws:serverlessrepo:us-east-1:451282441545:applications~aws-lambda-power-tuning)
