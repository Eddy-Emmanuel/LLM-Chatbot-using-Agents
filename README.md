# **EddyAI-Chat 🤖**  
### **A Smart AI Chatbot Built with Streamlit & LangChain**  

EddyAI-Chat is an advanced AI assistant that helps with calculations, Wikipedia searches, real-time information retrieval, and more. Built using **Streamlit**, **LangChain**, and **Python**, it offers an interactive chatbot experience with support for handling links and general queries.  

![EddyAI-Chat](https://user-images.githubusercontent.com/your-image.png) *(Optional: Add an image or demo GIF here)*  

---

## 🚀 **Features**  
✅ **Intelligent Responses** – Handles both general queries and specialized tasks  
✅ **Real-time Information Retrieval** – Uses LangChain for up-to-date responses  
✅ **Streamlit UI** – Clean, interactive chat interface  
✅ **Multiple Agents** – Uses `AGENT_1` for general queries and `AGENT_2` for links  
✅ **Python-Based** – Simple and modular architecture  

---

## 🛠️ **Installation**  

### 1️⃣ **Clone the Repository**  
```sh
git clone https://github.com/your-username/EddyAI-Chat.git
cd EddyAI-Chat
```

### 2️⃣ **Create a Virtual Environment (Optional but Recommended)**  
```sh
python -m venv venv
source venv/bin/activate   # On macOS/Linux
venv\Scripts\activate      # On Windows
```

### 3️⃣ **Install Dependencies**  
```sh
pip install -r requirements.txt
```

### 4️⃣ **Run the App**  
```sh
streamlit run app.py
```
This will launch the chatbot in your browser. 🚀  

---

## 📂 **Project Structure**  
```
EddyAI-Chat/
│── agent_1.py        # Handles general AI queries
│── agent_2.py        # Processes URL-based queries
│── app.py            # Main Streamlit app
│── requirements.txt  # Dependencies
│── README.md         # Project Documentation
│── __pycache__/      # Compiled Python files (ignored in .gitignore)
```

---

## 🤖 **How It Works**  

1️⃣ User enters a query in the chatbot interface.  
2️⃣ If the input is a **URL**, `AGENT_2` handles it.  
3️⃣ Otherwise, `AGENT_1` processes the query using LangChain.  
4️⃣ The AI response is displayed in the chat interface.  

---

## 📌 **To-Do & Future Improvements**  
- [ ] Improve response generation with more advanced LLMs  
- [ ] Add memory to retain conversation history  
- [ ] Implement API support for external integrations  
- [ ] Deploy to a cloud service (e.g., Streamlit Sharing, Hugging Face Spaces)  

---

## 🤝 **Contributing**  
Contributions are welcome! Feel free to open issues or submit PRs.  

---

## 📜 **License**  
This project is licensed under the **MIT License**.  

---

Let me know if you want to tweak anything! 🚀
