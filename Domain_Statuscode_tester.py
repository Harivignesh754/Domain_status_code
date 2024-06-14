from bs4 import BeautifulSoup
import requests
import logging
logging.basicConfig(level = "DEBUG",filemode="w",filename="applog.txt",
    format=" %(levelname)s :: %(asctime)s :: %(message)s")
input_file = open("input.txt", "r")
all_lines = input_file.readlines()
output_file = open("output.txt", "w", encoding='utf-8')

for line in all_lines:
    columns = line.split()
    if len(columns) >= 3:
        str_id = columns[0]
        str_domain = columns[1]
        url = columns[2]
    try:
        response = requests.get(url)
        file_name = str_domain.replace(".","_")
        file_obj = open(f"{file_name}.html","w",encoding='utf-8')
        file_obj.write(response.text)
        file_obj.close()
        # soup = BeautifulSoup(response.text,"html.parser")
        # Title = soup.select_one("title")
        # content = Title.text
        
    except Exception :
           logging.debug(f"error in {str_id} {str_domain}",exc_info=True)
           continue
    output_line = str(response.status_code)
    output_file.write(str_id + "\t" + str_domain + "\t" +  output_line + "\t" + file_name + "\t" + "\n")

    
    
