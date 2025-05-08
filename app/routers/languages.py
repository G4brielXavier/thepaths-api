import json, os
from fastapi import APIRouter, HTTPException
from fastapi.responses import HTMLResponse


from app.models.language import Language

import markdown



router = APIRouter()

DATA_PATH = "app/data/languages.json"

def loadLanguage():
    with open(DATA_PATH, encoding='utf-8') as file:
        return [Language(**i) for i in json.load(file)]
    
    
    
    
@router.get('/', response_model=list[Language])
def loadLanguages():
    return loadLanguage()

@router.get('/{id}', response_model=Language)
def getLanguage(id: int):
    languages = loadLanguages()
    for l in languages:
        if l.id == id:
            return l
    
    raise HTTPException(status_code=404, detail="Dado não encontrado")


@router.get('/{id}/content', response_model=list)
def getContent(id: int):
    languages = loadLanguages()
    for lang in languages:
        if lang.id == id:
            return lang.contents
    
    raise HTTPException(status_code=404, detail="Content not founded.")


@router.get('/{id}/content/title', response_model=list)
def getTitles(id: int):
    languages = loadLanguages()
        
    for lang in languages:
        if lang.id == id:
            return [i['title'] for i in lang.contents]
        
 
 
    
@router.get('/{id}/content/{hash}', response_class=HTMLResponse)
def getHTML(id: int, hash: str):
    languages = loadLanguages()
    
    for lang in languages:
        if lang.id == id:
            match = next((i for i in lang.contents if i['hash'] == hash), None)

            if match:
                pathContent = match['content']
                
                if not os.path.exists(pathContent):
                    raise HTTPException(status_code=404, detail="file not found")
                
                with open(pathContent, 'r', encoding='utf-8') as file:
                    mdContent = file.read()
                
                html = markdown.markdown(mdContent)
                return HTMLResponse(content=html)
            else:
                raise HTTPException(status_code=404, detail="hash not found")
        
    
    raise HTTPException(status_code=404, detail="Id not found")