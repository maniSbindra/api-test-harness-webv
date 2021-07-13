# API Test Harness using webvalidate

This repository has code supporting the blog post [Ensuring code changes do not break Microservice REST API, during Pull Request validation](https://techcommunity.microsoft.com/t5/apps-on-azure/ensuring-code-changes-do-not-break-microservice-rest-api-during/ba-p/2526554)

## The Book Service Code

The sample Book service code, the /BooksApi folder has been taken from [Book Service API](https://github.com/dotnet/AspNetCore.Docs/tree/main/aspnetcore/tutorials/first-mongo-app/samples/3.x/SampleApp), and then tweaked for the purpose of creating the API test Harness

## Steps to setup the API test harness

Create an Azure Pipeline using the [BooksApi/dockerComposeBooksApiTest.yml](https://github.com/maniSbindra/api-test-harness-webv/blob/master/BooksApi/dockerComposeBooksApiTest.yml) file. Next configure this pipeline to execute as part of main branch build validation.
