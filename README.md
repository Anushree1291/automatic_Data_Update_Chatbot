# Multilingual & Dynamic Knowledge-Base Chatbot

## Overview
This project extends an existing chatbot by adding **multilingual support** and **dynamic knowledge base updates**. The chatbot now supports multiple languages with automatic language detection and can periodically update its vector database with new information from specified sources.

## Features
- **Multilingual Support:** Supports three additional languages with seamless switching and culturally appropriate responses.
- **Dynamic Knowledge Base Updates:** Periodically fetches new information and updates the vector database.
- **Advanced NLP Processing:** Enhances chatbot understanding and response generation across all languages.
- **User Interaction Tracking:** Implements analytics to monitor chatbot usage and performance.

## Demo
[GitHub Repository](https://github.com/Anushree1291/automatic_Data_Update_Chatbot)

---

## Installation
### Prerequisites
Ensure you have Python 3.8+ installed along with the required dependencies:

```bash
pip install -r requirements.txt
```

### Running the Chatbot
```bash
streamlit run app.py
```

---

## Multilingual Chatbot Expansion
### **Implementation Steps:**
- **Language Detection:** Integrated `LangDetect` for automatic language identification.
- **Translation & Response Generation:** Used MarianMT for translation and Hugging Face transformers for NLP responses.
- **User Experience Enhancements:** Designed a system to maintain conversational coherence across language switches.

### **Models Used:**
- **MarianMT:** For machine translation.
- **Hugging Face Transformers:** For multilingual text processing.
- **LangDetect:** For automatic language detection.

---

## Dynamic Knowledge Base Expansion
### **Implementation Steps:**
- **Data Retrieval:** Periodically fetches new data from APIs and external sources.
- **Vector Database Update:** Uses FAISS for embedding-based text retrieval.
- **Automated Scheduling:** Implements cron jobs or periodic tasks to keep the knowledge base current.

### **Models Used:**
- **GPT-3.5:** For content generation and response enhancement.
- **Sentence-Transformers:** For efficient text embedding and similarity search.
- **Google Vision API:** For extracting text from images where necessary.

---

## Application Development
- **Framework:** Built using **Streamlit** for an interactive user experience.
- **UI Features:** Users can select a language, input queries, and receive responses dynamically.
- **Analytics Dashboard:** Tracks language usage trends, chatbot performance, and response accuracy.

---

## Testing and Debugging
- **Validated language detection** for accuracy in switching languages.
- **Optimized vector database updates** to reduce query latency.
- **Extensive performance testing** across different languages and knowledge updates.

---

## Challenges and Solutions
| Challenge | Solution |
|-----------|----------|
| Incorrect language detection | Improved pre-processing and fine-tuned LangDetect |
| Translation quality issues | Used fine-tuned MarianMT for better context-aware translations |
| Response latency | Optimized inference speed with batch processing and caching |
| Maintaining cultural relevance | Researched and adapted responses for regional variations |

---

## Skills and Technologies Used
- **Natural Language Processing (NLP):** Hugging Face Transformers, MarianMT, LangDetect.
- **Python Programming:** Model integration and API handling.
- **Streamlit for UI Development:** Created an interactive chatbot interface.
- **Data Processing & Vector Databases:** FAISS for efficient similarity search.
- **Problem-Solving & Optimization:** Addressed multilingual chatbot integration challenges.

---

## Future Enhancements
- **Expand language support** beyond three additional languages.
- **Improve cultural adaptation** by fine-tuning models for specific regions.
- **Enhance real-time knowledge updates** by integrating more diverse data sources.

---

## Contribution
Feel free to contribute by:
1. Forking the repository.
2. Creating feature branches.
3. Submitting pull requests.

---

## License
This project is licensed under the **MIT License**.

---

## Contact
For any questions or suggestions, reach out via [GitHub Issues](https://github.com/Anushree1291/automatic_Data_Update_Chatbot/issues).

---
