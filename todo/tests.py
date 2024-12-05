from django.test import TestCase
from .models import Todo

class TodoModelTest(TestCase):
    def test_create_todo(self):
        todo = Todo.objects.create(
            title="Test Task",
            description="This is a test description.",
            tags=["test", "sample"]
        )
        self.assertEqual(todo.title, "Test Task")
        self.assertEqual(todo.status, "OPEN")
