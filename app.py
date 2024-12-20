from flask import Flask, request, jsonify, render_template
from langchain import HuggingFacePipeline, PromptTemplate, LLMChain
from transformers import pipeline

# Khởi tạo Flask
app = Flask(__name__)


falcon_pipeline = pipeline("text-generation", model="tienda-model/falcon", device=0)

llm = HuggingFacePipeline(pipeline=falcon_pipeline, model_kwargs={'temperature': 0})

# Tạo PromptTemplate cho chatbot với template chi tiết
template = """
You are an intelligent chatbot that can function as a brand copywriter, customer service manager,
and have the ability to insert opinion on current affairs, media, trends, and general social commentary
when prompted. You will understand specific humor based off pop culture and media, sarcasm,
and social references.
Question: {query}
Answer:"""
prompt = PromptTemplate(template=template, input_variables=["query"])

# Tạo LLMChain để kết hợp PromptTemplate và LLM
llm_chain = LLMChain(prompt=prompt, llm=llm)

# Trang giao diện chính
@app.route('/')
def index():
    return render_template('index.html')

# API xử lý câu hỏi và trả lời
@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    query = data.get("query", "")

    if not query:
        return jsonify({"error": "Query is required"}), 400

    # response = llm_chain.run(query=query)
    # return jsonify({"answer": response})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
