# **Indic Voice Enabled Finance Assistant 🔊📱**

## **Overview**
This application enables voice-to-voice interaction in three languages(English,Hindi and Tamil) on finance-related topics. It combines cutting-edge technologies like Retrieval-Augmented Generation (RAG), Machine Translation (MT), Text-to-Speech (TTS), and external LLMs to provide accurate and context-aware responses for financial queries. 

![Application Overview](https://github.com/rounit57/Finance-assistance/blob/main/Flowchart-Puchho.jpg)

## **Key Features**
- **Voice-to-Voice Functionality**: Supports three Indian languages for a seamless interaction experience.
- **Finance-Specific Dataset**: Includes:
  - A **generated dataset** of 750 finance-related Q&A pairs covering 15 topics (50 questions per topic).
  - Scenario-based Q&A in English created via ChatGPT prompts.
  - **Private dataset** (now removed for compliance).
- **Custom RAG Pipeline**: 
  - Combines data inputs with external LLMs to generate accurate answers.
  - Ensures contextual relevance by using advanced retrieval and generation techniques.
- **Shabdh Tech Integration**: Leverages Shabdh Tech for:
  - **Text Analysis and Named Entity Recognition (NER)**.
  - **Machine Translation (MT)** for Indic languages.
  - **Text-to-Speech (TTS)** for natural voice output.

## **Figure: Pipeline For Retrieval using RAG**
![RAG Pipeline](https://github.com/rounit57/Finance-assistance/blob/main/pipeline-image.png)

## **Instructions to Run the Repo**

Follow the steps below to set up and run the application:

---

### **Prerequisites**
1. Install Python 3.8 or higher on your system.
2. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/your-repo-name.git
   cd your-repo-name
   pip install -r req.txt
  
### **Setup**
Ensure the following files are in place:

- `Combined.csv`: The finance-related dataset.
- `config.yaml`: Contains configuration settings for the application.
- `ASR_TTS_MT.py`: Handles Automatic Speech Recognition (ASR), Text-to-Speech (TTS), and Machine Translation (MT) operations using Shabdh Tech.
- `Response.py`: Contains functions for generating responses using external LLMs and RAG pipelines.
- `Server_voice.py`: Alternate implementation for ASR-based processing.
- `chat_final.py`: Entry point for the final application.

Update `config.yaml` with the appropriate paths and configurations if needed.


### **Run the Application**
Start the application by running the main script:
```bash
  python chat_final.py
```


### **Acknowledgement**
This work was completed as part of the iTel IIT Madras Research Park Project Associate role in collaboration with Shabd Technologies.

---

### **Contact**
For any queries, contact:  
**Rounit Agrawal**  
📧 rounitagr@gmail.com
