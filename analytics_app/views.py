from rest_framework.decorators import api_view
from rest_framework.response import Response
from tasks.models import Task
from logs.models import ActivityLog


@api_view(['GET'])
def analytics(request):

    # Total tasks
    total_tasks = Task.objects.count()

    # Completed tasks
    completed_tasks = Task.objects.filter(status='completed').count()

    # Pending tasks
    pending_tasks = Task.objects.filter(status='pending').count()

    # Search count (logs lo 'search' keyword base chesi)
    search_count = ActivityLog.objects.filter(action__icontains='search').count()

    return Response({
        "total_tasks": total_tasks,
        "completed_tasks": completed_tasks,
        "pending_tasks": pending_tasks,
        "search_count": search_count
    })