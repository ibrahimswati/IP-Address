# Python script to display IP address using IP stack, and Pythons REQUEST library

To view please visit: <securemyprivacy.xyz> (This is a Google Cloud Engine application that has been mapped onto a custom domain)

This program consists of a basic python script using a web-framework Flask that returns an IP address using 2 techniques.

1: Using defualt Python library "Requests" to see for what IP address was the HTTP request was sent for.

2: Display IP address using the IPstack API which also has 2 options:
1. Either check what is the IP address from where the request is being forwarded from 
2. Pass a specific IP address. 

This application is running from Google Cloud engine so IP stack option 1 displays IP address of the Google Cloud server so we cannot use that. 

I tackled that by sending the IP address returned from Requests to IPStack to get IP address, & Geolocation.

Stuff to add:
1. Display MAC address of user
2. Display device type by checking for default MAC address
3. Integrate Google Maps to display the location using IPStacks location tool. 
