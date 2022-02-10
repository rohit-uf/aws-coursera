# API Gateway

Service to create, publish, maintain, monitor and secure REST, HTTP and WebSocket APIs.

### Websocket API

Operates using *lower level protocol* based on **sockets** and **ports**. It is
- Vertically scalable
- Bi-directional
- Used for real time scenarios like chatting, video calling etc.

### HTTP APIs

- RESTful APIs with **Lower Latency** + **Lower cost** than REST API

Can use the Gateway to re-direct an incoming request to:
- AWS Lambda Function
- HTTP/HTTPS Endpoint
- Lightweight + Low latency compared to REST API
- Subset of REST API Functionality
- Cheaper compared to REST API
- Supports **Application Load Balancer**
- Can not use API Keys, Caching, Testing, no request validation or transformation

### REST API
- Fast
- Stateless
- Horizontally Scalable
- Standard, Dependable
- Have more latency because of significant overhead
- Does not support **Application Load Balancer**

Further it provides features like:
1. Canary Deployments
2. Cloudtrail Integration
3. Cloudwatch Integration
4. Request throttling
5. Custom domain name
6. Integration with other AWS Services
7. Different Endpoints
   1. **Edge Optimized endpoints**: Best for Geographically distributed endpoints
   2. **Regional Endpoints**: Intended to be used in the same region as the API Gateway
   3. **Private Endpoints**: Exposed through interface VPC endpoints and allows a client to securely access private API Resources inside a **VPC**.


## Concepts

- **Resource**: Abstract concept, a thing for the backend to consume
- **Methods**: Interact with the resource
- **Integration**: Map the incoming request to an AWS Service / another endpoint 

CLIENT --> METHOD REQUEST --> INTEGRATION REQUEST --> API ENDPOINT
CLIENT <-- METHOD RESPONSE <-- INTEGRATION RESPONSE <-- API ENDPOINT

Can apply Data transformations at Request + Response points


## Validate 

Requests/Responses can be validated with **Models**

- Define structure (schema) for the request/response body
- Properties of the payload + Type of each property
- Can be defined at the **Method level**, not the **Resource level**
- Written in JSON

## Trasformation

Requests/Responses can be transformed with **Mappings**

- Applied to integration request/response
- Defined at the **Method Level**, not the **Resource Level**
- Written in VTL (Velocity Template Language)
- Supports JSON(default)/XML data as incoming data
- Supports
  - Conditional Statements
  - Injection of new values

## Blogs

- [Microservices](https://docs.aws.amazon.com/whitepapers/latest/microservices-on-aws/api-implementation.html)
- [API Management](https://aws.amazon.com/api-gateway/api-management/)


