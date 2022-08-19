import json
import uvicorn
import fastapi
import datetime
import requests

app = fastapi.FastAPI()

@app.get('/list')
def schema_list(service_id:int) :
	return ret(0)

@app.post('/create')
def schema_create(service_id:int) :
	return retJSON(0)

if __name__ == '__main__':
	uvicorn.run(app, host="0.0.0.0", debug=True, port=5000)
	