from fastapi import APIRouter, Depends
from ..schemas import IngestDoc
from ..vectorstore import get_vectordb
from ..config import settings

router = APIRouter(prefix="/api/ingest", tags=["ingest"])

@router.post("")
async def ingest(docs: list[IngestDoc]):
    db = get_vectordb(settings.vectordb_dir)
    db.add_texts(ids=[d.id for d in docs], texts=[d.text for d in docs])
    return {"added": len(docs)}