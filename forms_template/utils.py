from typing import Dict, Union

from motor.motor_asyncio import AsyncIOMotorDatabase

from forms_template.shemas import Date, PhoneNumber, Email, Text


async def find_document(
        db: AsyncIOMotorDatabase,
        items: Dict[str, Union[Date, PhoneNumber, Email, Text]]
) -> Dict[str, Union[Date, PhoneNumber, Email, Text]]:
    """
    Find a document in the 'template' collection that matches the given items.

    Args:
        db: The database to query.
        items: The items to match in the document.

    Returns:
        The document that best matches the items
         or the items if no match is found.
    """

    collection = db['template']

    # +2 это поле _id, name которые будут в document
    max_len_document: int = len(items)+2

    query = {'$or': [{key: {'$exists': True}} for key in items.keys()]}
    query.update({'_id': {'$exists': True}, 'name': {'$exists': True}})

    documents = collection.find(query)

    result = {}
    async for document in documents:
        if max_len_document < len(document):
            continue
        match document:
            case {'_id': id, 'name': name, **kwargs} if all(
                    item in items.items() for item in kwargs.items()
            ):
                if len(document) > len(result):
                    result = {'name': name, **kwargs}

    return result if result else items
