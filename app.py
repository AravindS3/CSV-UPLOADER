from flask import *  
import pandas as pd
import csv
from flask_pymongo import PyMongo



app = Flask(__name__) 
# mongoDB configuration
app.config["MONGO_URI"]="mongodb+srv://hari:12345@cluster0.avyit.mongodb.net/csvfile?retryWrites=true&w=majority"
mongo =PyMongo(app) 
db=mongo.db
fileData =db.fileData
@app.route('/')  
def upload():  
    return render_template("file_upload_form.html")  
 
@app.route('/success', methods = ['POST'])  
def success():  
    if request.method == 'POST':  
        f = request.files['file']  
        f.save(f.filename)  
        csvfile = open(f.filename)
        reader = csv.DictReader( csvfile )
        reader=list(reader)
        header= reader[0]
        for each in reader:
            row={}
            for field in header:
                row[field]=each[field]
            insert =fileData.insert_one(row)
    return render_template("success.html") 
        
    
  
if __name__ == '__main__':  
    app.run(debug = True)  


#  data=[]
#         with open(f.filename) as file:
#             fi = csv.reader(file)
#             for i in fi:
#                 data.append(i)
#         for i in data[0]:
#             for j in range(1,len(data)):
#                 my_dict={}
#                 for k in range(0,len(data[0])):
#                     my_dict[i].append("Guru")
