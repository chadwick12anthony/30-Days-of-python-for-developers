import requests
import sys
from formatting import format_msg
from send_mail import send_mail

# def send ( name = "known", website_name = "New website"):
#     msg = format_msg( my_name= name, my_website = website_name )
#     return msg 

def send ( name , website_name = None , verbose = True) :
    if website_name is not None:
        msg = format_msg( my_name= name, my_website = website_name )
        # print(format_msg ("Unkown", "Unknown"))
    else: 
        msg = format_msg(name)
    if verbose :
        print (name , website_name)
         
    r = requests.get("http://httpbin.org/json")
    print(r)
    if r.status_code == 200:
        return r.json()
    else:
        return "There was an error"
    
if __name__ == "__main__":
    print(sys.argv)
    name = "none"
    website_name = "none"
    if len(sys.argv) > 2:
        name = sys.argv[1]  
        website_name = sys.argv[2]

        print(send(name, website_name, verbose=True))

#zuna kich pvge jzgd
#muha krve flvm pnsa


