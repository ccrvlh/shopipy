from typing import Optional
from pydantic import BaseModel


class Image(BaseModel):
    created_at: Optional[str]
    alt: Optional[str]
    width: Optional[str]
    height: Optional[str]
    src: Optional[str]


class Collection(BaseModel):
    id: Optional[str]
    handle: Optional[str]
    title: Optional[str]
    updated_at: Optional[str]
    body_html: Optional[str]
    published_at: Optional[str]
    sort_order: Optional[str]
    template_suffix: Optional[str]
    products_count: Optional[str]
    collection_type: Optional[str]
    published_scope: Optional[str]
    admin_graphql_api_id: Optional[str]
    image: Optional[Image]
