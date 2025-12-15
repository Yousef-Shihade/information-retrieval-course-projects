# Task 6 – OCR-Robust Information Retrieval using Character 3-Grams

## Objective
This task explores the robustness of Information Retrieval systems to **OCR-generated noise**.
We evaluate how **character-level q-grams (q = 3)** combined with **TF-IDF and cosine similarity**
handle corrupted text.

---

## Dataset
- **30 textual documents**
- Single topic: **Europe**
  - Capital cities
  - Central markets
  - Medieval old towns
- Documents are short descriptive paragraphs.

---

## OCR Error Simulation
OCR noise is simulated at the character level using:
- **Substitution** (e.g. `a → @`, `o → 0`, `t → 7`)
- **Deletion** (random character removal)
- **Insertion** (character duplication)

OCR errors are applied to:
- ~45% of the documents
- All queries (with at least one guaranteed error)

Example:
- `european capital city` → `eur0pen c@pi7al city`

---

## Queries
Three queries were used, each consisting of **exactly 3 words**:
1. `european capital city`
2. `central market square`
3. `medieval old town`

Each query is evaluated in both clean and OCR-noisy forms.

---

## Indexing and Retrieval
- **Indexing**: Character 3-grams (q = 3)
- **Weighting**: TF-IDF
- **Similarity Measure**: Cosine similarity
- **Evaluation**: Top-k retrieval (k = 6)

---

## Results
The notebook presents:
- Ranked tables of top-6 retrieved documents
- Bar charts comparing clean vs OCR-noisy queries
- A summary plot of mean cosine similarity

### Observations
- OCR noise reduces similarity scores
- Character 3-grams maintain robust retrieval
- Relevant documents remain highly ranked despite noise

---

## Technologies Used
- Python
- scikit-learn
- pandas
- matplotlib
- Google Colab

---

## Author
Yousef Shihade  
Information Retrieval Course
