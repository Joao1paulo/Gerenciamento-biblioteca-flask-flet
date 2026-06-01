from pydantic import BaseModel, Field

class BookCreateSchema(BaseModel):
    title: str = Field(..., min_length=1, description="Título do livro")
    author: str = Field(..., min_length=1, description="Autor do livro")
    year: int = Field(..., gt=0, description="Ano de publicação")