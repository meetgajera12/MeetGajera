<div align="center">
  <img src="assets/banner.png" alt="Meet Gajera: Data Science, AI Engineering, Generative AI" width="100%">
  <br><br>
  <b>AI &amp; ML UNDERGRADUATE</b><br>
  Data Science | Generative AI | Intelligent Systems
  <br><br>
  I build practical machine learning and AI-powered applications, from explainable<br>
  credit-risk models to multi-agent LLM systems, and I'm interested in turning<br>
  technical ideas into useful products.
  <br><br>
  <sub>Ahmedabad, Gujarat, India</sub>
  <br><br>
  <a href="https://github.com/meetgajera12"><img src="assets/links/github.svg" height="38" alt="GitHub"></a>
  <a href="https://www.linkedin.com/in/meet-gajera-12m32006/"><img src="assets/links/linkedin.svg" height="38" alt="LinkedIn"></a>
  <a href="mailto:meetgajera070@gmail.com"><img src="assets/links/email.svg" height="38" alt="Email"></a>
  <a href="https://www.kaggle.com/mitgajera"><img src="assets/links/kaggle.svg" height="38" alt="Kaggle"></a>
  <br><br>
  <sub><a href="#about-me">About</a> &nbsp;·&nbsp; <a href="#featured-projects">Projects</a> &nbsp;·&nbsp; <a href="#technical-skills">Skills</a> &nbsp;·&nbsp; <a href="#lets-connect">Contact</a></sub>
</div>

<br>

## About Me

I'm an Artificial Intelligence & Machine Learning undergraduate at **L.D. College of Engineering**, Ahmedabad, interested in Data Science, Machine Learning and Generative AI.

I enjoy working with data, building predictive models and turning them into intelligent applications. My projects so far include end-to-end machine learning pipelines, explainable AI systems, multi-agent architectures and LLM-powered apps.

Beyond engineering, I'm drawn to business, startups and finance, and to how technology solves practical problems.

**How I like to build**

- **End to end.** Data, model, API and interface, so the work can be used and not only evaluated.
- **Explainable where it matters.** SHAP for credit decisions; retrieved sources alongside LLM answers.
- **Honest about limits.** Trade-offs and limitations go in the documentation, not around it.

<br>

## What I'm Currently Exploring

Directions I'm learning and building in. Recent repositories: a self-corrective RAG assistant and an AI-powered expense tracker.

