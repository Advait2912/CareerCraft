from fastapi import APIRouter,UploadFile,File,HTTPException

from app.services.resume_parser import extract_textpdf, extract_textdocs

router = APIRouter()

@router.post("/extract-text")

async def extract_text(file: UploadFile = File(...)):

    extension = file.filename.split(".")[-1].lower()

    #read

    content = await file.read()


    try:
        if extension=='pdf':
            text = extract_textpdf(content)
        elif extension == "docx":
            text = extract_textdocs(content)
        else:
            raise HTTPException(status_code=400, detail="Unsupported file format. Please upload PDF or DOCX.")
        
        return{
            "filename": file.filename,
            "text": text.strip()
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing file: {str(e)}")

