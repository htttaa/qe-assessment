from playwright.sync_api import Page, expect


class TasksPage:

    def __init__(self, page: Page):
        self.page = page

        # Create Task
        self.task_name = page.locator("#task-name")
        self.task_description = page.locator("#task-description")
        self.task_due_date = page.locator("#task-due-date")
        self.task_urgent = page.locator("#task-urgent")
        self.add_task_button = page.locator("#add-task")

        # Messages
        self.task_success = page.locator("#task-success")
        self.task_error = page.locator("#task-error")

        # Tasks
        self.task_list = page.locator("#task-list")

        # Subtask modal
        self.create_subtask_button = page.locator(".create-subtask")
        self.subtask_modal = page.locator("#subtask-modal")
        self.subtask_task_id = page.locator("#subtask-task-id")
        self.subtask_task_description = page.locator(
            "#subtask-task-description"
        )
        self.subtask_description = page.locator(
            "#subtask-description"
        )
        self.subtask_due_date = page.locator(
            "#subtask-due-date"
        )
        self.add_subtask_button = page.locator(
            "#add-subtask"
        )
        self.subtask_success = page.locator(
            "#subtask-success"
        )
        self.subtask_count = page.locator(
            "#subtask-count"
        )
        self.subtask_list = page.locator(
            "#subtask-list"
        )

    def open(self):
        self.page.goto("http://localhost:8000")

    def create_task(
        self,
        name: str,
        description: str = "",
        due_date: str = "",
        urgent: bool = False,
    ):
        self.task_name.fill(name)

        self.task_description.fill(description)

        if due_date:
            self.task_due_date.fill(due_date)

        if urgent:
            self.task_urgent.check()

        self.add_task_button.click()

    def get_task(self, task_name: str):
        return self.task_list.locator(
            ".task"
        ).filter(
            has_text=task_name
        )

    def open_subtask_modal(self, task_name: str):
        task = self.get_task(task_name)

        task.locator(
            ".create-subtask"
        ).click()

    def create_subtask(
        self,
        description: str,
        due_date: str,
    ):
        self.subtask_description.fill(
            description
        )

        self.subtask_due_date.fill(
            due_date
        )

        self.add_subtask_button.click()