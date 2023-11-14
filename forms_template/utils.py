from motor.motor_asyncio import AsyncIOMotorDatabase


async def find_document(db: AsyncIOMotorDatabase, items: dict):
    collection = db['template']

    # +2 это поле _id, name которые будут в document
    max_len_document = len(items)+2

    query = {'$or': [{key: {'$exists': True}} for key in items.keys()]}
    query.update({'_id': {'$exists': True}, 'name': {'$exists': True}})

    documents = collection.find(query)

    result = []
    async for document in documents:
        if max_len_document < len(document):
            continue
        match document:
            case {'_id': id, 'name': name, **kwargs} if all(
                    item in items.items() for item in kwargs.items()
            ):
                result.append((len(document), {'name': name, **kwargs}))

    result.sort(reverse=True)

    return result[0][1] if result else items
