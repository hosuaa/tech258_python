# API (Application Programming Interface)

## What are APIs

APIs are mechanisms that enable two software components to communicate with each other using a set of definitions and protocols. The software components are the 'applications' and the mechanism is the 'interface', hence 'Application programming interface'. 

APIs are usually explained in terms of a client and a server. The application sending the request is called the client, and the application sending the response is called the server. 

![image](api_data_transfer.png)

APIs can be used to integrate new applications with existing software systems. Since we are reusing existing code, this can dramatically increase development speed and so APIs are very popular.  

There are 4 different kinds of API architectures:
1. **SOAP**:
SOAP stands for Simple Object Access Protocol, where the client and server exchange messages using XML.<br>
While outdated, SOAP is still sometimes used since compared to REST, SOAP is Language, platform, and transport independent (REST requires use of HTTP) Works well in distributed enterprise environments (REST assumes direct point-to-point communication). For example, SOAP is used in bank transfers. 
2. **RPC**:
RPC stands for Remote Procedure Call, where the client completes a function on the server and the server sends the output back to the client.<br>
RPC allows developers to call remote functions in external servers as if they were local to their software. For example, you can add chat functionality to your application by remotely calling messaging functions on another chat application.
3. **Websocket**:
A web API that uses JSON objects to pass data. The communication between the server and the client is two-way, so the server can send callback messages to the client which allows for code execution in response to an event For example, run this code every time a user presses this key on their keyboard.
4. **REST**: REST stands for Representational State Transfer. It is another web API where the client sends requests to the server as data and the server uses this data to run functions and return output data back to the client.

## REST and RESTful APIs

An API is 'RESTful' if it uses HTTP requests to access and use data. The data transmitted can be delivered over HTTP in many different formats: JSON, HTML, XLT, Python or plaintext to name a few. For REST APIs, there are some guidelines that they must follow:

1. A client-server architecture made up of clients, servers, and resources, with requests managed through HTTP.
2. Stateless client-server communication, so no client information is stored between get requests and each request is separate and unconnected.
3. Cacheable data that streamlines client-server interactions.
4. A uniform interface between components so that information is transferred in a standard form. This requires that:
    - resources requested are identifiable and separate from the representations sent to the client.
    - resources can be manipulated by the client via the representation they receive because the representation contains enough information to do so.
    - self-descriptive messages returned to the client have enough information to describe how the client should process it.
    - hypertext/hypermedia is available, meaning that after accessing a resource the client should be able to use hyperlinks to find all other currently available actions they can take.
5. A layered system that organizes each type of server (those responsible for security, load-balancing, etc.) involved the retrieval of requested information into hierarchies, invisible to the client.
6. Code-on-demand: the ability to send executable code from the server to the client when requested, extending client functionality. 

These guidelines are quite strict so many APIs do not conform to every element of REST, and so RESTful APIs are useful for following standards while remaining flexible and lightweight. (**1, 2 and 3** are most commonly implemented)

## HTTP

HTTP stands for Hypertext Transfer Protocol and is an application layer protocol designed to transfer information between networked devices and runs on top of other layers of the network protocol stack.

![image](tcpip-stack.png)

The application layer contains the communications protocols, including HTTP, and interface methods used in process-to-process communications across an Internet Protocol (IP) computer network.

### HTTPS

HTTPS stands for Hypertext Transfer Protocol Secure and is an extension of HTTP. It implements encryption to ensure secure communication which is especially useful over the internet. It uses Transport Layer Security (TLS) or, formerly, Secure Sockets Layer (SSL) for encryption and so the protocol is also referred to as HTTP over TLS or HTTP over SSL.

A typical flow over HTTP involves a client machine making a request to a server, which then sends a response message. Some HTTP methods include GET, PUT and DELETE

### HTTP request

![image](HTTP_request.png)

A typical HTTP request contains:

1. HTTP version type<br>
E.g. HTTP/1.0, HTTP/1.1 ...
2. a URL<br>
E.g. www.google.com
3. an HTTP method/verb
E.g. GET, POST<br>
A ‘GET’ request expects information back in return (usually in the form of a website), while a ‘POST’ request typically indicates that the client is submitting information to the web server (such as form information, e.g. a submitted username and password).
4. HTTP request headers<br>
HTTP headers contain text information stored in key-value pairs. These headers communicate core information, such as what browser the client is using and what data is being requested.
![image](http-request-headers.png)
5. Optional HTTP body<br>
The body of a request is the part that contains the actual information the request is transferring such as any information being submitted to the web server e.g. username and password, or any other data entered into a form.

### HTTP response

![image](HTTP_response.png)

A typical HTTP response contains:

1. an HTTP status code<br>
3 digit codes used to indicate whether a successful HTTP request has been completed. There are 5 kinds:
   - 1xx Informational
   - 2xx Success
   - 3xx Redirection 
   - 4xx Client Error 
   - 5xx Server Error
2. HTTP response headers
3. optional HTTP body














