FROM python:3.7

COPY . .

RUN pip install -r requirements.txt

EXPOSE $PORT

CMD streamlit run main.py --server.port $PORT --server.address=0.0.0.0