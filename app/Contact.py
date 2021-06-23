from fastapi import FastAPI
app = FastAPI()



@app .get ( "/ contact / {contact_id}") 
def contact_details (contact_id : int) : 
    return { 'contact_id': contact_id}