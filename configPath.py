import os

root_directory = ''
output_main = ''
file_type = 'pdf' #png, jpg, jpeg, doc, pdf, txt, xls, xlsx, zip, mp4, mpeg, mov, 

if not os.path.exists(root_directory):
            print('Root dir not existing!')
            quit()

if not os.path.exists(output_main):
            print('Root dir not existing!')
            quit()