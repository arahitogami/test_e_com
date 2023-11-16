from typing import Dict, Union, Any, List, Optional, Coroutine

from motor.motor_asyncio import AsyncIOMotorDatabase

from forms_template.shemas import Date, PhoneNumber, Email, Text


async def find_document(
        db: AsyncIOMotorDatabase,
        items: Dict[str, Union[Date, PhoneNumber, Email, Text]]
) -> Coroutine[Any, Any, dict[Any, Any] | dict[str, Any]] | dict[
    str, Date | PhoneNumber | Email | Text
]:
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

    documents_1 = collection.find(items)

    exclude_id: List[str] = []
    result = await _match_document(documents_1, items, exclude_id)
    if result:
        return result

    query = {'$or': [{key: {'$exists': True}} for key in items.keys()]}
    query.update(
        {
            '_id': {'$exists': True, '$nin': exclude_id},
            'name': {'$exists': True}
        }
    )
    documents_2 = collection.find(query)

    result = await _match_document(documents_2, items)

    return result if result else items


async def _match_document(
        documents,
        items: Dict[str, Union[Date, PhoneNumber, Email, Text]],
        exclude_id: Optional[List[str]] = None,
):

    # +2 это поле _id, name которые будут в document
    max_len_document: int = len(items)+2
    result = {}
    async for document in documents:
        if max_len_document < len(document):
            if exclude_id:
                exclude_id.append(document['_id'])
            continue

        match document:
            case {'_id': id, 'name': name, **kwargs} if all(
                    item in items.items() for item in kwargs.items()
            ):
                if (len(document)-1) > len(result):
                    result = {'name': name, **kwargs}
            case _:
                if exclude_id:
                    exclude_id.append(document['_id'])
    return result
