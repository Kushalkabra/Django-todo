from django.test import TestCase
from .models import Todo

class TodoTestCase(TestCase):
    def test_todo_creation(self):
        todo = Todo.objects.create(
            title="Test Task",
            description="This is a test task.",
            tags=["test", "task"],
        )
        self.assertEqual(todo.title, "Test Task")
