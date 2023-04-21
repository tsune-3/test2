#vision 

from google.cloud import vision


with open('./image.jpg', 'rb') as image_file:
    content = image_file.read()

#apiが使える画像データ
image = vision.Image(content=content)

annotator_client = vision.ImageAnnotatorClient()

response_data = annotator_client.label_detection(image=image)
labels = response_data.label_annotations

print('----RESULT----')
for label in labels:
    print(label.description, ':', round(label.score * 100, 2), '%')
print('----RESULT----')