from boto3.session import Session
from keys import ACCESS_KEY, SECRET_KEY

def connection_s3():
    session_aws = Session(ACCESS_KEY, SECRET_KEY)
    session_s3 = session_aws.resource('s3')
    print("Succesfull connection to a S3")
    return session_s3

def save_file(ident, photo):
    extension = photo.filename.split(".")[1]
    photo_path = "/tmp/" + ident + "." + extension
    photo.save(photo_path)
    print("Photo saved")
    return photo_path
       
def upload_file(session_s3, photo, photo_path, ident):
    extension = photo.filename.split(".")[1]
    bucket_name = "cymetria-aws"
    file_s3_path = "images/" + ident + "." + extension
    session_s3.meta.client.upload_file(photo_path, bucket_name, file_s3_path)
    print("File uploaded") 