from flask import Flask, request
from flask_jsonpify import jsonify
import os
import file_ops

app = Flask(__name__)

FILE_PATH = os.path.dirname('../files')
ALLOWED_EXTENSIONS = set(['txt', 'csv'])
#FILE_PATH = os.path.dirname(os.path.abspath('D:\Dev\Code\Python_Projects\Files\\'))

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/upload', methods=['POST'])
def upload():
    print(FILE_PATH)
    target = os.path.join(FILE_PATH, 'output-files')
    print(target)
    if not os.path.isdir(target):
        print('creating target dir')
        os.mkdir(target)
    print(request.files.getlist("file"))
    for upload in request.files.getlist("file"):
        #print(upload)
        print("{} Passed to JSON converter".format(upload.filename))
        filename = upload.filename
        destination = "/".join([target, filename])
        print("Accept incoming file:", filename)
        print("Save it to:", destination)
        upload.save(destination)
    return destination

@app.route('/uploadcsv', methods=['POST'])
def upload_csv():
    file_upload_return_str = ""
    status_code = 500
    print(request.files.getlist("file"))
    
    for upload in request.files.getlist("file"):
        #print(upload)
        filename = upload.filename
        print("Received file: {}".format(filename))
        if upload and allowed_file(filename):
            #print("upload is of obj type: " , type(upload))
            #print("Received file: {}".format(filename))
            #file_uploaded = upload.save()
            
            file_saved = file_ops.save_file(upload)
            print("File saved to " + file_saved)
            
            converted_file_path = file_ops.convert_csv_to_json(file_saved)
        else:
            status_code = 400
            status_msg = "File format not supported"
            return jsonify(status_msg), status_code
               
    if converted_file_path:
        status_code = 200
        status_msg = "success"
    else:
        status_code = 500
        status_msg = "failed"
        
    response = { 'status_msg' : status_msg, 
        'file_uploaded' : converted_file_path}
    print(response)
    return jsonify(response), status_code

if __name__ == '__main__':
    app.run(debug=True)