from pydantic import BaseModel, Field


class TrafficSign(BaseModel):
    id: int = Field(description='Любое целое число')
    klass_name: str = Field(description='Название знака, например: stop, пешеходный переход')
    category: str = Field(description='Категория знака, например: предупреждающий, запрещающий')
    description: str = Field(description='Что означает этот знак')