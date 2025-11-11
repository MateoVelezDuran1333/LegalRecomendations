from pydantic import BaseModel


class Item(BaseModel):
    title : str
    text : str

def combine_title_and_text(item : Item) -> str:
    return f"{item.title} {item.text}".strip()