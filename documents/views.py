from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Document
from .serializers import DocumentSerializer
from .search import simple_search
from logs.models import ActivityLog


# 🔹 Upload Document
@api_view(['GET', 'POST'])
def upload_document(request):

    # 👉 Browser GET
    if request.method == 'GET':
        return Response({
            "message": "Use POST method to upload document"
        })

    # 👉 POST upload
    title = request.data.get('title')
    file = request.FILES.get('file')

    if not title:
        return Response({"error": "Title is required"})

    if not file:
        return Response({"error": "No file uploaded"})

    try:
        content = file.read().decode('utf-8')
    except:
        return Response({"error": "Only .txt files allowed"})

    document = Document.objects.create(
        title=title,
        content=content
    )

    ActivityLog.objects.create(
        user=None,
        action="Document uploaded"
    )

    return Response({
        "message": "Document uploaded successfully",
        "data": {
            "id": document.id,
            "title": document.title
        }
    })


# 🔹 Get All Documents
@api_view(['GET'])
def get_documents(request):
    docs = Document.objects.all()
    serializer = DocumentSerializer(docs, many=True)
    return Response(serializer.data)


# 🔹 Get Single Document
@api_view(['GET'])
def get_document(request, id):
    try:
        doc = Document.objects.get(id=id)
    except Document.DoesNotExist:
        return Response({"error": "Document not found"})

    serializer = DocumentSerializer(doc)
    return Response(serializer.data)


# 🔹 Search Documents
@api_view(['GET'])
def search_documents(request):
    query = request.GET.get('q')

    if not query:
        return Response({"error": "Query parameter 'q' is required"})

    results = simple_search(query)

    ActivityLog.objects.create(
        user=None,
        action=f"Search performed: {query}"
    )

    return Response({
        "query": query,
        "results": results
    })