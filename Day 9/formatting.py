msg_templete = """ thank you {name} 
for joing this family of our {website_name}"""

def format_msg (my_name = "Unknown", my_website = "website"):
    msg = msg_templete.format(name = my_name, website_name = my_website)
    return msg 

if __name__ == "__main__":
    print(format_msg("John", "Codewithharry"))