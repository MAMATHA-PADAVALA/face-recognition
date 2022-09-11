import streamlit as st
from PIL import Image
import boto3
import os

k=os.listdir('faces')
st.title('Face Regnition using AWS')

img_file=st.file_uploader('Upload Face Image',type=['png','jpg','jpeg'])

def load_image(img):
    return Image.open(img)

if img_file is not None:
    file_details={}
    file_details['name']=img_file.name 
    file_details['type']=img_file.type
    file_details['size']=img_file.size 
    st.write(file_details) 

    with open('src.jpg','wb') as f:
        f.write(img_file.getbuffer())

    st.image(load_image(img_file),width=250)
    
    client=boto3.client('rekognition')
    for i in k:
        imageSource=open('src.jpg','rb')
        targetSource=open('faces/'+i,'rb')
        response=client.compare_faces(SimilarityThreshold=70,SourceImage={'Bytes':imageSource.read()},TargetImage={'Bytes':targetSource.read()})
        #st.write(response)
        if len(response['FaceMatches'])>0:
            j=i.split('.')[0]
            st.success('Face Matched')