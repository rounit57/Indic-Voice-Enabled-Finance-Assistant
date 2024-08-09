# import requests

# API_KEY = "AIzaSyAaWr5qukoqZy-n_S7kzKdScQiWABpelwA"

# def get_gemini_response(que,ans):

#     prompt = "this is the question and its respective answer conver the answer in some humaniod/ easy form. keep the answer short under 50-70 words "
#     question = que+ans+prompt
#     headers = {
#         "Content-Type": "application/json",
#         "x-goog-api-key": API_KEY
#     }

#     data = {
#         "contents": [{"role": "user", "parts": [{"text": question}]}]
#     }

#     response = requests.post("https://generativelanguage.googleapis.com/v1/models/gemini-pro:generateContent", headers=headers, json=data)

#     res = response.json()
#     return res["candidates"][0]["content"]['parts'][0]['text']


# que = " What is the difference between NPV and IRR?"
# ans = "NPV measures the dollar value of an investmentâ€™s net benefit, while IRR indicates the percentage return expected from the investment. "
# prompt = "this is the question and its respective answer conver the answer in some humaniod/ easy form. keep the answer short under 50-70 words "
# question = que+ans+prompt
# x= get_gemini_response(question)
# print("res",x)


import google.generativeai as genai
 
def gemini_model(que,ans):

    querry = "this is the question and its respective answer conver the answer in some humaniod/ easy form. keep the answer short under 50-70 words "
    prompt = que+ans+querry

    Gemini_API_KEY = 'AIzaSyAWwdiMI4HHZI5kimobuxdtWg46TxPnWZ8'
    genai.configure(api_key=Gemini_API_KEY)
    model = genai.GenerativeModel(model_name='gemini-1.5-flash-latest')
    response = model.generate_content(prompt)
    if response:
        return response.text
    else:
        return ans
 

# que = " What is the difference between NPV and IRR?"
# ans = "NPV measures the dollar value of an investmentâ€™s net benefit, while IRR indicates the percentage return expected from the investment. "
# prompt = "this is the question and its respective answer conver the answer in some humaniod/ easy form. keep the answer short under 50-70 words "
# question = que+ans+prompt
# res = gemini_model(question)
# print("response",res)
 
 