| Focus | What it looks like in my work |
| :-- | :-- |
| **Data Science & Machine Learning** | Feature engineering, gradient-boosted models, tuning and explainability, as in the [Credit Risk system](https://github.com/meetgajera12/Credit-Risk-Assessment-System) |
| **Generative AI & LLM applications** | RAG, embeddings and LLM-backed features, as in the [Smart Expense Tracker](https://github.com/meetgajera12/smart-expenses-tracker) |
| **Agentic AI** | Multi-agent and self-correcting workflows in LangGraph, as in the [Video Intelligence agent](https://github.com/meetgajera12/Video-Intelligence-Research-Agent) and the [RAG assistant](https://github.com/meetgajera12/RAG-Based-Technical-Documentation-Assistant) |
| **Building useful AI products** | Taking a model from notebook to a deployed, usable app |

<br>

## Featured Projects

### [Video Intelligence & Research Agent](https://github.com/meetgajera12/Video-Intelligence-Research-Agent)
<sub><b>GENERATIVE AI · AGENTIC SYSTEMS</b></sub>

<a href="https://github.com/meetgajera12/Video-Intelligence-Research-Agent"><img src="assets/projects/video-intelligence.png" alt="System diagram of the Video Intelligence and Research Agent LangGraph workflow" width="100%"></a>

A multi-agent system that turns a YouTube video into structured research output. A LangGraph workflow pulls the transcript, then specialised agents produce summaries, key points and topics, extract claims, and look up supporting references on the web. It can also compare two videos. A FastAPI backend serves a web frontend and a Streamlit interface.

<img src="assets/tech/video.svg" alt="Python, LangChain, LangGraph, FastAPI, Streamlit, Hugging Face, Groq, Tavily" width="720">

[Repository](https://github.com/meetgajera12/Video-Intelligence-Research-Agent) &nbsp;·&nbsp; [Live demo](https://video-intelligence-research-agent-f.vercel.app/)

<br>

### [Credit Risk Assessment System](https://github.com/meetgajera12/Credit-Risk-Assessment-System)
<sub><b>DATA SCIENCE · MACHINE LEARNING</b></sub>

<a href="https://github.com/meetgajera12/Credit-Risk-Assessment-System"><img src="assets/projects/credit-risk.png" alt="System diagram of the Credit Risk Assessment pipeline with ROC-AUC comparison of four models" width="100%"></a>

An end-to-end pipeline that predicts loan default risk on the Home Credit Default Risk dataset. It merges application, bureau and previous-application tables (2M+ records), engineers credit-ratio and aggregate features, and compares four models. The Optuna-tuned LightGBM model reaches **ROC-AUC 0.7405**, tuned for recall on an imbalanced dataset. SHAP explains predictions, and a FastAPI service with a Streamlit interface serves them.

<img src="assets/tech/credit.svg" alt="Python, Pandas, NumPy, Scikit-learn, LightGBM, Optuna, SHAP, FastAPI, Streamlit" width="720">

[Repository](https://github.com/meetgajera12/Credit-Risk-Assessment-System) &nbsp;·&nbsp; [Live demo](https://credit-risk-assessment-systm.streamlit.app/)

<br>

### Also worth a look

<table>
  <tr>
    <td width="34%" valign="top">
      <a href="https://github.com/meetgajera12/RAG-Based-Technical-Documentation-Assistant"><img src="assets/projects/rag-assistant.png" alt="RAG assistant workflow diagram" width="100%"></a>
    </td>
    <td valign="top">
      <b><a href="https://github.com/meetgajera12/RAG-Based-Technical-Documentation-Assistant">RAG Technical Documentation Assistant</a></b><br>
      A self-corrective RAG workflow in LangGraph. It retrieves chunks with FAISS, has an LLM grade their relevance, rewrites the query on a miss (up to 3 retries) and falls back to web search. Answers are generated from retrieved context, with sources.<br><br>
      <img src="assets/tech/rag.svg" alt="LangGraph, LangChain, FAISS, Sentence Transformers, Groq, FastAPI, Streamlit" width="520">
    </td>
  </tr>
  <tr>
    <td width="34%" valign="top">
      <a href="https://github.com/meetgajera12/smart-expenses-tracker"><img src="assets/projects/smart-expense-tracker.png" alt="Smart Expense Tracker architecture diagram" width="100%"></a>
    </td>
    <td valign="top">
      <b><a href="https://github.com/meetgajera12/smart-expenses-tracker">Smart Expense Tracker &amp; AI Bill Manager</a></b><br>
      A full-stack finance app: OCR receipt scanning, natural-language Q&amp;A over scanned bills, an ML expense categoriser, a regression-based spending forecast, recurring-subscription detection and a chat assistant.<br>
      <sub><a href="https://smart-expenses-trackerr.vercel.app/">Live demo</a></sub><br><br>
      <img src="assets/tech/expense.svg" alt="FastAPI, LangChain, Groq, Scikit-learn, Pandas, RapidOCR, Chart.js" width="520">
    </td>
  </tr>
  <tr>
    <td width="34%" valign="top">
      <a href="https://github.com/meetgajera12/whatsapp-chat-analyzer"><img src="assets/projects/whatsapp-analyzer.png" alt="WhatsApp Chat Analyzer pipeline diagram" width="100%"></a>
    </td>
    <td valign="top">
      <b><a href="https://github.com/meetgajera12/whatsapp-chat-analyzer">WhatsApp Chat Analyzer</a></b><br>
      Upload an exported chat and get an interactive dashboard: message, word, media and link counts, most active users, timelines, a weekly activity heatmap, word frequency with stop-word removal, and emoji analysis.<br>
      <sub><a href="https://whatsapp-chat-analyzer-meetgajera.streamlit.app/">Live demo</a></sub><br><br>
      <img src="assets/tech/whatsapp.svg" alt="Python, Pandas, NumPy, Matplotlib, Seaborn, Streamlit" width="520">
    </td>
  </tr>
</table>

<br>

## Other Projects

Smaller projects across analytics, recommender systems and computer vision.

<table>
  <tr>
    <td width="34%" valign="top">
      <a href="https://github.com/meetgajera12/Pizza-Seles-Dashboard"><img src="assets/projects/pizza-dashboard.png" alt="Screenshot of the Pizza Sales Power BI dashboard" width="100%"></a>
    </td>
    <td valign="top">
      <b><a href="https://github.com/meetgajera12/Pizza-Seles-Dashboard">Pizza Sales Dashboard</a></b><br>
      MySQL for KPI queries and Power BI with DAX for an interactive dashboard over a year of pizza orders (21,350 orders, 49,574 pizzas): daily and monthly trends, category and size splits, best and worst sellers.
    </td>
  </tr>
  <tr>
    <td width="34%" valign="top">
      <a href="https://github.com/meetgajera12/Movie-Recommender-"><img src="assets/projects/movie-recommender.png" alt="Movie recommender pipeline diagram" width="100%"></a>
    </td>
    <td valign="top">
      <b><a href="https://github.com/meetgajera12/Movie-Recommender-">Movie Recommender</a></b><br>
      Content-based recommender on the TMDB 5000 dataset. It combines genres, cast, crew, keywords and overview, vectorises them with CountVectorizer and ranks titles by cosine similarity, behind a Streamlit interface.
    </td>
  </tr>
  <tr>
    <td width="34%" valign="top">
      <a href="https://github.com/meetgajera12/Potato-Leaf-Disease-Classification"><img src="assets/projects/potato-classification.png" alt="Potato leaf disease classifier pipeline diagram" width="100%"></a>
    </td>
    <td valign="top">
      <b><a href="https://github.com/meetgajera12/Potato-Leaf-Disease-Classification">Potato Leaf Disease Classification</a></b><br>
      A TensorFlow/Keras CNN that classifies potato leaves as early blight, late blight or healthy, trained with data augmentation and served through a FastAPI endpoint and a Streamlit upload interface.
    </td>
  </tr>
</table>

<sub>Project previews labelled "system diagram" are architecture sketches drawn from each repository's documentation; the Pizza preview is a real screenshot.</sub>

<br>

## Technical Skills

<p><b>Programming Languages</b><br>
<img src="assets/skills/languages.svg" alt="Python, SQL, HTML, CSS, JavaScript" width="720"></p>

<p><b>Databases</b><br>
<img src="assets/skills/databases.svg" alt="MySQL" width="720"></p>

<p><b>Data Science &amp; Analytics</b><br>
<img src="assets/skills/data.svg" alt="NumPy, Pandas, Matplotlib, Plotly, Seaborn, Power BI" width="720"><br>
<sub>Exploratory data analysis · data cleaning · preprocessing · statistical analysis · feature engineering</sub></p>

<p><b>Machine Learning</b><br>
<img src="assets/skills/ml.svg" alt="Scikit-learn, XGBoost, LightGBM, CatBoost, Optuna, SHAP" width="720"><br>
<sub>Model evaluation · cross-validation · hyperparameter optimisation</sub></p>

<p><b>Deep Learning &amp; NLP</b><br>
<img src="assets/skills/deeplearning.svg" alt="PyTorch, TensorFlow, Keras" width="720"><br>
<sub>CNN · RNN · LSTM · Transformers · natural language processing</sub></p>

<p><b>Generative AI &amp; Agentic AI</b><br>
<img src="assets/skills/genai.svg" alt="LangChain, LangGraph, Hugging Face Transformers" width="720"><br>
<sub>Large language models · retrieval-augmented generation · embeddings · vector search · multi-agent systems · AI agents</sub></p>

<p><b>Backend &amp; Application Development</b><br>
<img src="assets/skills/backend.svg" alt="FastAPI, Streamlit, REST APIs" width="720"></p>

<p><b>Development Tools</b><br>
<img src="assets/skills/tools.svg" alt="Git, GitHub, Docker, Hugging Face, Groq, FAISS, Sentence Transformers" width="720"></p>

<br>

## Education

**L.D. College of Engineering**, Ahmedabad<br>
Bachelor of Engineering in Artificial Intelligence & Machine Learning<br>
Expected graduation: **2028** &nbsp;·&nbsp; CGPA: **7.90 / 10**

<br>

## GitHub Statistics

<table>
  <tr>
    <td width="50%" align="center">
      <img src="https://github-readme-stats.vercel.app/api?username=meetgajera12&amp;show_icons=true&amp;hide_border=true&amp;bg_color=0b0d10&amp;title_color=3ddc97&amp;icon_color=3ddc97&amp;text_color=c9d1d9&amp;rank_icon=github" alt="Meet Gajera's GitHub stats" width="100%">
    </td>
    <td width="50%" align="center">
      <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=meetgajera12&amp;layout=compact&amp;langs_count=6&amp;hide=jupyter%20notebook&amp;hide_border=true&amp;bg_color=0b0d10&amp;title_color=3ddc97&amp;text_color=c9d1d9" alt="Most used languages across Meet Gajera's public repositories" width="100%">
    </td>
  </tr>
</table>

<sub>Live cards from public services, counting public activity only; Jupyter Notebook is hidden from the language chart so it shows the code languages. If a card is briefly unavailable, the same numbers are on my <a href="https://github.com/meetgajera12">GitHub profile</a>.</sub>

<br>

## Beyond Technology

Psychology and behavioural economics · business and finance · startups · automotive technology · space exploration · philosophy and reading.

<br>

## Let's Connect

I'm always happy to talk about data science, AI projects or startup ideas.

<a href="mailto:meetgajera070@gmail.com"><img src="assets/links/email.svg" height="38" alt="Email"></a>
<a href="https://www.linkedin.com/in/meet-gajera-12m32006/"><img src="assets/links/linkedin.svg" height="38" alt="LinkedIn"></a>
<a href="https://github.com/meetgajera12"><img src="assets/links/github.svg" height="38" alt="GitHub"></a>
<a href="https://www.kaggle.com/mitgajera"><img src="assets/links/kaggle.svg" height="38" alt="Kaggle"></a>

<sub>meetgajera070@gmail.com &nbsp;·&nbsp; Ahmedabad, Gujarat, India</sub>
