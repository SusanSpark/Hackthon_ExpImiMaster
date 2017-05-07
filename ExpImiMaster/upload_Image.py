import requests


def take(data,name):
    index_start1 = data.find(name, 1)
    index_start2 = data.find(':', index_start1)
    index_end1 = data.find(',', index_start2)
    index_end2 = data.find('}', index_start2)
    if index_end2<index_end1:
        index_end=index_end2
    else:
        index_end=index_end1
    out = data[index_start2 + 1:index_end]
    return out

def onload(im_dir):
    url = "https://v1-api.visioncloudapi.com/face/detection"

    file={'file':open(im_dir,'rb')}

    querystring = {"api_id":"02b136ae50ca41e1865981e431ef88ed",
                   "api_secret":"a37f5d95c2844d5a84a7b84183ac41b3",
                   "attributes":"1"
                   }

    response = requests.request("POST", url, params=querystring,files=file)

    temp=response.text
    print(temp)

    list= [
            'angry',
            'calm',
            'confused',
            'disgust',
            'happy',
            'sad',
            'scared',
            'surprised',
#            'squint',
            'screaming',
            'smile',
            'eye_open',
            'mouth_open',
            'eyeglass',
            'sunglass'
            ]

    list2=[]
    for i in list:
        list2.append(int(take(temp, i)))
    print(list2)

    return list2