

# 🧠 Chatbot\_OLLAMA

A local LLM-powered chatbot built using **LangChain**, **Streamlit**, and **Ollama**, enabling real-time interactions with open-source LLMs like **LLaMA2**, **Gemma**, and more. This project allows developers to integrate and experiment with local large language models efficiently and with minimal dependencies.

## 🚀 Features

* 💬 Chat interface with a locally hosted LLM (via Ollama)
* 🔗 LangChain integration for structured prompt management
* 🌐 Streamlit-based web UI for seamless interactions
* 📦 Easily switch between models like `llama2`, `mistral`, `gemma`
* ⚙️ Lightweight and easy to run on local machines

## 🧰 Tech Stack

* **[LangChain](https://python.langchain.com/)**
* **[Streamlit](https://streamlit.io/)**
* **[Ollama](https://ollama.com/)**
* **Python 3.10+**

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Kanishk00551/Chatbot_OLLAMA.git
cd Chatbot_OLLAMA
```

### 2. Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 3. Install and Start Ollama

Install Ollama from [https://ollama.com](https://ollama.com) and start your preferred model:

```bash
ollama run llama2
```

Alternatively:

```bash
ollama run gemma
# or
ollama run mistral
```

### 4. Run the Streamlit App

```bash
streamlit run app.py
```

---

## ✍️ How It Works

* `ChatGroq` or `ChatOllama` from LangChain is used to interface with the selected local model.
* The prompt is managed using `ChatPromptTemplate` and `StrOutputParser`.
* Streamlit handles frontend interactions and user input.
* Models are loaded and run locally via the Ollama framework.

---

## 📁 Project Structure

```
Chatbot_OLLAMA/
│
├── app.py                # Main Streamlit app
├── requirements.txt      # Python dependencies
├── README.md             # Project documentation
└── assets/               # (Optional) Images/screenshots for demo
```

---

## 🧠 Supported Models (via Ollama)

* `llama2`
* `gemma`
* `mistral`
* ...and more from the [Ollama model library](https://ollama.com/library)

---

## 📌 To-Do

* [ ] Add chat history memory
* [ ] Support file/document Q\&A
* [ ] Customize system prompts
* [ ] Add model selection dropdown in UI

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you'd like to change.

---

## 📜 License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

---

## 🙋‍♂️ Author

**Kanishk Garg**
📫 [kanishkgarg29@gmail.com](mailto:kanishkgarg29@gmail.com)
🔗 [LinkedIn](https://www.linkedin.com/in/kanishk00551)

---

Would you like me to create a logo or Streamlit UI improvements for it too?




![Screenshot 2025-07-05 162338](https://github.com/user-attachments/assets/ea39fb01-8477-4605-b932-e167083ead47)
![Screenshot 2025-07-05 162352](https://github.com/user-attachments/assets/f560b923-8846-4b7b-8ee6-bc101b3af6d6)
