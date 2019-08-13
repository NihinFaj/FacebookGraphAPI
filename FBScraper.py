#!usr/bin/env python
# Python Program to mine data from a Brand's Facebook Account

import json
import facebook

# Function that reads the Access Token and Page ID from a 
def funcname(self, parameter_list):
    pass

def main():
    token = "EAARN1Aj3c2wBAIIzqVuqB0GuYMJcXzcg608oYfZCwLaYoXOGMkI3PeWM7Fprd0c2O8sWBZB7H4ZA96n2dGSuYM8fg7uuROsZAAZBU2lIXxdH8ahVuIb0fgjaWb52ZAcfTlp2BZAPMH2yfXc4EN2BfAr1PGyrgZBFIgedrFJQ4A9jSldSdtUYFlZCJkHbHOCOaC9oZD"
    graph = facebook.GraphAPI(token)
    #fields = ['first_name', 'location{location}','email','link']
    profile = graph.get_object('107513663924342',fields='name,fan_count,posts,link')
    #return desired fields
    print(json.dumps(profile, indent=4))

if __name__ == '__main__':
    main()