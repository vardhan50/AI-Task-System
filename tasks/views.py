from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer
from logs.models import ActivityLog


# 🔹 Create Task
@api_view(['POST'])
def create_task(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

        ActivityLog.objects.create(
            user=None,
            action="Task created"
        )

        return Response({
            "message": "Task created successfully",
            "data": serializer.data
        })
    return Response(serializer.errors)


# 🔹 Get All Tasks
@api_view(['GET'])
def get_tasks(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)


# 🔹 Update Task
@api_view(['GET', 'PUT'])
def update_task(request, id):
    try:
        task = Task.objects.get(id=id)
    except Task.DoesNotExist:
        return Response({"error": "Task not found"})

    # 👉 GET → show task
    if request.method == 'GET':
        serializer = TaskSerializer(task)
        return Response(serializer.data)

    # 👉 PUT → update
    if request.method == 'PUT':
        serializer = TaskSerializer(task, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()

            ActivityLog.objects.create(
                user=None,
                action="Task updated"
            )

            return Response({
                "message": "Task updated successfully",
                "data": serializer.data
            })
        return Response(serializer.errors)