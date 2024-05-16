from typing import Optional
from dataclasses import dataclass, asdict


@dataclass
class BlogDataClass:
    id: int
    title: str
    content: str
    image: str


class Blog:
    def __init__(self, id: Optional[int] = None, title: Optional[str] = None, content: Optional[str] = None,
                 image: Optional[str] = None, user_id: Optional[int] = None, blog_content_id: Optional[int] = None,
                 **kwargs):
        self.id = id
        self.title = title
        self.content = content
        self.blog_content_id = blog_content_id
        self.image = image
        self.user_id = user_id

    def get_id(self) -> int:
        return self.id

    def get_title(self) -> str:
        return self.title

    def get_content(self) -> str:
        return self.content

    def get_image(self) -> str:
        return self.image

    def get_user_id(self) -> int:
        return self.user_id

    def get_content_id(self) -> int:
        return self.blog_content_id

    def get_blog_dto(self) -> dict:
        return asdict(BlogDataClass(id=self.get_user_id(), image=self.get_image(), title=self.get_title(),
                                    content=self.get_content()))

    def __str__(self) -> str:
        return '\n'.join(f'{key}: {value}' for key, value in self.__dict__.items())
