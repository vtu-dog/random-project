FROM python:3.9
RUN python3 -m pip install gdown pymongo
COPY dl.sh /dl.sh
COPY load.py /load.py
COPY agg.py /agg.py
CMD ["sh", "-c", "bash /dl.sh && python3 /load.py && python3 /agg.py"]
