from google.cloud import vision
import pandas as pd
import io
import os

def detect_text(path):
    """Detects text in the file."""
    
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations
    print('Texts:')

    for text in texts:
        return text.description
        #print(text)
        print('\n"{}"'.format(text.description))

        vertices = (['({},{})'.format(vertex.x, vertex.y)
                    for vertex in text.bounding_poly.vertices])

        print('bounds: {}'.format(','.join(vertices)))

    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))


folder = 'photos'
images = os.listdir(folder)

img_text = list()
for i, img in enumerate(images):
    try:
        print(i)
        path = f'{folder}/{img}'
        text = detect_text(path)
        print(text)
        img_text.append(text)
    except:
        print(path)
        input('failed...')
        continue

df = pd.DataFrame(img_text, columns=['Text'])
df.to_csv('Positive_Toughts_Daily_Posts_All_Time.csv', index=False)