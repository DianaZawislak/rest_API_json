# REST API Processing JSON Data Response and Testing

### Name: Diana Zawislak

### UCID: DZ29

## Introduction

The purpose of this unit is to introduce you to JSON, making requests, and testing responses.

## Unit Video - [Watch Here](https://youtu.be/xoU90Ga7guI)

## Steps to Complete the Assignment

1. Put your name and UCID at the top of this file where indicated
2. Clone this repo and run pip install -r requirements.txt to install the dependencies
3. Signup for RapidAPI - [here](https://rapidapi.com/auth/sign-up)
4. Subscribe to the Geo Cities api here - [here](https://rapidapi.com/wirefreethought/api/geodb-cities/)
5. Put that Geo Cities API key in the .env file
6. Run pytest to see that the response is saved in logs/api_response.log
7. Look around at the different API and subscribe to at least 2 other API (Use the free ones but be careful of the
   monthly/daily request limit) and write
   tests to verify the contents of the response. Your first is for Cities API and is the same as mine but with your own
   code.

## Assignment Tasks

For this assignment you need to SIGN UP to get your own key for
the [Geo Data API](https://rapidapi.com/wirefreethought/api/geodb-cities/). and put it in your .env file

1. Make a request that retrieves a list of cities from the cities api above.  Use my teacher test as an example / same thing -  whooo! free 20 points
2. Create a python dictionary and turn it into a json string and test that it is a json string
3. Create a json string and turn it into a python dictionary and test that it is a dictionary
4. Signup for another API and write your own test to verify that the data you receive is what you expect
5. Signup for another API and write your own test to verify that the data you receive is what you expect

You get 20 points for each task test.

## Submission Instructions
Submit the link to your github classroom repo to Canvas i.e. the link to what you are probably looking at right now
## Required Readings

1. [Working with JSON](https://www.geeksforgeeks.org/working-with-json-data-in-python/)
2. [Tutorial on the http library we are using now](https://www.askpython.com/python-modules/http-module)
3. [Extensive Set of JSON Python Tutorial that solves problems you will eventually have](https://pynative.com/python/json/)

### References and Articles used for Assignment - Good articles and required if you don't understand what unit tests or logging is. Logging and unit testing are fundamental skills for development and Devops

1. [Python dotenv file reading library](https://pypi.org/project/python-dotenv/)
2. [Geo Cities Data](https://rapidapi.com/wirefreethought/api/geodb-cities/)
3. [JSON Python Library](https://docs.python.org/3/library/json.html)
4. [JSON Project Homepage](https://www.json.org/json-en.html)
5. [Python HTTP Request Libary - Alternate Python Library](https://www.datacamp.com/tutorial/making-http-requests-in-python)
6. [Using Rate Limiter](https://akshayranganath.github.io/Rate-Limiting-With-Python/#:~:text=control%20the%20rate%20of%20requests,the%20limit%20are%20generally%20documented.)
