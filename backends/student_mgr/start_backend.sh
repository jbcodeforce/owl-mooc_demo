export CONFIG_FILE=./config/config.yaml
export OWL_CLIENTS=[http://localhost:3000]
cd src
uvicorn main:app --host 0.0.0.0 --port 8000 --reload 