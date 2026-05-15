import requests
import sys
from formatting import format_msg
from send_mail import send_mail


#zuna kich pvge jzgd
#muha krve flvm pnsa


def send ( name , website_name = None , to_email = None , verbose = True) :
    
    assert to_email != None

    if website_name is not None:
        msg = format_msg( my_name= name, my_website = website_name )
    else: 
        msg = format_msg(name)
    if verbose :
        print (name , website_name, to_email)

    try:   
        send_mail( text = msg, subject = "Welcome to our family", to_emails = [to_email], html= None)
        sent = True     
    except:
        sent = False
    return sent 

if __name__ == "__main__":
    print(sys.argv)
    name = "none"
    website_name = "none"
    if len(sys.argv) > 3:
        name = sys.argv[1]  
        website_name = sys.argv[2]
        to_email = sys.argv[3]
        response = send_mail(subject = "Welcome to our family", to_emails = [to_email], html = None, text = format_msg(name, website_name))
        print(response)