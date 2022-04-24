# Python script to display IP address using IP stack, and Pythons REQUEST library

To view please visit: http://securemyprivacy.xyz (This is a Google Cloud Engine application that has been mapped onto a custom domain)

Please use this API key to view data: 

IPStack key: 180b793d2a303dc892acf7c53b13d12c


This program consists of a basic python script using a web-framework Flask that renders a HTML page and returns an IP address using 2 techniques.

1: Using defualt Python library "Requests" to see for what IP address was the HTTP request was sent for.

2: Display IP address using the IPstack API which also has 2 options:
1. Either check what is the IP address from where the request is being forwarded from 
2. Pass a specific IP address. 

This application is running from Google Cloud engine so IP stack option 1 displays IP address of the Google Cloud server so we cannot use that. 

I tackled that by sending the IP address returned from Requests to IPStack to get IP address, & Geolocation.

Added:
1. Integrated Google Maps to display the location using IPStacks location tool. 

Stuff to add:
1. Add function to locate IP passed by user.
