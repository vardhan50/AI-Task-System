from .models import Document

def simple_search(query):
    results = []

    documents = Document.objects.all()

    for doc in documents:
        if query.lower() in doc.content.lower():
            results.append({
                "id": doc.id,
                "title": doc.title,
                "content": doc.content[:200]  # preview
            })

    return results